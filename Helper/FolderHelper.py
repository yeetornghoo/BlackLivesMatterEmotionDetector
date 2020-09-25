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


def reset_dataset_viz_output_folder(dir_path, lexicon_name, plot_name):

    # MAIN FOLDER (CREATE IF NOT EXIST)
    standard_fdr = "{}img/standard".format(dir_path)
    individual_fdr = "{}img/individual".format(dir_path)
    create_folder(standard_fdr)
    create_folder(individual_fdr)

    # LEXICON FOLDER (RESET)
    standard_fdr = standard_fdr + "/{}".format(lexicon_name)
    individual_fdr = individual_fdr + "/{}".format(lexicon_name)
    create_folder(standard_fdr)
    create_folder(individual_fdr)

    # LEXICON FOLDER (RESET)
    standard_fdr = standard_fdr + "/{}".format(plot_name)
    individual_fdr = individual_fdr + "/{}".format(plot_name)
    reset_folder(standard_fdr)
    reset_folder(individual_fdr)