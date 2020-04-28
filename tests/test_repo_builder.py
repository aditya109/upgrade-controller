from unittest import TestCase

from pkg.core.repository_module.repo_builder import RepositoryBuilder
from pkg.core.repository_module.repository import Repository


class Test_Repository_Builder(TestCase):
    def test_build(self):
        # Fake Values
        path = "D:\\tmp\\repo"
        url = "https://github.com/aditya109/testing124"
        local_commit = "444ec7d15f1f89352cef47a9bea52087315b36b3"
        remote_commit = "c038cd7aafc88b8795ff3730d550453edeb38e18"

        # Creating Repository Object manually
        comparator_repository = Repository()
        comparator_repository.repository_path = path
        comparator_repository.repository_url = url
        comparator_repository.local_commit = local_commit
        comparator_repository.remote_commit = remote_commit

        # Creating Repository Object using RepositoryBuilder
        builder_repository = RepositoryBuilder()
        test_repository = builder_repository \
            .clone_at \
            .clone_at_path(path) \
            .clone_from \
            .clone_url(url) \
            .has_local \
            .has_local_commit(local_commit) \
            .has_remote \
            .has_remote_commit(remote_commit) \
            .build()

        self.assertEqual(test_repository.local_commit, comparator_repository.local_commit)
        self.assertEqual(test_repository.remote_commit, comparator_repository.remote_commit)
        self.assertEqual(test_repository.repository_path, comparator_repository.repository_path)
        self.assertEqual(test_repository.repository_url, comparator_repository.repository_url)
