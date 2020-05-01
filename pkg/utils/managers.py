import os
import requests
from pkg.core.logger_module.logger import get_configured_logger
from pkg.core.repository_module.repo_builder import RepositoryBuilder
from pkg.service.dir_manager.file_struct_creater import DirectoryPath
from pkg.utils.env import env_getter


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

    def get_logger_object(self):
        logger = get_configured_logger(self.application_name)
        logger.setLevel("INFO")
        logger.setLevel("DEBUG")
        logger.debug(f"the log file can found out at : C:\\{self.application_name}\\logs\\{self.application_name}_log")
        logger.info("successfully configured `logger` object")
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

    def __init__(self, logger):
        self.logger = logger

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
            self.logger.info("successfully created and configured `repository` object")
            return repository
