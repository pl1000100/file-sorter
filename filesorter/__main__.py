import argparse

from .filesorter import FileSorter
from.movestrategy import MoveNoSort, MoveSortByExtension, MoveSortByModificationDate


def main():
    parser = argparse.ArgumentParser(description="Command Line File Sorter")
    parser.add_argument("src", help="path to source folder")
    parser.add_argument("dst", help="path to destination folder")
    
    parser.add_argument("-l", "--log", help="log moved files to txt file", action="store_true")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()
    fs = FileSorter(args.src, args.dst)
    fs.move_files(MoveSortByExtension)



if __name__ == '__main__':
    main()
