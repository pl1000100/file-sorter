import os
import shutil

from abc import ABC, abstractmethod


class MoveStrategy(ABC):
    @abstractmethod
    def move(src, dst):
        pass


class MoveNoSort(MoveStrategy):
    def move(src, dst):
        try:
            shutil.move(src, dst)
        except shutil.Error as e:
            print(e)


class MoveSortByExtension(MoveStrategy):
    def move(src, dst):
        if os.path.isdir(src):
            items = os.listdir(src)
            files = list(filter(lambda x: os.path.isfile(os.path.join(src, x)), items))
            dirs = list(filter(lambda x: os.path.isdir(os.path.join(src, x)), items))
            print(files)
            print(dirs)
        
        # try:
        #     shutil.move(src, dst)
        # except shutil.Error as e:
        #     print(e)


class MoveSortByModificationDate(MoveStrategy):
    def move(src, dst):
        pass