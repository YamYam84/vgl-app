from functools import wraps
from app.logging.logging_config import get_logger

logger = get_logger(__name__)

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Entering: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.debug(f"Exiting: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}", exc_info=True)
            raise
    return wrapper
