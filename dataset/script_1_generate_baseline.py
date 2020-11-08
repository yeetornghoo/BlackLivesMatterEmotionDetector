import os

import pandas as pd
from Controller import FileController

<<<<<<< HEAD
parent_path = "C:/workspace/SocialMovementSentiment/dataset/"
=======
main_path = "C:/workspace/SocialMovementSentiment/dataset/"
>>>>>>> 62e059ce96e40d6e6bfd67529b337baf2b6733bb


# PROCESS LABELED DATA
os.chdir("{}labeled".format(parent_path))
exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
<<<<<<< HEAD
os.chdir("{}unlabeled".format(parent_path))
=======
os.chdir("../")
os.chdir("C:/workspace/SocialMovementSentiment/dataset/unlabeled")
>>>>>>> 62e059ce96e40d6e6bfd67529b337baf2b6733bb
exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
os.chdir("{}master".format(parent_path))
#exec(open('script_1_create_and_validate_baseline_dataset.py').read())