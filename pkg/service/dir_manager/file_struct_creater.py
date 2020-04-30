import os


class InvalidPathException(Exception):
    """
    Exception occurs when path entered cannot exist
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"{InvalidPathException}: path is invalid"


class EmptyPathException(Exception):
    """
    Exception occurs when and empty path is tried to be created
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"{EmptyPathException}: path is empty"


class DirectoryPath:
    """
    Class creates skeleton directory setup for the project
    """
    def __init__(self):

        # dir_structure holds the directory path
        self.dir_structure = []

        # ABORT_STATE report module failure
        self.ABORT_STATE = False

    def add_path(self, path):
        """
        Returns False if the path addition was a SUCCESS, else returns True
        in case, of path addition operation FAILURE
        :param path:
        :return: bool
        """
        try:
            if len(path) == 0:
                # Check for empty path
                raise EmptyPathException
            # Check for invalid path
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
            # Declaring Failure
            self.ABORT_STATE = True
        except EmptyPathException:
            print("Cannot push empty path for directory structure")
        else:
            # Append path to project directory structure
            self.dir_structure.append(path)

    @staticmethod
    def create_directory(cur_path):
        """
        Helper module to perform the recursive directory creation according to path given
        :param cur_path:
        :return:
        """
        cur_path = cur_path.split("\\")
        test_path = ""
        for dir in cur_path:
            test_path = f"{test_path}{dir}\\"
            if not os.path.exists(test_path):
                os.mkdir(test_path)

    def make_all_path(self):
        """
        Perform directory structure creation all paths in dir_structure
        :return: None
        """
        for path in self.dir_structure:
            if os.path.exists(path):
                # print(f"{path} \n--> path exists\n--> skipping directory creation")
                pass
            else:
                # print(f"{path}\n--> path does not exist")
                # print("--> attempting directory creation")
                try:
                    DirectoryPath.create_directory(path)
                except Exception:
                    # print(f"--> make directory attempt FAIL")
                    self.ABORT_STATE = True
                    break
                else:
                    # print(f"--> make directory attempt SUCCESS")
                    pass

    def __str__(self) -> str:
        """
        Prints present value of instance attribute `dir_structure`
        :return: string
        """
        dir_structure = "Current Directory Structure:\n__________________________\n"
        for path in self.dir_structure:
            dir_structure = f"{dir_structure}{path}\n"
        return dir_structure



