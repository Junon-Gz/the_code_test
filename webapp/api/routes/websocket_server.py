from fastapi import APIRouter, WebSocket,WebSocketDisconnect
from fastapi.responses import HTMLResponse
from utils.websocket_utils import ConnectionManager
from utils.websocket_utils import generate_websocket_test_page

manager = ConnectionManager()

router = APIRouter()

@router.get("/chat/{client_id}")
async def get_websocket_test_page(client_id: str):
    return HTMLResponse(generate_websocket_test_page(str(client_id)))

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    await manager.broadcast(f"Client{client_id} Joined the chat")
    try:
        while True:
            data = await websocket.receive_text()
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client{client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client{client_id} left the chat")