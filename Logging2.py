import logging
logging.basicConfig(filename="C://Users//addyf//Desktop//Certificates//test.log",
                    format='%(asctime)s: %(levelname)s:  %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', )
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("This is debug message")
logger.info("This is info msg")
logger.warning("This is warning msg")
logger.error("This is error msg")
logger.critical("This is critical msg")