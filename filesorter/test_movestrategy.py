import os
import shutil
import unittest

from movestrategy import MoveNoSort, MoveSortByExtension, MoveSortByModificationDate

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

    def test_MoveNoSort_1(self):
        test_path = "./test_dir"
        src = os.path.join(test_path, "src")
        dst = os.path.join(test_path, "dst")
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(os.path.join(src, "1"))
        self.create_file(os.path.join(src, "1/a.txt"))
        self.create_file(os.path.join(src, "1/b.txt"))
        os.mkdir(os.path.join(src, "2"))
        MoveNoSort().move(src, dst)

        self.assertTrue(os.path.exists(os.path.join(dst, "1/a.txt")))
        self.assertTrue(os.path.exists(os.path.join(dst, "1/b.txt")))

    def test_MoveSortByExtension_1(self):
        test_path = "./test_dir"
        src = os.path.join(test_path, "src")
        dst = os.path.join(test_path, "dst")
        os.mkdir(src)
        os.mkdir(dst)
        os.mkdir(os.path.join(src, "1"))
        self.create_file(os.path.join(src, "1/a.txt"))
        self.create_file(os.path.join(src, "1/b.ext"))
        os.mkdir(os.path.join(src, "2"))
        self.create_file(os.path.join(src, "2/c.ext"))
        self.create_file(os.path.join(src, "2/d.ext"))
        self.create_file(os.path.join(src, "e.txt"))
        self.create_file(os.path.join(src, "f.txt"))
        self.create_file(os.path.join(src, "g.ext"))
        MoveSortByExtension().move(src, dst)

        self.assertTrue(os.path.exists(os.path.join(dst, "1/a.txt")))
        self.assertTrue(os.path.exists(os.path.join(dst, "1/b.ext")))
        self.assertTrue(os.path.exists(os.path.join(dst, "2/c.ext")))
        self.assertTrue(os.path.exists(os.path.join(dst, "2/d.ext")))
        self.assertTrue(os.path.exists(os.path.join(dst, "txt/e.txt")))
        self.assertTrue(os.path.exists(os.path.join(dst, "txt/f.txt")))
        self.assertTrue(os.path.exists(os.path.join(dst, "ext/g.ext")))
