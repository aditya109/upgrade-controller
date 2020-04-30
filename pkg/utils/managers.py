from pkg.core.logger_module.logger import get_configured_logger
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
        logger.info("configured logger object")
        logger.setLevel("DEBUG")
        logger.debug(f"the log file can found out at : C:\\{self.application_name}\\logs\\{self.application_name}_log")
        return logger
