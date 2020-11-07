import os

import pandas as pd
from Controller import FileController

dir_path = "C:/workspace/SocialMovementSentiment/dataset/"


# PROCESS LABELED DATA
os.chdir("{}/labeled".format(dir_path))
exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
os.chdir("{}/unlabeled".format(dir_path))
exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
os.chdir("{}/master".format(dir_path))
exec(open('script_1_create_and_validate_baseline_dataset.py').read())