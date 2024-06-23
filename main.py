from app import app
from app.logging.logging_config import setup_logging, get_logger
from app.logging.logging_decorator import log_function_call

setup_logging()
logger = get_logger(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
