import sys
import os

import yaml

from controller.upgrade_ctrlr.abort_upgrade import AbortUpgradeController


def env_getter():
    """
    Extracts the envs from the `env.yaml` and returns a dictionary
    full of envs
    :return: dict
    """
    env_dict = {}
    try:
        path = ""
        for f in sys.path:
            if "upgrade-controller" in f:
                # getting the reset path of upgrade-controller to locate env.yaml
                path = f.split("upgrade-controller")[0] + "upgrade-controller"

        with open(path+"\\env.yaml", "r") as file:
            env_dict = yaml.full_load(file)

    except FileNotFoundError:
        print("env.yaml is not available")
        # self.logger.critical("aborting upgrade")
        AbortUpgradeController().abort_upgrade()
    else:
        return env_dict
