from fastapi import WebSocket
from jinja2 import Template
from pathlib import Path
from typing import Any

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


def render_websocket_template(*, template_name: str, context: dict[str, Any]) -> str:
    template_str = (
        Path(__file__).parent.parent / "static" / "page" / template_name
    ).read_text()
    html_content = Template(template_str).render(context)
    return html_content

def generate_websocket_test_page(id: str) -> str:
    return render_websocket_template(template_name="websocket_test_page.html", context={"id":id})