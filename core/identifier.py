import re
import json
from typing import List
from models import HashSignature, IdentificationMatch
from config import SIGNATURES_PATH
from core.confidence import calculate_confidence
from logger import logger

class HashIdentifier:
    def __init__(self):
        self.signatures: List[HashSignature] = self._load_signatures()

    def _load_signatures(self) -> List[HashSignature]:
        try:
            with open(SIGNATURES_PATH, "r") as f:
                data = json.load(f)
                return [HashSignature(**sig) for sig in data]
        except Exception as e:
            logger.error(f"Failed to load signatures: {e}")
            return []

    def identify(self, hash_string: str) -> List[IdentificationMatch]:
        """Identifies potential hash types for a given string."""
        matches = []
        hash_string = hash_string.strip()
        
        for sig in self.signatures:
            if re.match(sig.regex, hash_string, re.IGNORECASE):
                confidence = calculate_confidence(hash_string, sig)
                matches.append(IdentificationMatch(
                    name=sig.name,
                    description=sig.description,
                    category=sig.category,
                    confidence_score=confidence
                ))
        
        # Sort matches by confidence score descending
        return sorted(matches, key=lambda x: x.confidence_score, reverse=True)
