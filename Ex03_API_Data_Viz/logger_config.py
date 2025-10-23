import logging
import logging.handlers
import os
from datetime import datetime

LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    
LOG_FILE = os.path.join(LOG_DIR, datetime.now().strftime('app_%Y%m%d_%H%M%S.log'))

def setup_logger(name):
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    # 콘솔에 표시
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # 로그파일에 표시
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE, maxBytes = 1024*1024*5, backupCount=5, encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
    return logger