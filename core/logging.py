import logging
from core.config import settings

def setup_logging():
    """
    Configura e retorna um logger com handlers para console e arquivo.
    """
    logger = logging.getLogger("api_users")
    logger.setLevel(settings.LOG_LEVEL)

    if not logger.handlers:
        file_handler = logging.FileHandler(settings.LOG_FILE_PATH)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

log = setup_logging()