import logging
import os

from services import UpgradeControllerAbstract, Repository


class UpgradeController(UpgradeControllerAbstract):

    def __init__(self):
        self.credentials = self.credential_extractor()
        self._repository = Repository()
        self.repository_setter()

        self.application_name = ""
        self.application_name_setter(self._repository.repository_url.split("/")[-1])

        self.logger = logging.getLogger(f'{self.application_name}.upgrade')
        self.logger_config()

    def logger_config(self):
        try:
            os.mkdir(f"{os.getcwd()}\\logs")
        except FileExistsError:
            pass

        self.logger.setLevel(logging.DEBUG)

        # create file handler which logs even debug messages
        fh = logging.FileHandler(f'{os.getcwd()}\\logs\\{self.application_name}.log')
        fh.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.logger.info("Logger Object configured")

    def application_name_setter(self, application_name):
        self.application_name = application_name

    @property
    def repository(self):
        return self._repository

    def repository_setter(self):
        if self.credentials is None:
            self.abort_upgrade()
        else:
            pass
        self._repository.remote_name = "origin"
        self._repository.repository_name = "C:\\tmp\\spring-di"
        self._repository.repository_url = "https://github.com/aditya109/spring-di"

    def __str__(self) -> str:
        return f"UpgradeController ==> \nattribute [repository]: {self._repository}\n" \
               f"attribute [application_name]: {self.application_name}"

    def credential_extractor(self):
        try:
            credential_file = open("repo-ev.txt")
        except FileNotFoundError:
            self.logger.critical("Credential File Not Found")
        finally:
            self.logger.info("Put credential file to continue !")
            self.logger.info("init() failed !")
            return None
        return credential_file.read().split("\n")

    def perform_upgrade(self):
        # f = open("repo-env.txt")
        # credentials = f.read().split("\n")
        # print(credentials)
        # f.close()
        # this completes the configuration of "logger object"
        # sample example of usage of logger object
        # logger.info('creating an instance of auxiliary_module.Auxiliary')
        pass

    def abort_upgrade(self):
        self.logger.critical("Unable to continue upgrade ")
        self.logger.info("Exiting upgrade module...")


ob = UpgradeController()
# ob.perform_upgrade()
# # print(ob)
