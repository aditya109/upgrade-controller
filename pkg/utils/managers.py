import os
import requests
from pkg.core.logger_module.logger import LoggerL
from pkg.core.repository_module.repo_builder import RepositoryBuilder
from pkg.service.dir_manager.file_struct_creater import DirectoryPath
from pkg.utils.env import env_getter
from pkg.service.gitops_main.gitops_main import CoreGitOpsImpl

class Dir_Module_Manager:
    """
    Dir_Module_Manager is responsible for creating application directory
    structure and prep it for further usage
    """

    def __init__(self):
        self.directory_path_object = None
        envs = env_getter()
        self.dir_paths = envs['PATHS']
        self.application_name = envs['APPLICATION_NAME']

    def create_project_directory_structure(self):
        """
        ABORT_STATE = False -> No Error
        ABORT_STATE = True -> Module Failure
        """
        self.directory_path_object = DirectoryPath()
        for path in self.dir_paths:
            self.directory_path_object.add_path(path)
        self.directory_path_object.make_all_path()
        return self.directory_path_object.ABORT_STATE


class Logger_Module_Manager:
    """
    Logger_Module_Manager is responsible for creating logger object
    """

    def __init__(self):
        self.application_name = env_getter()['APPLICATION_NAME']

    def set_logger_object(self):
        """
        Instantiates the logger object and dumps into a temp file
        :return:
        """
        LoggerL().create_logger()


    def get_logger_object(self):
        """
        Makes static access call to get_logger() of LoggerL class
        :return: Logger
        """
        logger = LoggerL().get_logger()
        logger.setLevel("INFO")
        logger.setLevel("DEBUG")
        logger.debug(f"log file can found out at : C:\\{self.application_name}\\logs\\{self.application_name}_log")
        logger.info("`logger` object get operation SUCCESS !")
        return logger


class InvalidRepositoryEnvException(Exception):
    """
        Exception occurs when url entered is invalid
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"{InvalidRepositoryEnvException}: url is invalid"


class Repository_Module_Manager:
    """
    Class create a repository object from `env.yaml`
    """

    def __init__(self):
        self.logger = LoggerL().get_logger()

    def build_repo_envs(self):
        """
        Builds the repository object using RepositoryBuilder available
        :return: Repository
        """
        envs = env_getter()
        repo_path, local_commit, remote_commit = envs['REPO_PATH'], "", ""
        repo_maker = envs["REPO_MAKER_GITHUB_HANDLE"]
        repo_name = envs["REPO_NAME"]
        repo_url = f"https://github.com/{repo_maker}/{repo_name}"

        try :
            # check for invalid envs in `env.yaml`
            self.logger.info("checking for invalid ENVS in `env.yaml`")
            if (not os.path.exists(repo_path)) or ("message" in requests.get(
                    url=f"https://api.github.com/repos/{repo_maker}/{repo_name}").json()):
                raise InvalidRepositoryEnvException
        except InvalidRepositoryEnvException:
            self.logger.critical("Invalid REPO_URL or REPO_PATH in `env.yaml`")
            return None
        else:
            self.logger.info("ENV validation SUCCESS !!")
            self.logger.info("building `repository` object using implemented builder")
            repository_builder = RepositoryBuilder()
            repository = repository_builder \
                .clone_at \
                .clone_at_path(path=repo_path) \
                .clone_from \
                .clone_url(url=repo_url) \
                .has_local \
                .has_local_commit(local_commit=local_commit) \
                .has_remote \
                .has_remote_commit(remote_commit=remote_commit) \
                .build()
            self.logger.info("creation and configuration of `repository` object SUCCESS !")
            return repository


class CoreGitOpsManager:
    def __init__(self, repository):
        self.logger = Logger_Module_Manager().get_logger_object()
        self.repository = repository

    def perform_clone(self):
        self.logger.setLevel("INFO")
        self.logger.info("initiating operation : git clone")
        o = CoreGitOpsImpl(self.logger, self.repository)
        return o.do_plain_clone()


    def perform_pull(self):
        self.logger.setLevel("INFO")
        self.logger.info("initiating operation : git pull")
        o = CoreGitOpsImpl(self.logger, self.repository)
        return o.do_pull()

