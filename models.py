from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class HashSignature(BaseModel):
    name: str
    regex: str
    description: str
    category: str
    confidence_weight: float = 1.0

class IdentificationMatch(BaseModel):
    name: str
    description: str
    category: str
    confidence_score: float

class AnalysisResult(BaseModel):
    hash_string: str
    entropy: float
    length: int
    char_set: str
    matches: List[IdentificationMatch]
    recommendations: List[str]

class BatchResult(BaseModel):
    results: List[AnalysisResult]
    total_processed: int
    summary: Dict[str, int]
