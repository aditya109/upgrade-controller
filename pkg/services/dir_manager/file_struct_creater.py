import os
import re
import shutil


class InvalidPathException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"{InvalidPathException}: path is invalid"


class EmptyPathException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"{EmptyPathException}: path is empty"


class DirectoryPath:
    def __init__(self):
        self.dir_structure = []
        self.ABORT_STATE = False

    def add_path(self, path):
        try:
            if len(path) == 0:
                raise EmptyPathException
            special_chars = ["\\", ":", "_"]
            valid_chars = []
            alpha = "A"
            for i in range(0, 26):
                valid_chars.append(alpha)
                valid_chars.append(chr(ord(alpha) + 32))
                alpha = chr(ord(alpha) + 1)
            for ch in special_chars:
                valid_chars.append(ch)
            for f in path:
                if f not in valid_chars:
                    raise InvalidPathException
        except InvalidPathException:
            self.ABORT_STATE = True
        except EmptyPathException:
            print("Cannot push empty path for directory structure")
        else:
            self.dir_structure.append(path)

    @staticmethod
    def create_directory(cur_path):
        cur_path = cur_path.split("\\")
        test_path = ""
        for dir in cur_path :
            test_path = f"{test_path}{dir}\\"
            if not os.path.exists(test_path):
                os.mkdir(test_path)

    def make_all_path(self):

        for path in self.dir_structure:
            if os.path.exists(path):
                print(f"{path} \n--> path exists\n--> skipping directory creation")
            else:
                print(f"{path}\n--> path does not exist")
                print("--> attempting directory creation")
                try:
                    DirectoryPath.create_directory(path)
                except Exception:
                    print(f"--> make directory attempt FAIL")
                    self.ABORT_STATE = True
                    break
                else:
                    print(f"--> make directory attempt SUCCESS")
            return

    def __str__(self) -> str:
        dir_structure = "Current Directory Structure:\n__________________________\n"
        for path in self.dir_structure:
            dir_structure = f"{dir_structure}{path}\n"
        return dir_structure


# application_name = "brsv"
# d = DirectoryPath()
# bad_path = "C:\\&(*&(*&fakeapp\\brsv"
# d.add_path(bad_path)
# d.make_all_path()
#
#
# d.add_path(f"C:\\{application_name}\\output")
# d.add_path(f"C:\\{application_name}\\repo")
# d.add_path(f"C:")
# d.add_path(f"C>>>:\\{application_name}")
# d.make_all_path()
# if d.ABORT_STATE:
#     print("FAIL")
# else :
#     print("OK")
