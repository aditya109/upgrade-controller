import os
from services import CoreGitOpsAbstract, GitOpsWrapperAbstract
import logging


class CoreGitOps(CoreGitOpsAbstract):
    def __init__(self):
        super().__init__()

    def get_status(self):
        pass

    def do_plain_clone(self):
        pass

    def do_hard_reset(self):
        pass

    def do_pull(self):
        pass


class GitOpsWrapper(GitOpsWrapperAbstract):
    def __init__(self):
        self.log = None
        super().__init__()

    def check_repository_existence(self):
        try :
            path = "C:\\temp"
            status = os.stat(path)
            print(status)
        except FileNotFoundError :
            logging.INFO(f"the system cannot find the file specified: {path}")

    def compare_local_remote_commit(self):
        pass


obj = GitOpsWrapper()
obj.check_repository_existence()
