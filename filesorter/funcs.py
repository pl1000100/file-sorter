import os
import shutil



def move_func(src, dst):
    # if not os.path.exists(dst):
    #     os.makedirs(dst)
    # if os.path.exists(dst):
    #     for item in os.listdir(src):
    #         shutil.move(src + f"/{item}", dst)
    #     return
    shutil.move(src, dst)