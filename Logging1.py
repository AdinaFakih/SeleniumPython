import logging
logging.basicConfig(filename="C://Users//addyf//Desktop//Certificates//test.log",
                    format='%(asctime)s: %(levelname)s:  %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                    )

logging.debug("This is debug message")
logging.info("This is info msg")
logging.warning("This is warning msg")
logging.error("This is error msg")
logging.critical("This is critical msg")