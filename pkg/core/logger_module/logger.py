# TODO
import logging
import os

application_name = "brsv"


class UnknownLoggingConfigurationException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"{UnknownLoggingConfigurationException}: Logging Configuration parameter is unknown"


class LevelLogger:
    def __init__(self):
        self._level_logger = ""

    @property
    def level_logger(self):
        return self._level_logger

    @level_logger.setter
    def level_logger(self, application_name):
        self._level_logger = logging.getLogger(f'{application_name}.upgrade')

    def configure_logger(self, handler_configuration_type):
        try:
            handler_configuration_type = handler_configuration_type.upper()
            if handler_configuration_type == "ERROR":
                config = logging.ERROR
            elif handler_configuration_type == "INFO":
                config = logging.INFO
            elif handler_configuration_type == "CRITICAL":
                config = logging.CRITICAL
            elif handler_configuration_type == "WARNING":
                config = logging.INFO
            elif handler_configuration_type == "DEBUG":
                config = logging.DEBUG
        except UnknownLoggingConfigurationException:
            config = logging.DEBUG
            print("logging configuration is set to enable DEBUG mode")

        cwd = os.getcwd()
        cwd = cwd.split("\\")

        try:
            os.mkdir(f"{cwd[0]}\\{application_name}\\upgrade-logs\\logs")
        except FileExistsError:
            pass
        handler = None
        if config == logging.ERROR:
            handler = logging.StreamHandler()
            handler.setLevel(config)
        else:
            handler = logging.FileHandler(f'{os.getcwd()}\\logs\\{application_name}.log')
            handler.setLevel(config)
            print(f'{cwd[0]}\\{application_name}\\upgrade-logs\\logs\\{application_name}.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.level_logger.addHandler(handler)
        self.level_logger.info("Logger Object Configured")


o = LevelLogger()
o.level_logger = application_name
o.configure_logger("INFO")
#