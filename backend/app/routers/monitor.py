from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/servers", response_model=list[schemas.ServerSchema])
def get_servers(db: Session = Depends(get_db)):
    return db.query(models.Server).all()

@router.get("/usage", response_model=list[schemas.UsageSchema])
def get_usage(db: Session = Depends(get_db)):
    return db.query(models.ResourceUsage).all()

@router.get("/network", response_model=list[schemas.NetworkTrafficSchema])
def get_network_traffic(db: Session = Depends(get_db)):
    return db.query(models.NetworkTraffic).all()

@router.get("/alerts", response_model=list[schemas.AlertLevelSchema])
def get_alert_levels(db: Session = Depends(get_db)):
    return db.query(models.AlertLevel).all()
