# TODO
from controller.upgrade_ctrlr.abort_upgrade import AbortUpgradeController
from controller.upgrade_ctrlr.upgrade_controller import UpgradeController
from pkg.utils.managers import Dir_Module_Manager, Logger_Module_Manager

if __name__ == "__main__":

    # creating skeleton directory structure of the project
    dir_module_manager = Dir_Module_Manager()
    project_skeleton_state = dir_module_manager.create_project_directory_structure()

    logger_module_manager = Logger_Module_Manager()
    logger_module_manager.set_logger_object()

    if project_skeleton_state:
        AbortUpgradeController().abort_upgrade()
        pass

    upgrade_controller = UpgradeController()
    upgrade_controller.perform_upgrade()
