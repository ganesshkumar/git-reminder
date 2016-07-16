import logging
from enum import Enum
from telegram_helper import send_message


logging.basicConfig()
logger = logging.getLogger('message_processor')

class Commands(Enum):
    echo = 1

def process_incoming_message(text):
    try:
        if text.startswith('/' + Commands.echo.name):
            payload = text.split(Commands.echo.name)[1].strip()
            send_message(payload)

    except KeyError:
        logger.error('Command Not Found')
