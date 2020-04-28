from abc import ABC, abstractmethod


class UpgradeControllerAbstract(ABC):
    def __init__(self):
        super().__init__()
        self. = ""

    @abstractmethod
    def perform_upgrade(self):
        pass

    @abstractmethod
    def abort_upgrade(self):
        pass


class UpgradeController(UpgradeControllerAbstract):

    def perform_upgrade(self):
        pass

    def abort_upgrade(self):
        pass

