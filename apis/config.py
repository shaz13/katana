import logging
from pathlib import Path

APP_ROOT = Path("./core")
MODEL_ROOT = APP_ROOT / "models" / "logreg.pkl"
TEMP_CSV = APP_ROOT / "dataset" / "diabetes.csv"


class ColorFormatter(logging.Formatter):
    """Logging Formatter to add colors for warning, errors etc"""

    blue = '\x1b[94m'
    green = '\x1b[92m'
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: bold_red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
