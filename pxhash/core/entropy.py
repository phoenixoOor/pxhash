import math
from collections import Counter

def calculate_shannon_entropy(data: str) -> float:
    """
    Calculates the Shannon entropy of a string.
    Entropy is a measure of randomness.
    """
    if not data:
        return 0.0
    
    counts = Counter(data)
    total_len = len(data)
    
    entropy = 0.0
    for count in counts.values():
        probability = count / total_len
        entropy -= probability * math.log2(probability)
        
    return round(entropy, 4)

def analyze_character_set(data: str) -> str:
    """Identifies the character set used in the string."""
    if all(c in "0123456789" for c in data):
        return "Numeric"
    if all(c in "0123456789abcdefABCDEF" for c in data):
        return "Hexadecimal"
    if all(c in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=" for c in data):
        return "Base64"
    return "Alpha-numeric/Special"
