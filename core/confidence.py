from typing import List
from pxhash.models import HashSignature

def calculate_confidence(hash_string: str, signature: HashSignature) -> float:
    """
    Calculates a confidence score for a given hash and signature match.
    Logic considers length specificity and character set constraints.
    """
    base_weight = signature.confidence_weight
    
    # Simple length-based adjustment
    # More specific signatures (longer or with more complex patterns) get higher scores
    length_factor = min(len(hash_string) / 64.0, 1.0)
    
    # Pattern complexity adjustment (basic implementation)
    # Regexes with more special characters are considered more specific
    complexity = sum(1 for c in signature.regex if c in "$.|()*+?\\")
    complexity_factor = min(complexity / 10.0, 0.2)
    
    score = (base_weight * 0.8) + (length_factor * 0.1) + complexity_factor
    
    return min(round(score, 2), 1.0)
