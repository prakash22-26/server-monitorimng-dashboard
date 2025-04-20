from sqlalchemy import Column, Integer, Float, DateTime, func,String
from .database import Base

class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip = Column(String)
    status = Column(String)
    
class ResourceUsage(Base):
    __tablename__ = "resource_usage"

    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(Float)
    ram = Column(Float)
    disk = Column(Float)
    app = Column(Float)
    timestamp = Column(DateTime, default=func.now())

class NetworkTraffic(Base):
    __tablename__ = "network_traffic"

    id = Column(Integer, primary_key=True, index=True)
    bytes_sent = Column(Float)
    bytes_recv = Column(Float)
    timestamp = Column(DateTime, default=func.now())

class AlertLevel(Base):
    __tablename__ = "alert_levels"

    id = Column(Integer, primary_key=True, index=True)
    critical = Column(Integer)
    medium = Column(Integer)
    low = Column(Integer)
    timestamp = Column(DateTime, default=func.now())