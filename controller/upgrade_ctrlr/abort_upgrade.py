import sys


class AbortUpgradeController:
    def __init__(self):
        pass

    def abort_upgrade(self):
        print("exiting the upgrade")
        sys.exit(0)
