import os
import shutil
import unittest
from unittest import TestCase

from pkg.services.dir_manager.file_struct_creater import DirectoryPath


class TestDirectoryPath(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dummy_object = None
        cls.good_path = "C:\\fakeapp\\logs"
        cls.bad_path = "C:\\<>%^##fakeapp\\logs"
        cls.empty_path = ""
        cls.__path = [cls.good_path, cls.bad_path, cls.empty_path]

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.dummy_object
        for path in cls.__path:
            if os.path.exists(path):
                shutil.rmtree(path, ignore_errors=False, onerror=None)

    def setUp(self) -> None:
        self.dummy_object = DirectoryPath()

    def tearDown(self) -> None:
        self.dummy_object = None

    # test case for make_all_path()
    def test_make_all_path(self):
        # checking for good path directory creation
        self.setUp()

        self.dummy_object.add_path(self.good_path)
        self.dummy_object.make_all_path()
        result = os.path.exists(self.good_path)
        self.assertTrue(result)

        # checking for triggers for already existing directory creation
        self.dummy_object.make_all_path()
        self.assertFalse(self.dummy_object.ABORT_STATE)

        self.tearDown()

    # test case for add_path()
    def test_add_path(self):
        # checking for invalid path append
        self.setUp()
        self.dummy_object.add_path(self.bad_path)
        self.assertTrue(self.dummy_object.ABORT_STATE)

        # checking for empty path
        self.setUp()
        fake_list = []
        self.dummy_object.add_path(self.empty_path)
        self.assertEqual(self.dummy_object.dir_structure, fake_list)

        # checking for good path
        self.setUp()
        self.dummy_object.add_path(self.good_path)
        self.assertFalse(self.dummy_object.ABORT_STATE)

        self.tearDown()


if __name__ == "__main__":
    unittest.main()
