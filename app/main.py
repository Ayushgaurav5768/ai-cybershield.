from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import scan, dashboard, assistant
from app.database.db import engine
from app.models.scan_model import Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI CyberShield")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(scan.router)
app.include_router(dashboard.router)
app.include_router(assistant.router)

@app.get("/")
def root():
    return {"message": "AI CyberShield Backend Running"}
