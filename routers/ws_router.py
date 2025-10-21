# routers/ws_router.py
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from .api_router import generate_reply, append_message, smart_greeting

ws_router = APIRouter()
logger = logging.getLogger("SpeechBot")


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info("Client connected")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            logger.info("Client disconnected")

    async def send(self, websocket: WebSocket, message):
        await websocket.send_json(message)


manager = ConnectionManager()


@ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        greeting = smart_greeting()
        append_message("bot", greeting)
        await manager.send(websocket, {"type": "greet", "reply": greeting})

        while True:
            data = await websocket.receive_json()
            msg_type = data.get("type")

            if msg_type == "message":
                text = (data.get("text") or "").strip()
                if not text:
                    await manager.send(websocket, {"type": "error", "message": "Empty message"})
                    continue
                append_message("user", text)
                result = generate_reply(text)
                append_message("bot", result["reply"])
                await manager.send(websocket, {"type": "reply", **result})

            elif msg_type in ("stop", "abort"):
                await manager.send(websocket, {"type": "ack", "message": f"{msg_type} acknowledged"})
                append_message("user", f"__{msg_type}__")

            else:
                await manager.send(websocket, {"type": "error", "message": f"Unknown type: {msg_type}"})

    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.exception("WebSocket error: %s", e)
        await websocket.close()
