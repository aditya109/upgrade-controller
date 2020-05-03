from controller.upgrade_ctrlr.abort_upgrade import AbortUpgradeController
from pkg.utils.managers import Logger_Module_Manager, Repository_Module_Manager, CoreGitOpsManager


class UpgradeController:
    """
    Class has the prime functionality of driving the upgrade.
    Implementation class for UpgradeControllerAbstract.
    """

    def __init__(self):
        self.logger = None
        self.repository = None

    def perform_upgrade(self):
        """
        perform_upgrade manages calls to core-type and service-type pkg(s) and ensures
        smooth installation of rolling upgrade
        """

        # created the logger object of the Logger module
        logger_module_manager = Logger_Module_Manager()

        self.logger = logger_module_manager.get_logger_object()

        repository_module_manager = Repository_Module_Manager()
        self.repository = repository_module_manager.build_repo_envs()

        if self.repository is None:
            # TODO handle abort
            self.logger.setLevel("CRITICAL")
            self.logger.critical("aborting upgrade")
            pass

        # testing code TODO
        core_git_ops_manager = CoreGitOpsManager(self.repository)
        clone_state = core_git_ops_manager.perform_clone()

        if clone_state is None:
            AbortUpgradeController().abort_upgrade()