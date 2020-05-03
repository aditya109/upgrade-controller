# Class for Repository type Object
class Repository:
    def _init_(self):
        #  _repository_path is the class attribute which stores directory path of the location where the
        # repository needs to be cloned
        self._repository_path = ""

        #  _repository_url is the class attribute which stores git url of the target repository
        self._repository_url = ""

        # _local_commit is the class attribute which stores the current local commit
        self._local_commit = ""

        # _remote_commit is the class attribute which stores the current remote commit
        self._remote_commit = ""

    # The following are the getters and setters of the above class attribute
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
        string_output = ""
        for f in vars(self):
            string_output = string_output + f"{f} : {vars(self)[f]}\n"
        return f"<Repository object>\n{string_output}"
