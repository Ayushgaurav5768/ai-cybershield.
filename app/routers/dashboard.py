from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database.db import SessionLocal
from app.models.scan_model import Scan

router = APIRouter()

@router.get("/dashboard")
def get_dashboard():
    db: Session = SessionLocal()

    total_scans = db.query(func.count(Scan.id)).scalar()
    phishing_count = db.query(func.count(Scan.id)) \
                        .filter(Scan.prediction == "Phishing") \
                        .scalar()

    safe_count = db.query(func.count(Scan.id)) \
                    .filter(Scan.prediction == "Safe") \
                    .scalar()

    db.close()

    return {
        "total_scans": total_scans,
        "phishing_count": phishing_count,
        "safe_count": safe_count
    }


@router.get("/recent-scans")
def get_recent_scans():
    db = SessionLocal()

    scans = db.query(Scan) \
              .order_by(Scan.created_at.desc()) \
              .limit(10) \
              .all()

    db.close()

    return [
        {
            "url": scan.url,
            "prediction": scan.prediction,
            "risk_score": scan.risk_score,
            "created_at": scan.created_at
        }
        for scan in scans
    ]
