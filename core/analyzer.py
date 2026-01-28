from typing import List, Optional
from models import AnalysisResult, IdentificationMatch
from core.identifier import HashIdentifier
from core.entropy import calculate_shannon_entropy, analyze_character_set

class HashAnalyzer:
    def __init__(self):
        self.identifier = HashIdentifier()

    def analyze(self, hash_string: str) -> AnalysisResult:
        """Performs full analysis on a single hash string."""
        matches = self.identifier.identify(hash_string)
        entropy = calculate_shannon_entropy(hash_string)
        char_set = analyze_character_set(hash_string)
        
        recommendations = self._generate_recommendations(hash_string, matches, entropy)
        
        return AnalysisResult(
            hash_string=hash_string,
            entropy=entropy,
            length=len(hash_string),
            char_set=char_set,
            matches=matches,
            recommendations=recommendations
        )

    def _generate_recommendations(self, 
                                 hash_string: str, 
                                 matches: List[IdentificationMatch], 
                                 entropy: float) -> List[str]:
        recommendations = []
        
        if not matches:
            recommendations.append("No common hash patterns identified. This might be a custom format or encrypted data.")
        
        top_match = matches[0].name if matches else None
        
        if top_match in ["MD5", "SHA-1"]:
            recommendations.append(f"{top_match} is considered cryptographically broken. Avoid using for security-sensitive applications.")
        
        if entropy < 3.0:
            recommendations.append("Low entropy detected. The string may have low randomness or follow a highly structured pattern.")
        
        if "Password Hash" in [m.category for m in matches]:
            recommendations.append("This appears to be a password hash. Ensure it is stored securely and use modern algorithms like Argon2 for new implementations.")

        return recommendations
