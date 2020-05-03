from pkg.utils.env import env_getter
from pkg.utils.managers import Logger_Module_Manager, Repository_Module_Manager


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
        logger_module_manager = Logger_Module_Manager()
        logger_module_manager.set_logger_object()

        self.logger = logger_module_manager.get_logger_object()

        repository_module_manager = Repository_Module_Manager()
        repository = repository_module_manager.build_repo_envs()

        if repository is None:
            # TODO handle abort
            self.logger.setLevel("CRITICAL")
            self.logger.critical("aborting upgrade")
            pass