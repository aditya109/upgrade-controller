import os
import shutil
import sys
import unittest
from logging import Logger
from unittest import TestCase

from pkg.utils.env import env_getter
from pkg.utils.managers import Dir_Module_Manager, Logger_Module_Manager


class Test_Utils(TestCase):
    def test_env_getter(self):
        # check for proper functionality of env_getter()
        env = env_getter()
        self.assertTrue(type(env) is dict)

    def test_create_project_directory_structure(self):
        # check for proper functionality of create_project_directory_structure()
        dummy_object = Dir_Module_Manager()
        self.assertTrue(type(dummy_object.create_project_directory_structure()) is bool)
        del dummy_object

    def test_get_logger_object(self):
        # check for proper functionality of get_logger_object()
        dummy_object = Logger_Module_Manager()
        dummy_object.set_logger_object()
        self.assertTrue(type(dummy_object.get_logger_object()) is Logger)
        del dummy_object
