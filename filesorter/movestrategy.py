import os
import shutil
import time

from abc import ABC, abstractmethod


class MoveStrategy(ABC):
    @abstractmethod
    def move(src, dst):
        pass


class MoveNoSort(MoveStrategy):
    def move(self, src, dst):
        if os.path.isfile(src):
            shutil.move(src, os.path.join(dst, os.path.basename(src)))
        if os.path.isfile(src):
            return
        for i in os.listdir(src):
            shutil.move(os.path.join(src, i), dst)
        # try:
        #     for i in os.listdir(src):
        #         shutil.move(os.path.join(src, i), dst)
        # except shutil.Error as e:
        #     print(e)


class MoveSortByExtension(MoveStrategy):
    def move(self, src, dst):
        def move_file(src_file, dst_dir):
            file = os.path.basename(src_file).split(".")
            if len(file) > 1:
                ext_dir = os.path.join(dst_dir, file[-1])
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                shutil.move(src_file, os.path.join(ext_dir, os.path.basename(src_file)))
            else:
                shutil.move(src_file, dst_dir)

        if os.path.isfile(src):
            move_file(src, dst)
            return

        items = os.listdir(src)
        files = list(filter(lambda item: os.path.isfile(os.path.join(src, item)), items))
        dirs = list(filter(lambda item: os.path.isdir(os.path.join(src, item)), items))

        for d in dirs:
            shutil.move(os.path.join(src, d), dst)
        for f in files:
            move_file(os.path.join(src, f), dst)
        

class MoveSortByModificationDate(MoveStrategy):
    def move(self, src, dst):
        def _get_modification_date(file_path):
            mod_time = os.path.getmtime(file_path)
            return time.strftime('%Y-%m-%d', time.localtime(mod_time))
        
        def move_file(src_file, dst_dir):
            mod_date = _get_modification_date(src_file)
            mod_dir = os.path.join(dst_dir, mod_date)
            if not os.path.exists(mod_dir):
                os.makedirs(mod_dir)
            shutil.move(src_file, os.path.join(mod_dir, os.path.basename(src_file)))
        if os.path.isfile(src):
            move_file(src, dst)
            return
        for i in os.listdir(src):
            move_file(os.path.join(src, i), dst)

    