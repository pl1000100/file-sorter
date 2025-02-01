import datetime
import os
import re


def create_date_dir(in_path):
    today = datetime.date.today()
    base_path = f"{in_path.rstrip("/").rstrip("\\")}/{str(today)}"

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


def move_files(src, dst):
    pattern = r'^\d{4}-\d{2}-\d{2}( \(\d+\))?(\.txt)?'
    regex = re.compile(pattern)
    src = src.rstrip("/")
    items = os.listdir(src)

    to_move = [item for item in items if not regex.match(item)]
    for item in to_move:
        os.system(f"mv -v '{src}/{item}' '{dst}' >> './{dst}.txt'")
