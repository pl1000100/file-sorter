import os
import sys


class Sorter():
    def __init__(self, args):
        self.source = None
        self.destination = None
        self.log = None
        self.valid = False
        self.msg = None
        self._handle_args(args)

    def _handle_args(self, args):
        if len(args) < 2 and ("-h" not in args and "--help" not in args):
            self.msg = "Not enough arguments\nTry filesorter -h for help"
            return
        
        if "-h" in args or "--help" in args:
            self.msg = "filesorter [-f --flag] <src> <dst>   copies files from source directory to destination sorting therm by file type.\n\n" \
                           "It will create destination directort if it doesn't exists.\n\n" \
                           "Flags:\n" \
                           "-h, --help          quick info about available flags\n" \
                           "--log-default       logs all moved files and dirs into file in destination dir"
            return
        
        # Past help and 2 args minimum
        self.source = os.path.abspath(args[-2])
        self.destination = os.path.abspath(args[-1])
        if not os.path.isdir(self.source):
            self.msg = "Source not valid"
            return
        self.valid = True

        for flag in args[:-2]:
            f = flag.split("=", 1)
            flag_name = f[0]
            flag_value = None
            if len(f) > 1:
                flag_value = f[1]
            match flag_name:
                case "--log":
                    self.log = os.path.dirname(self.destination)
                case _:
                    self.msg = f"Unsupported: {flag_name}"
                    self.valid = False
            

