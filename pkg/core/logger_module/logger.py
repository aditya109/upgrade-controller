import logging
import pickle
import sys

from pkg.utils.env import env_getter


class LoggerL:
    def __init__(self):
        self.application_name = env_getter()['APPLICATION_NAME']

    def create_logger(self):
        logger = logging.getLogger(f"{self.application_name}-logs")

        # configuration of handlers for logger objects
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f"C:\\{self.application_name}\\logs\\{self.application_name}_log.txt", "w")

        # creating formatter
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

        # setting formatter for logger objects
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # adding handlers for logger objects
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

        logger.setLevel("INFO")
        logger.info("`logger` object creation SUCCESS !")

        for f in sys.path:
            if "upgrade-controller" in f:
                # getting the reset path of upgrade-controller to locate logger
                path = f.split("upgrade-controller")[0] + "upgrade-controller\\pkg\\core\\logger_module"

        # dumping `logger` object in logger file
        with open(path + "\\logger", "wb") as logger_ob_file:
            pickle.dump(logger, logger_ob_file)

        logger.setLevel("DEBUG")
        logger.debug("`logger` object binary_file_dump SUCCESS !")

    @staticmethod
    def get_logger():
        logger = None
        for f in sys.path:
            if "upgrade-controller" in f:
                # getting the reset path of upgrade-controller to locate logger
                path = f.split("upgrade-controller")[0] + "upgrade-controller\\pkg\\core\\logger_module"

        # dumping `logger` object in logger file
        with open(path + "\\logger", "rb") as logger_ob_file:
            logger = pickle.load(logger_ob_file)
        logger.setLevel("DEBUG")
        # logger.debug("`logger` object binary_file_dump retrieval SUCCESS !")
        return logger

