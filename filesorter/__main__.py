import argparse

from filesorter.file_sorter import FileSorter
from filesorter.movestrategy import NoSort, SortByExtension, SortByModificationDate


def main():
    parser = argparse.ArgumentParser(description="Command Line File Sorter")
    parser.add_argument("src", help="path to source folder")
    parser.add_argument("dst", help="path to destination folder")
    
    parser.add_argument("-e", "--extension", help="sort files by extension", action="store_true")
    parser.add_argument("-d", "--date", help="sort files by modification date", action="store_true")
    parser.add_argument("-l", "--log", help="log moved files to txt file", action="store_true")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    fs = FileSorter(args.src, args.dst, args.verbose)
    if args.extension:
        fs.move_files(SortByExtension)
    elif args.date:
        fs.move_files(SortByModificationDate)
    else:
        fs.move_files(NoSort)


if __name__ == '__main__':
    main()
