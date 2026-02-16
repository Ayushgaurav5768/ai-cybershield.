from fastapi import APIRouter
from app.schemas.scan_schema import ScanRequest, ScanResponse
from app.services.feature_extractor import extract_features
from app.services.prediction_service import predict_url
from app.services.explanation_service import generate_explanation
from app.database.db import SessionLocal
from app.models.scan_model import Scan


router = APIRouter()

@router.post("/scan", response_model=ScanResponse)
def scan_url(data: ScanRequest):
    features = extract_features(data.url)
    prediction, risk_score = predict_url(features)
    reasons = generate_explanation(data.url, features)

    # Save to database
    db = SessionLocal()
    new_scan = Scan(
        url=data.url,
        prediction=prediction,
        risk_score=risk_score
    )
    db.add(new_scan)
    db.commit()
    db.close()

    return {
        "prediction": prediction,
        "risk_score": risk_score,
        "reasons": reasons
    }

