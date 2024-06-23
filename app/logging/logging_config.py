import logging
import logging.config
import os
from datetime import datetime

def setup_logging(default_level=logging.DEBUG):
    log_filename = f"app_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': default_level,
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'level': default_level,
                'filename': f'app/logging/{log_filename}',
                'mode': 'a',
            },
        },
        'root': {
            'handlers': ['console', 'file'],
            'level': default_level,
        },
        'loggers': {
            '__main__': {
                'handlers': ['console', 'file'],
                'level': default_level,
                'propagate': False
            },
        }
    }

    logging.config.dictConfig(logging_config)

def get_logger(name):
    return logging.getLogger(name)
