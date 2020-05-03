from abc import abstractmethod, ABC

import git
from git import GitCommandError


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


class CoreGitOpsImpl(CoreGitOpsAbstract):
    def __init__(self, logger, repository):
        super().__init__()
        self.logger = logger
        self.repository = repository

    def get_status(self):
        # TODO
        pass

    def do_plain_clone(self):
        self.logger.info("info core-git-ops-impl")
        try :
            clone_result = git.Repo.clone_from(self.repository.repository_url, self.repository.repository_path)

        except GitCommandError:
            self.logger.critical(f"destination path {self.repository.repository_path} already exists and is not an empty directory")
        else:
            # returns something like this <git.repo.base.Repo 'C:\\BRSV\\tmp\\setup\\.git'> as result
            return clone_result

    def do_hard_reset(self):
        # TODO
        pass

    def do_pull(self):
        # TODO
        # DIR_NAME = "D:\\tmp"
        # REMOTE_URL = "https://github.com/aditya109/Bank-Reconcilation-Statement-Validator.git"
        #
        # os.mkdir(DIR_NAME)
        #
        # repo = git.Repo.init(None)
        # origin = repo.create_remote('origin', REMOTE_URL)
        # origin.fetch()
        # origin.pull(origin.refs[0].remote_head)
        # print("______________DONE______________")
        pass


"""
# if __name__ == "__main__":
#     obj = CoreGitOps()
# git.Repo.clone_from("https://github.com/aditya109/testing124", "D://tmp//repo")

repo=git.Repo("D://tmp//repo//")
# print(repo.head.commit.diff(None))

# config = None
# commit_format = (config or {}).get("commit_format", "Release {version}")
# if repo.head.ref != repo.heads.master :
#     raise Exception("You need to be on `master` branch in order to do a release")

# if repo.is_dirty():
#     raise Exception("Git repository has unstaged changes.")

# if len(repo.untracked_files) > 0 :
#     raise Exception('Git repository has untracked files')

# print(repo.head.commit)
# repo.remotes.origin.fetch()

# repo.remotes.origin.pull(origin.refs[0].remote_head)

# if repo.remotes.origin.refs.master.commit != repo.head.ref.commit :
#     raise Exception("Master has unsynced changes ")
# print(repo.head.commit)


# DIR_NAME = "D:\\tmp\\repo"
# REMOTE_URL = "https://github.com/aditya109/testing124"

# repo.remotes.origin.fetch()
# repo.remotes.origin.pull(repo.remotes.origin.refs[0].remote_head)
# print("______________DONE______________")
"""
