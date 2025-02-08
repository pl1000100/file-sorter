import os
import time

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def move(func, src, dst, verbose=False):
        pass


class NoSort(Strategy):
    def move(self, func, src, dst, verbose=False):
        if os.path.isfile(src):
            if verbose:
                print(f"Moving {os.path.basename(src)} to {dst}")
            func(src, os.path.join(dst, os.path.basename(src)))
            return
        for i in os.listdir(src):
            if verbose:
                print(f"Moving {i} to {dst}")
            func(os.path.join(src, i), os.path.join(dst, i))
        # try:
        #     for i in os.listdir(src):
        #         func(os.path.join(src, i), dst)
        # except shutil.Error as e:
        #     print(e)


class SortByExtension(Strategy):
    def move(self, func, src, dst, verbose=False):
        if os.path.isfile(src):
            name_split = os.path.splitext(src)
            if name_split[1] != None:
                if verbose:
                    print(f"Moving {os.path.basename(src)} to {dst}/{name_split[1][1:]}")
                func(src, os.path.join(dst + f"/{name_split[1][1:]}", os.path.basename(src)))
                return
            if verbose:
                print(f"Moving {os.path.basename(src)} to {dst}")
            func(src, os.path.join(dst, os.path.basename(src)))
            return
        for i in os.listdir(src):
            name_split = os.path.splitext(i)
            if name_split[1] != None:
                if verbose:
                    print(f"Moving {i} to {dst}/{name_split[1][1:]}")
                func(os.path.join(src, i), dst + f"/{name_split[1][1:]}")
                continue
            func(os.path.join(src, i), dst)
        

class SortByModificationDate(Strategy):
    def move(self, func, src, dst, verbose=False):
        def _get_modification_date(file_path):
            mod_time = os.path.getmtime(file_path)
            return time.strftime('%Y-%m-%d', time.localtime(mod_time))

        if os.path.isfile(src):
            if verbose:
                print(f"Moving {os.path.basename(src)} to {dst + f'/{_get_modification_date(src)}'}")
            func(src, dst + f"/{_get_modification_date(src)}")
            return
        for item in os.listdir(src):
            if verbose:
                print(f"Moving {item} to {dst}")
            func(src + f"/{item}", dst + f"/{_get_modification_date(src + f'/{item}')}")