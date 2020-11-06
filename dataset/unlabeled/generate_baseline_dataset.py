import pandas as pd
import os
import subprocess
from Controller import FileController, GitController, LogController, PlutchikStandardController
from Controller.Baseline import BaselineViz

# SETTING
dir_path = "C:/workspace/SocialMovementSentiment/dataset/unlabeled/"
label_dataset_folder = ["blm_davideantonio", "blm_baltimore", "blm_minnesota", "blm_washington"]

# LOOP DATASET
df = pd.DataFrame()
for folder_name in label_dataset_folder:

    folder_path = "{}{}/".format(dir_path, folder_name)
    os.chdir(folder_path)
    exec(open('script_0_init.py').read())

    # PROCESS INVIDIUAL DATASET
    dataset_file_path = "{}/baseline-dataset.csv".format(dir_path)
    ds_tmp = pd.read_csv(dataset_file_path, sep=",")
    ds_tmp = ds_tmp[["tweet_text", "sentiment", "sentiment_score"]]

    LogController.log("Added {} with {} rows".format(folder_name, len(ds_tmp.index)))
    df = df.append(ds_tmp, ignore_index=True)

df = df[["sentiment", "tweet_text"]]
FileController.save_df_to_csv("{}master/baseline-dataset.csv".format(dir_path), df)

'''
# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
df = pd.read_csv("{}master/baseline-dataset.csv".format(dir_path), sep=",")
out_path = "master/img/baseline/"
#BaselineViz.run_mood(df, out_path, 0.75)

#BaselineViz.df_summary(df, "fear", min_perc, out_path)
#BaselineViz.df_summary(df, "anger", min_perc, out_path)
#BaselineViz.df_summary(df, "sadness", min_perc, out_path)
#BaselineViz.df_summary(df, "joy", min_perc, out_path)


BaselineViz.df_summary(df, "anticipation", 0.0, out_path)
BaselineViz.df_summary(df, "disgust", 0.3, out_path)
BaselineViz.df_summary(df, "trust", 0.68, out_path)
BaselineViz.df_summary(df, "surprise", 0.0, out_path)
'''

# COMMIT TO GIT
GitController.commit("auto: update latest labeled datasets")

