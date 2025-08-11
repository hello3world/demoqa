"""
Logging configuration for DemoQA project
"""
import logging
import os
from datetime import datetime

def setup_logger(name='demoqa', level=logging.INFO):
    """Sets up and returns a logger"""
    
    # Create logs directory
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    
    # Form log file name
    log_file = f"{log_dir}/demoqa_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Clear existing handlers
    if logger.handlers:
        logger.handlers.clear()
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Create main logger
logger = setup_logger() 