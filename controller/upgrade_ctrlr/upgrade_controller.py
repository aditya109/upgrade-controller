import os

from controller.upgrade_ctrlr.abort_upgrade import AbortUpgradeController
from pkg.utils.env import env_getter
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
        """perform_upgrade manages calls to core-type and service-type pkg(s) and ensures
        smooth installation of rolling upgrade
        """

        # created the logger object of the Logger module
        logger_module_manager = Logger_Module_Manager()
        self.logger = logger_module_manager.get_logger_object()

        # created the repository object of the Repository module
        repository_module_manager = Repository_Module_Manager()
        self.repository = repository_module_manager.build_repo_envs()

        # check if the repository object is initialized
        if self.repository is None:
            self.logger.setLevel("CRITICAL")
            self.logger.critical("aborting upgrade")
            AbortUpgradeController().abort_upgrade()


        REPO_DIRECTORY = env_getter()['REPO_PATH']

        # created a core_git_ops_manager object of CoreGitOpsManager class
        core_git_ops_manager = CoreGitOpsManager(self.repository)

        # git operation flow
        if not os.listdir(REPO_DIRECTORY):
            # check if the repository directory is empty
            # if yes then clone the repository
            clone_state = core_git_ops_manager.perform_clone()
            if clone_state is None:
                AbortUpgradeController().abort_upgrade()
        else:
            # if no then pull the repository
            pull_state = core_git_ops_manager.perform_pull()

            if pull_state is None:
                AbortUpgradeController().abort_upgrade()

