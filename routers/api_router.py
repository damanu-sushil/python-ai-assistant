# routers/api_router.py
import json
import datetime
import re
import smtplib
import logging
import webbrowser
from pathlib import Path
from threading import Lock
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from pydantic import BaseModel, EmailStr
import os
from dotenv import load_dotenv

# --- Local imports ---
from modules.talk import greet, talk
from modules.search import search_web
from modules.sendmail import send_email as module_send_email
from modules.weather_info import get_weather

load_dotenv()
logger = logging.getLogger("AIDEN")

api_router = APIRouter()

APP_NAME = os.getenv("APP_NAME", "AIDEN")
ROOT = Path(__file__).parent.parent
STATIC_DIR = ROOT / "static"
CONV_FILE = ROOT / "conversations.json"
STATIC_DIR.mkdir(parents=True, exist_ok=True)

if not CONV_FILE.exists():
    CONV_FILE.write_text(json.dumps({"conversations": []}, indent=2), encoding="utf-8")

_file_lock = Lock()


class MessageIn(BaseModel):
    text: str
    user: str = "user"


class EmailIn(BaseModel):
    recipient: EmailStr
    subject: str
    message: str


# --- File Helpers ---
def _load_conversations():
    with _file_lock:
        with open(CONV_FILE, "r", encoding="utf-8") as f:
            return json.load(f)


def _save_conversations(data):
    with _file_lock:
        with open(CONV_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


def append_message(sender, text):
    data = _load_conversations()
    item = {"sender": sender, "text": text, "ts": datetime.datetime.utcnow().isoformat() + "Z"}
    data.setdefault("conversations", []).append(item)
    _save_conversations(data)


# --- Greeting ---
def get_time_based_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 17:
        return "Good afternoon!"
    elif 17 <= hour < 21:
        return "Good evening!"
    else:
        return "Good night!"


def smart_greeting():
    if greet:
        greet()
    greeting = get_time_based_greeting()
    talk(greeting)
    return f"{greeting} I'm {APP_NAME}. How can I help you?"


# --- Email ---
def send_email_safe(recipient, subject, message):
    try:
        return module_send_email(recipient, subject, message)
    except Exception as e:
        logger.warning("Email send failed: %s", e)
        return f"Failed to send email: {e}"


# --- Reply Logic ---
def generate_reply(text: str):
    t = text.lower().strip()

    if re.search(r"\b(hi|hello|hey|good morning|good afternoon|good evening|good night)\b", t):
        g = get_time_based_greeting()
        talk(g)
        return {"reply": f"{g} How can I help you?", "action": "none"}

    if "time" in t:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return {"reply": f"The current time is {now}.", "action": "none"}

    if "weather" in t:
        city_match = re.search(r"weather(?: in)? ([a-zA-Z\s\-]+)", t)
        if city_match:
            city = city_match.group(1)
            info = get_weather(city)
            return {"reply": f"The weather in {city} is {info}.", "action": "none"}
        return {"reply": "Please tell me which city.", "action": "ask_city"}

    # --- Wikipedia / Google ---
    if re.search(r"\b(who is|what is|tell me about)\b", t):
        query = text.strip("?")
        try:
            answer = search_web(query)
            if answer:
                talk(answer)
                return {"reply": answer, "action": "none"}
        except Exception:
            pass
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)
        talk(f"I opened Google for {query}.")
        return {"reply": f"I opened Google for {query}.", "action": "open_url", "url": url}

    if "open youtube" in t:
        webbrowser.open("https://www.youtube.com")
        talk("Opening YouTube now.")
        return {"reply": "Opening YouTube.", "action": "open_url", "url": "https://www.youtube.com"}

    return {"reply": f"I heard: '{text}'.", "action": "none"}


# --- API Routes ---
@api_router.get("/")
async def root():
    html_path = STATIC_DIR / "aiden-pro.html"
    if html_path.exists():
        return FileResponse(str(html_path))
    greeting = smart_greeting()
    return HTMLResponse(f"<h3>{greeting}</h3>")


@api_router.get("/greet")
async def greet_endpoint():
    greeting = smart_greeting()
    append_message("bot", greeting)
    return JSONResponse({"message": greeting})


@api_router.post("/message")
async def message_endpoint(msg: MessageIn):
    if not msg.text.strip():
        raise HTTPException(status_code=400, detail="Empty message")
    append_message("user", msg.text)
    result = generate_reply(msg.text)
    append_message("bot", result["reply"])
    return JSONResponse(result)


@api_router.post("/email")
async def email_endpoint(email: EmailIn, background: BackgroundTasks):
    def send_task():
        result = send_email_safe(email.recipient, email.subject, email.message)
        append_message("bot", result)

    background.add_task(send_task)
    append_message("user", f"Send email to {email.recipient}")
    return JSONResponse({"status": "sending"})


@api_router.get("/history")
async def history_endpoint():
    return _load_conversations()


@api_router.post("/clear")
async def clear_endpoint():
    _save_conversations({"conversations": []})
    return JSONResponse({"status": "cleared"})
