import os
import pandas as pd
from Controller import FileController

parent_path = "C:/workspace/SocialMovementSentiment/dataset/"

# PROCESS LABELED DATA

os.chdir("{}labeled".format(parent_path))
exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
#os.chdir("{}unlabeled".format(parent_path))
#exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
#os.chdir("{}labeled".format(parent_path))
#exec(open('generate_baseline_dataset.py').read())
