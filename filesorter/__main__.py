import datetime
import os
import sys


def create_date_dir(in_path):
    now = datetime.date.today()
    base_path = f"{in_path.rstrip("/").rstrip("\\")}/{str(now)}"

    if os.path.exists(base_path):
        i = 1
        iter_path = f"{base_path} ({i})"
        while os.path.exists(iter_path):
            i += 1
            iter_path = f"{base_path} ({i})"
        os.mkdir(iter_path)
        return iter_path
    
    os.mkdir(base_path)
    return base_path


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

    date_dir = create_date_dir(args[0])
    items = os.listdir(args[0])


if __name__ == '__main__':
    main()