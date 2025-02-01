import os
import sys

from .funcs import create_date_dir, move_files


def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("Usage:\nfilesorter <folder>")
        sys.exit(1)
    if len(args) > 1:
        print("Not executed, too many arguments!")
        sys.exit(1)
    if not os.path.isdir(args[0]):
        print(f"{args[0]} is not a valid dir")
        sys.exit(1)
    # if os.exists(args[0]):
    date_dir = create_date_dir(args[0])
    move_files(args[0], date_dir)


if __name__ == '__main__':
    main()
