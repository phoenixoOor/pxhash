import re

def is_hex(s: str) -> bool:
    """Checks if a string is a valid hexadecimal string."""
    return bool(re.fullmatch(r"^[0-9a-fA-F]+$", s))

def is_base64(s: str) -> bool:
    """Checks if a string is a valid base64 string."""
    return bool(re.fullmatch(r"^[A-Za-z0-9+/]+={0,2}$", s))
