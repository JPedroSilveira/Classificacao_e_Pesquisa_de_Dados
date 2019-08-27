import os
from os.path import isfile, join


# Return a list with all folders in a path
#   path: str, the path to search
def get_folders(path: str) -> list:
    return [f for f in os.listdir(path) if not isfile(join(path, f))]


# Create a folder in the root path
#   name: str, the name of the new folder
def create_folder_on_root(name: str) -> str:
    return create_folder('./', name)


# Create a folder in a path
#   path: str, the path where the folder will be created
#   name: str, the name of the new folder
def create_folder(path: str, name: str) -> str:
    if name not in get_folders(path):
        try:
            os.mkdir(path + name)
        except OSError:
            print("Creation of the directory %s failed" % path)

    return path + name


# Generate a new number folder based in which exists
#   path: str, the main path to create this new folder
def get_new_test_folder(path: str) -> str:
    folders = get_folders(path)

    new_folder = len(folders) + 1

    return create_folder(path + '/', str(new_folder))


