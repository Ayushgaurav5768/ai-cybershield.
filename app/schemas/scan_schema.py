from pydantic import BaseModel
from typing import List

class ScanRequest(BaseModel):
    url: str

class ScanResponse(BaseModel):
    prediction: str
    risk_score: int
    reasons: List[str]
