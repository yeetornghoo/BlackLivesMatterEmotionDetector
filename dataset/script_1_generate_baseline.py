import os
import pandas as pd
from Controller import FileController

main_path = "C:/workspace/SocialMovementSentiment/dataset/"

# PROCESS LABELED DATA
os.chdir("{}labeled".format(main_path))
exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
#os.chdir("{}unlabeled".format(main_path))
#exec(open('generate_baseline_dataset.py').read())

# PROCESS LABELED DATA
#os.chdir("{}master".format(main_path))
#exec(open('script_1_create_and_validate_baseline_dataset.py').read())