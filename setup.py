# TODO
from controller.upgrade_ctrlr.upgrade_controller import UpgradeController
from pkg.utils.managers import Dir_Module_Manager

if __name__ == "__main__":

    upgrade_controller = UpgradeController()

    # creating skeleton directory structure of the project
    dir_module_manager = Dir_Module_Manager()

    if dir_module_manager.create_project_directory_structure():
        # TODO abort upgrade
        pass

    upgrade_controller.perform_upgrade()
