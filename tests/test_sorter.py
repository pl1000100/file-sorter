import os
import unittest

from filesorter.sorter import Sorter

class TestSorter(unittest.TestCase):
    def setUp(self):
        files_to_create = ["1", "2", "3.txt", "4.a", "5.a", "6.b", "7.txt", "8"]
        if os.path.exists("./test_dir"):
            os.system("rm -rf ./test_dir")
        os.mkdir("./test_dir")
        os.mkdir("./test_dir/src")
        os.mkdir("./test_dir/src/1to5")
        os.mkdir("./test_dir/dst")
        for i in files_to_create[:5]:
            os.system(f"touch ./test_dir/src/1to5/{i}")
        for i in files_to_create[5:]:
            os.system(f"touch ./test_dir/src/{i}")

    def tearDown(self):
        os.system("rm -rf ./test_dir")
    
    def test_sorter_1(self):
        src = "./test_dir/src"
        args = [src]
        sorter = Sorter(args)
        self.assertFalse(sorter.valid)

    def test_sorter_2(self):
        args = ["-h"]
        sorter = Sorter(args)
        self.assertFalse(sorter.valid)

    def test_sorter_3(self):
        src = "./test_dir/src"
        args = ["--help", src]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)

    def test_sorter_4(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        args = ["-h", src, dst]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)

    def test_sorter_5(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        args = [src, dst]
        sorter = Sorter(args)
        
        self.assertEqual(sorter.source, os.path.abspath(src))
        self.assertEqual(sorter.destination, os.path.abspath(dst))
        self.assertTrue(sorter.valid)

    def test_sorter_6(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        args = ["--log", src, dst]
        sorter = Sorter(args)

        self.assertEqual(sorter.source, os.path.abspath(src))
        self.assertEqual(sorter.destination, os.path.abspath(dst))
        self.assertTrue(sorter.valid)
        
    def test_sorter_7(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        args = [src, "--log", dst]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)

    def test_sorter_8(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        args = [src, dst, "--log"]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)

    def test_sorter_9(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        args = [dst, src, "--log"]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)

    def test_sorter_move_files_1(self):
        src = "./test_dir/src"
        dst = "./test_dir/dst"
        args = [src, dst]
        sorter = Sorter(args)
        expected = [
            "./test_dir/dst/1to5/1",
            "./test_dir/dst/1to5/2",
            "./test_dir/dst/1to5/3.txt",
            "./test_dir/dst/1to5/4.a",
            "./test_dir/dst/1to5/5.a",
            "./test_dir/dst/#b/6.b",
            "./test_dir/dst/#txt/7.txt",
            "./test_dir/dst/8",
        ]

        for d in expected:
            self.assertTrue(os.path.exists(os.path.abspath(d)))
        
        self.assertEqual(sorter.source, os.path.abspath(src))
        self.assertEqual(sorter.destination, os.path.abspath(dst))
        self.assertTrue(sorter.valid)