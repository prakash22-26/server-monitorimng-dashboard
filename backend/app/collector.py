import time
import psutil
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models

def collect_and_store():
    while True:
        db: Session = SessionLocal()

        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        net_io = psutil.net_io_counters()
        app_usage = 35  # Placeholder for now

        usage = models.ResourceUsage(
            cpu=cpu,
            ram=ram,
            disk=disk,
            app=app_usage
        )
        db.add(usage)

        net = models.NetworkTraffic(
            bytes_sent=net_io.bytes_sent,
            bytes_recv=net_io.bytes_recv
        )
        db.add(net)

        # Alert levels could be set based on logic
        alerts = models.AlertLevel(
            critical=2,
            medium=6,
            low=10
        )
        db.add(alerts)

        db.commit()
        db.close()

        time.sleep(10)  # Collect every 10 seconds
