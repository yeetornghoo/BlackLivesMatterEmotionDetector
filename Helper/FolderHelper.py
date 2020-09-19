import shutil
import os
from Controller import LogController
import os.path
from os import path


def reset_folder(dir_path):
    delete_folder(dir_path)
    create_folder(dir_path)


def create_folder(dir_path):

    try:
        if not path.isdir(dir_path):
            os.makedirs(dir_path)
    except OSError as error:
        print("There was an error.")
    finally:
        LogController.log("folder '{}' is created".format(dir_path))


def delete_folder(dir_path):

    try:
        if path.isdir(dir_path):
            shutil.rmtree(dir_path)
    except OSError as error:
        print("There was an error.")
    finally:
        LogController.log("folder '{}' is deleted".format(dir_path))