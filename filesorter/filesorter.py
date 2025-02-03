from .movestrategy import MoveStrategy, MoveNoSort

class FileSorter():
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        
    def move_files(self, move_strategy: MoveStrategy=MoveNoSort):
        move_strategy.move(self.src, self.dst)

