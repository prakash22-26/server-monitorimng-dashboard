from fastapi import FastAPI
from app import models
from app.database import engine  
from fastapi.middleware.cors import CORSMiddleware
from app.routers import monitor,ws 

app = FastAPI() 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(monitor.router)

app.include_router(ws.router)

models.Base.metadata.create_all(bind=engine) 

@app.get("/")
def read_root():
    return {"message": "Server Monitoring API is running"}
