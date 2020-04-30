from pkg.utils.env import env_getter
from pkg.utils.managers import Logger_Module_Manager


class UpgradeController:
    """
    Class has the prime functionality of driving the upgrade.
    Implementation class for UpgradeControllerAbstract.
    """

    def __init__(self):
        self.logger = None
        self.application_name = env_getter()['APPLICATION_NAME']

    def perform_upgrade(self):
        """
        perform_upgrade manages calls to core-type and service-type pkg(s) and ensures
        smooth installation of rolling upgrade
        """

        # created the logger object of the Logger module
        logger_module_manager = Logger_Module_Manager(self.application_name)
        self.logger = logger_module_manager.get_logger_object()

        self.logger.info("using `logger` as persistent object")


