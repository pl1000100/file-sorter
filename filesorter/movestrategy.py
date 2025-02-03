import os
import shutil

from abc import ABC, abstractmethod


class MoveStrategy(ABC):
    @abstractmethod
    def move(self, src, dst):
        pass


class MoveNoSort(MoveStrategy):
    def move(self, src, dst):
        for i in os.listdir(src):
            shutil.move(os.path.join(src, i), dst)
        # try:
        #     shutil.move(src, dst)
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
        pass