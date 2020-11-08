import os

import pandas as pd
from Controller import FileController

dir_path = "C:/workspace/SocialMovementSentiment/dataset/"


# PROCESS LABELED DATA
os.chdir("C:/workspace/SocialMovementSentiment/dataset/labeled")
exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
os.chdir("C:/workspace/SocialMovementSentiment/dataset/unlabeled")
exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
os.chdir("C:/workspace/SocialMovementSentiment/dataset/master")
exec(open('script_1_create_and_validate_baseline_dataset.py').read())