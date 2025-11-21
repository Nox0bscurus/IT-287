import logging
import traceback

# Configure logging to write to a file
logging.basicConfig(
    filename='game.log',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def error(message):
    logging.error(message)

def p(message):
    logging.info(message)

def warning(message):
    logging.warning(message)