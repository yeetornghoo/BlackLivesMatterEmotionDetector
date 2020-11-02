import os
import pandas as pd
import subprocess

from Controller import FileController, DataCleaning, DataSpellingCorrection

dir_path = "C:/workspace/SocialMovementSentiment/dataset/labeled/"

label_dataset_folder = ["crownflower", "emotioncause", "ISEAR",
                        "SemEval2018_Task1", "SemEval2019_Task3",
                        "smile_twitter"]

'''
# PROCESS DATASET
for folder_name in label_dataset_folder:
    folder_path = "{}{}/".format(dir_path, folder_name)
    os.chdir(folder_path)
    exec(open('script_0_init.py').read())
'''

# COMBINE FINAL BASELINE DATASET
df = pd.DataFrame()
for folder_name in label_dataset_folder:
    baseline_ds_path = "{}{}/baseline-dataset.csv".format(dir_path, folder_name)
    df_tmp = pd.read_csv(baseline_ds_path, sep=",")
    df = df.append(df_tmp, ignore_index=True)

FileController.save_df_to_csv("baseline-dataset.csv", df)

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "'AUTO: UPDATE LATEST UNLABELED BASELINE DATASET'"])
subprocess.call(["git", "push"])
