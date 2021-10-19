import argparse
import os

# Comments for review:
# - File name:
#   - I thought it was big enough to separate from utils.py
#   - I tried directory-utils.py - but the hyphen meant I could  not import it
#   - And an underscore in directory_utils.py was inconsistent with existing filenames


pushstack = list()


def pushdir(dirname: str):
    global pushstack
    pushstack.append(os.getcwd())
    os.chdir(dirname)


def popdir():
    global pushstack
    os.chdir(pushstack.pop())


def use_directory(dir, create_if_missing):
    class PushPopDirectory:
        def __init__(self, dir):
            self.dir = dir

        def __enter__(self):
            pushdir(dir)

        def __exit__(self, exc_type, exc_val, exc_tb):
            popdir()

    if create_if_missing:
        os.makedirs(dir, exist_ok=True)
    return PushPopDirectory(dir)


# From https://stackoverflow.com/q/11415570/104370
def readable_dir(prospective_dir):
    if not os.path.isdir(prospective_dir):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(prospective_dir))
    if os.access(prospective_dir, os.R_OK):
        return prospective_dir
    else:
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(prospective_dir))
