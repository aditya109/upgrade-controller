# TODO
import logging
import os
from abc import ABC, abstractmethod


class GitOpsWrapperAbstract(ABC):
    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def check_repository_existence(self):
        pass

    @abstractmethod
    def compare_local_remote_commit(self):
        pass


class GitOpsWrapperImpl(GitOpsWrapperAbstract):
    def __init__(self):
        super().__init__()
        pass

    def check_repository_existence(self):
        try:
            path = "C:\\temp"
            status = os.stat(path)
            print(status)
        except FileNotFoundError:
            logging.INFO(f"the system cannot find the file specified: {path}")

    def compare_local_remote_commit(self):
        pass
