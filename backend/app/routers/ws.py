import json
import psutil
import asyncio
import socket
from datetime import datetime
from fastapi import APIRouter, WebSocket

router = APIRouter()

def get_app_cpu_usage(app_name):
    total_cpu = 0.0
    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            if app_name.lower() in proc.info['name'].lower():
                total_cpu += proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return total_cpu

@router.websocket("/ws/updates")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            app_cpu = get_app_cpu_usage("python")

            alerts = {
                "critical": int(cpu > 50 or ram > 50 or disk > 50),
                "medium": int(25 < cpu <= 25 or 50 < ram <= 25),
                "low": int(cpu <= 50 and ram <= 60)
            }

            data = {
                "alerts": alerts,
                "usage": [
                    {"name": "CPU", "value": cpu},
                    {"name": "RAM", "value": ram},
                    {"name": "Disk", "value": disk},
                    {"name": "App", "value": (app_cpu, 2)}
                ],
                "networkTraffic": {
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "traffic": psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
                },
                "servers": [
                    {
                        "id": 1,
                        "name": socket.gethostname(),
                        "ip": socket.gethostbyname(socket.gethostname()),
                        "status": "Online"
                    }
                ]
            }

            await websocket.send_text(json.dumps(data))
            await asyncio.sleep(2)

    except Exception as e:
        print("WebSocket error:", e)
        await websocket.close()
