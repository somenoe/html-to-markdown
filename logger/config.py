import logging
import colorlog
from pathlib import Path
from datetime import datetime

# Create this as a module-level variable so it's only computed once
LOG_DIR = Path("data/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")


def setup_logger(name: str = __name__) -> logging.Logger:
    # Use pre-computed values
    log_file = LOG_DIR / f"audiobook_generation_{TIMESTAMP}.log"

    # Get or create logger
    if name in logging.Logger.manager.loggerDict:
        return logging.getLogger(name)

    # Set up new logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.handlers = []

    # Set up colored logging for console
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING': 'yellow',
            'ERROR':   'red',
            'CRITICAL': 'red,bg_white',
        }
    ))

    # File handler for logging to file
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'))

    # Add handlers
    logger.addHandler(handler)
    logger.addHandler(file_handler)
    logger.propagate = False

    return logger
