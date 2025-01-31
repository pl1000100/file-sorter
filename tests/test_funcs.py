import datetime
import os
import unittest

from filesorter.funcs import create_date_dir

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
        