import os
import sys

from .sorter import Sorter


def main():
    args = sys.argv[1:]
    s = Sorter(args)
    print(s.msg)




    # if len(args) < 2 and ("-h" not in args and "--help" not in args):
    #     print("Usage:\nfilesorter [-f --flag] <src> <dst>")
    #     sys.exit(2)
    
    # if "-h" in args or "--help" in args:
    #     print("filesorter - copies files from source directory to destination sorting therm by file type\n" \
    #           "It will create destination directort if it doesn't exists"
    #           "Usage: filesorter [-f --flag] <src> <dst>\n\n" \
    #           "Flags:\n" \
    #           "-h, --help   Quick info about available flags"
    #           "--log-default   logs all moved files and dirs into file in destination dir"
    #     )
    #     sys.exit(1)

    

    # src_dir = os.path.abspath(args[-2])
    # dst_dir = os.path.abspath(args[-1])
    # log = None

    # flags = args[:-2]
    # if len(flags) > 0:
    #     index = 0
    #     while index < len(flags):
    #         match flags[index]:
    #             case "--log":
    #                 log = os.path.dirname(dst_dir)
    #                 index += 1
    #             case _:
    #                 print(f"Unsupported: {flags[index]}")
    #                 sys.exit(2)

    # if not os.path.isdir(src_dir) or os.listdir(src_dir) == []:
    #     print(f"Directory don't exists or empty")
    #     sys.exit(1)

    
    
    # dst_dir = args[-2].rstrip("/")
    
    # if not os.path.isdir(source_dir):
    #     print(f"{source_dir} is not a valid dir")
    #     sys.exit(1)
    # if os.listdir(source_dir) == []:
    #     print(f"{source_dir} is empty")
    #     sys.exit(1)

    


if __name__ == '__main__':
    main()
