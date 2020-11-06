import os
import pandas as pd
from Controller import FileController
from Controller import GitController
from Controller.Baseline import BaselineViz

dir_path = "C:/workspace/SocialMovementSentiment/dataset/labeled/"

label_dataset_folder = ["crownflower", "emotioncause", "ISEAR", "SemEval2018_Task1", "SemEval2019_Task3", "smile_twitter"]

# GENERATE BASELINE DATASET
for folder_name in label_dataset_folder:
    folder_path = "{}{}/".format(dir_path, folder_name)
    os.chdir(folder_path)
    exec(open('script_0_init.py').read())

# COMBINE FINAL BASELINE DATASET
df = pd.DataFrame()
for folder_name in label_dataset_folder:
    baseline_ds_path = "{}{}/baseline-dataset.csv".format(dir_path, folder_name)
    df_tmp = pd.read_csv(baseline_ds_path, sep=",")
    df = df.append(df_tmp, ignore_index=True)
FileController.save_df_to_csv("master/baseline-dataset.csv", df)

'''
# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
df = pd.read_csv("{}master/baseline-dataset.csv".format(dir_path), sep=",")
out_path = "master/img/baseline/"
BaselineViz.run(df, out_path)
'''

# COMMIT TO GIT
GitController.commit("auto: update latest labeled datasets")
