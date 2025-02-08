import time
import os
import shutil
import datetime
import unittest

from filesorter.movestrategy import NoSort, SortByExtension, SortByModificationDate
from filesorter.file_sorter import FileSorter

class TestMoveStrategy(unittest.TestCase):
    def setUp(self):
        test_path = "./test_dir"
        if os.path.exists(test_path):
            shutil.rmtree(test_path)
        os.mkdir(test_path)

    # def tearDown(self):
    #     test_path = "./test_dir"
    #     shutil.rmtree(test_path)

    def create_file(self, path):
        with open(path, 'w') as file:
            pass
        
    def test_filesorter_move_NoSort_1(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(src + "/1")
        os.mkdir(src + "/1/2")
        os.mkdir(src + "/1/2/3")
        self.create_file(src + "/a.txt")
        self.create_file(src + "/1/a.txt")
        self.create_file(src + "/1/2/a.txt")
        self.create_file(src + "/1/2/3/a.txt")
        fs = FileSorter(src, dst)
        fs.move_files(NoSort)
        self.assertTrue(os.path.exists(dst + "/a.txt"))
        self.assertTrue(os.path.exists(dst + "/1/a.txt"))
        self.assertTrue(os.path.exists(dst + "/1/2/a.txt"))
        self.assertTrue(os.path.exists(dst + "/1/2/3/a.txt"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_NoSort_2(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        fs = FileSorter(src, dst)
        fs.move_files(NoSort)
        self.assertTrue(os.path.exists(dst))
        self.assertTrue(os.listdir(dst) == [])
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_NoSort_3(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        self.create_file(src + "/a.txt")
        fs = FileSorter(src, dst)
        fs.move_files(NoSort)
        self.assertTrue(os.path.exists(dst + "/a.txt"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_NoSort_4(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(src + "/1")
        fs = FileSorter(src, dst)
        fs.move_files(NoSort)
        self.assertTrue(os.path.exists(dst + "/1"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_SortByModificationDate_1(self):
        today = datetime.date.today()
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(src + "/1")
        os.mkdir(src + "/1/2")
        os.mkdir(src + "/1/2/3")
        self.create_file(src + "/a.txt")
        self.create_file(src + "/1/a.txt")
        self.create_file(src + "/1/2/a.txt")
        self.create_file(src + "/1/2/3/a.txt")
        fs = FileSorter(src, dst)
        fs.move_files(SortByModificationDate)
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/a.txt"))
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/1/a.txt"))
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/1/2/a.txt"))
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/1/2/3/a.txt"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_SortByModificationDate_2(self):
        today = datetime.date.today()
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(src + "/1")
        os.mkdir(src + "/1/2")
        os.mkdir(src + "/1/2/3")
        self.create_file(src + "/a.txt")
        self.create_file(src + "/1/a.txt")
        self.create_file(src + "/1/2/a.txt")
        self.create_file(src + "/1/2/3/a.txt")
        first_january = datetime.date(2025, 1, 1)
        os.utime(src + "/a.txt", (time.mktime(first_january.timetuple()), time.mktime(first_january.timetuple())))
        os.utime(src + "/1/a.txt", (time.mktime(first_january.timetuple()), time.mktime(first_january.timetuple())))
        fs = FileSorter(src, dst)
        fs.move_files(SortByModificationDate)
        self.assertTrue(os.path.exists(dst + f"/{first_january}" + "/a.txt"))
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/1/a.txt"))
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/1/2/a.txt"))
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/1/2/3/a.txt"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_SortByModificationDate_3(self):
        today = datetime.date.today()
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(src + "/1")
        fs = FileSorter(src, dst)
        fs.move_files(SortByModificationDate)
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/1"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_SortByModificationDate_4(self):
        today = datetime.date.today()
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        self.create_file(src + "/a.txt")
        fs = FileSorter(src, dst)
        fs.move_files(SortByModificationDate)
        self.assertTrue(os.path.exists(dst + f"/{today}" + "/a.txt"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_SortByModificationDate_5(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        fs = FileSorter(src, dst)
        fs.move_files(SortByModificationDate)
        self.assertTrue(os.path.exists(dst))
        self.assertTrue(os.listdir(src) == [])
        
    def test_filesorter_move_SortByExtension_1(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(src + "/1")
        os.mkdir(src + "/1/2")
        os.mkdir(src + "/1/2/3")
        self.create_file(src + "/a.txt")
        self.create_file(src + "/1/a.txt")
        self.create_file(src + "/1/2/a.txt")
        self.create_file(src + "/1/2/3/a.txt")
        fs = FileSorter(src, dst)
        fs.move_files(SortByExtension)
        self.assertTrue(os.path.exists(dst + "/txt/a.txt"))
        self.assertTrue(os.path.exists(dst + "/1/a.txt"))
        self.assertTrue(os.path.exists(dst + "/1/2/a.txt"))
        self.assertTrue(os.path.exists(dst + "/1/2/3/a.txt"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_SortByExtension_2(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        self.create_file(src + "/a.txt")
        fs = FileSorter(src, dst)
        fs.move_files(SortByExtension)
        self.assertTrue(os.path.exists(dst + "/txt/a.txt"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_SortByExtension_3(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(src + "/1")
        fs = FileSorter(src, dst)
        fs.move_files(SortByExtension)
        self.assertTrue(os.path.exists(dst + "/1"))
        self.assertTrue(os.listdir(src) == [])

    def test_filesorter_move_SortByExtension_4(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        os.mkdir(src)
        os.mkdir(dst)
        fs = FileSorter(src, dst)
        fs.move_files(SortByExtension)
        self.assertTrue(os.path.exists(dst))
        self.assertTrue(os.listdir(src) == [])
