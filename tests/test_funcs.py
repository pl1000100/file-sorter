import datetime
import os
import unittest

from filesorter.funcs import create_date_dir, move_files

class TestFuncs(unittest.TestCase):
    def test_create_date_dir(self):
        today = datetime.date.today()
        if os.path.exists("./test_dir"):
            os.system("rm -rf ./test_dir")
        os.mkdir("./test_dir")

        create_date_dir("./test_dir")
        create_date_dir("./test_dir")

        self.assertTrue(os.path.exists(f"./test_dir/{str(today)}"))
        self.assertTrue(os.path.exists(f"./test_dir/{str(today)} (1)"))
        os.system("rm -rf ./test_dir")
        
    def test_move_files(self):
        today = datetime.date.today()
        if os.path.exists("./test_dir"):
            os.system("rm -rf ./test_dir")
        os.mkdir("./test_dir")
        create_date_dir("./test_dir")
        with open('./test_dir/1.txt', 'w') as fp:
            pass
        with open('./test_dir/2.txt', 'w') as fp:
            pass
        with open('./test_dir/1', 'w') as fp:
            pass

        move_files("./test_dir", f"./test_dir/{str(today)}")

        self.assertTrue(os.path.exists(f"./test_dir/{str(today)}/1.txt"))
        self.assertTrue(os.path.exists(f"./test_dir/{str(today)}/2.txt"))
        self.assertTrue(os.path.exists(f"./test_dir/{str(today)}/1"))
        os.system("rm -rf ./test_dir")
        