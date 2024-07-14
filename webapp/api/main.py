from fastapi import APIRouter

from api.routes import websocket_server

api_router = APIRouter()
api_router.include_router(websocket_server.router, tags=["websocket_server"])