import datetime
import os


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