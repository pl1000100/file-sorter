import unittest

from filesorter.sorter import Sorter

class TestSorter(unittest.TestCase):
    def test_sorter_1(self):
        src = "/home"
        args = [src]
        sorter = Sorter(args)
        self.assertFalse(sorter.valid)

    def test_sorter_2(self):
        args = ["-h"]
        sorter = Sorter(args)
        self.assertFalse(sorter.valid)

    def test_sorter_3(self):
        src = "/home"
        args = ["--help", src]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)

    def test_sorter_4(self):
        src = "/home"
        dst = "/some/other/directory"
        args = ["-h", src, dst]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)

    def test_sorter_5(self):
        src = "/home"
        dst = "/some/other/directory"
        args = [src, dst]
        sorter = Sorter(args)
        
        self.assertEqual(sorter.source, src)
        self.assertEqual(sorter.destination, dst)
        self.assertTrue(sorter.valid)

    def test_sorter_6(self):
        src = "/home"
        dst = "/some/other/directory"
        args = ["--log", src, dst]
        sorter = Sorter(args)

        self.assertEqual(sorter.source, src)
        self.assertEqual(sorter.destination, dst)
        self.assertTrue(sorter.valid)
        
    def test_sorter_7(self):
        src = "/home"
        dst = "/some/other/directory"
        args = [src, "--log", dst]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)

    def test_sorter_8(self):
        src = "/home"
        dst = "/some/other/directory"
        args = [src, dst, "--log"]
        sorter = Sorter(args)

        self.assertFalse(sorter.valid)