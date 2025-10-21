# app.py
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from routers.api_router import api_router
from routers.ws_router import ws_router

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "SpeechBot")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(APP_NAME)

app = FastAPI(title=f"{APP_NAME} API")

# --- Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(api_router, tags=["API"])
app.include_router(ws_router, tags=["WebSocket"])

# --- Run Server ---
if __name__ == "__main__":
    import uvicorn
    logger.info(f"{APP_NAME} started successfully!")
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
