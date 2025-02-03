from .movestrategy import MoveStrategy, MoveNoSort

class FileSorter():
    def __init__(self, src, dst, verbose=False):
        self.src = src
        self.dst = dst
        self.verbose = verbose
        
    def move_files(self, move_strategy: MoveStrategy=MoveNoSort):
        move_strategy.move(self.src, self.dst, self.verbose)

