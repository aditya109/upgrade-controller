from abc import abstractmethod, ABC
import logging
from pprint import pprint


class Repository:
    def _init_(self):
        self._repository_path = ""
        self._repository_url = ""
        self._remote_name = ""
        self._local_commit = ""
        self._remote_commit = ""

    @property
    def repository_path(self):
        return self._repository_path

    @repository_path.setter
    def repository_path(self, repository_path):
        self._repository_path = repository_path

    @property
    def repository_url(self):
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        self._repository_url = repository_url

    @property
    def remote_name(self):
        return self._remote_name

    @remote_name.setter
    def remote_name(self, remote_name):
        self._remote_name = remote_name

    @property
    def local_commit(self):
        return self._local_commit

    @local_commit.setter
    def local_commit(self, local_commit):
        self._local_commit = local_commit

    @property
    def remote_commit(self):
        return self._remote_commit

    @remote_commit.setter
    def remote_commit(self, remote_commit):
        self._remote_commit = remote_commit

    def __str__(self) -> str:
        return f"<Repository object> {vars(self)}"

class CoreGitOpsAbstract(ABC):
    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def do_plain_clone(self):
        pass

    @abstractmethod
    def do_hard_reset(self):
        pass

    @abstractmethod
    def do_pull(self):
        pass


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


class UpgradeControllerAbstract(ABC):
    def __init__(self):
        super().__init__()
        self._version = ""

    @abstractmethod
    def perform_upgrade(self):
        pass
