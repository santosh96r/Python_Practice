import logging 
# logging.basicConfig(level=logging.DEBUG, filemode="w", filename="abc.log",datefmt="", )

class LoggerDemo:
    def sample_logger(self):
        # create logger 
        logger = logging.getLogger("demolog")
        logger.setLevel(logging.DEBUG)

        #create console handler or file handler and set the log level 

        consoleHandler = logging.StreamHandler()
        filehandler = logging.FileHandler("logs/filehandler.log")

        # create formatter 

        formatter = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s ", datefmt="%d/%m/%Y %I:%M:%S: %p")


        # add formatter to console or file handler 

        consoleHandler.setFormatter(formatter)
        filehandler.setFormatter(formatter)

        # add console handler to logger 

        logger.addHandler(consoleHandler)
        logger.addHandler(filehandler)

        # application code 

        logger.debug("debug log statement ")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement ")
        logger.critical("critical log statement ")

obj1 = LoggerDemo()
obj1.sample_logger()