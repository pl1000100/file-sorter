from filesorter.movestrategy import NoSort
from filesorter.funcs import move_func

class FileSorter():
    def __init__(self, src, dst, verbose=False):
        self.src = src
        self.dst = dst
        self.verbose = verbose
        
    def move_files(self, move_strategy=NoSort):
        move_strategy().move(move_func, self.src, self.dst, self.verbose)
        