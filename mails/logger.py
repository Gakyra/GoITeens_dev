import logging

logger = logging.getLogger('mails')

def log_message(message):
    logger.error(message)

log_message("Aboba")
