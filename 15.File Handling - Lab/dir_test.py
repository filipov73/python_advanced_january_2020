from os import listdir
from os.path import isdir, isfile, join


def print_all_dirs_files(path):
    dirs_files = [join(path, content) for content in listdir(path)]
    [print(x) for x in dirs_files]
    [print_all_dirs_files(dir_) for dir_ in dirs_files if isdir(dir_)]


path = "dir_1"
print_all_dirs_files(path)
