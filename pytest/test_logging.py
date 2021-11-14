import logging

logger = logging.getLogger(__name__)

logger.addHandler()
finalhandler = logging.FileHandler('logfile.log')
logger.debug('Debug Statement is executed')
logger.info("Information")
logger.warning("Warning Statement")
logger.error("A major error")
logger.critical("Critical Issue")
