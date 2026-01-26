import logging
import sys
from rich.logging import RichHandler

def setup_logger(name: str = "pxhash", level: int = logging.INFO) -> logging.Logger:
    """Configures a professional logger using rich for colored output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding handlers multiple times if setup is called again
    if not logger.handlers:
        handler = RichHandler(rich_tracebacks=True, markup=True)
        formatter = logging.Formatter("%(message)s", datefmt="[%X]")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

logger = setup_logger()
