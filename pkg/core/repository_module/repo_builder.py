from pkg.core.repository_module.repository import Repository


# Primary Builder for Repository type Object
class RepositoryBuilder:
    def __init__(self, repository=None):
        if repository is None:
            self.repository = Repository()
        else:
            self.repository = repository

    # The following are the piecewise builder classes

    # Piecewise Builder class call for Repository Path
    @property
    def clone_at(self):
        return RepositoryPathBuilder(self.repository)

    # Piecewise Builder class call for Repository Url
    @property
    def clone_from(self):
        return RepositoryURLBuilder(self.repository)

    # Piecewise Builder class call for Repository Remote Commit
    @property
    def has_remote(self):
        return RepositoryRemoteCommitBuilder(self.repository)

    # Piecewise Builder class call for Repository Local Commit
    @property
    def has_local(self):
        return RepositoryLocalCommitBuilder(self.repository)

    def build(self):
        return self.repository


# Piecewise Builder class for Repository Path
class RepositoryPathBuilder(RepositoryBuilder):
    def __init__(self, repository):
        super().__init__(repository)

    def clone_at_path(self, path):
        self.repository._repository_path = path
        return self


# Piecewise Builder class for Repository URL
class RepositoryURLBuilder(RepositoryBuilder):
    def __init__(self, repository):
        super().__init__(repository)

    def clone_url(self, url):
        self.repository._repository_url = url
        return self


# Piecewise Builder class for Repository Remote Commit
class RepositoryRemoteCommitBuilder(RepositoryBuilder):
    def __init__(self, repository):
        super().__init__(repository)

    def has_remote_commit(self, remote_commit):
        self.repository._remote_commit = remote_commit
        return self


# Piecewise Builder class for Repository Local Commit
class RepositoryLocalCommitBuilder(RepositoryBuilder):
    def __init__(self, repository):
        super().__init__(repository)

    def has_local_commit(self, local_commit):
        self.repository._local_commit = local_commit
        return self

