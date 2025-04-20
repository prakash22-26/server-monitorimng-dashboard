from pydantic import BaseModel
from datetime import datetime

class ServerSchema(BaseModel):
    id: int
    name: str
    ip_address: str

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2


class UsageSchema(BaseModel):
    id: int
    cpu: float
    ram: float
    disk: float
    app: float
    timestamp: datetime

    class Config:
        from_attributes = True


class NetworkTrafficSchema(BaseModel):
    id: int
    bytes_sent: float
    bytes_recv: float
    timestamp: datetime

    class Config:
        from_attributes = True


class AlertLevelSchema(BaseModel):
    id: int
    critical: int
    medium: int
    low: int
    timestamp: datetime

    class Config:
        from_attributes = True
