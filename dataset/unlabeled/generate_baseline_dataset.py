import pandas as pd
import os
from Controller import FileController, LogController
from Controller.Baseline import BaselineViz

# SETTING
dir_path = "C:/workspace/SocialMovementSentiment/dataset/unlabeled/"
label_dataset_folder = ["blm_baltimore", "blm_davideantonio", "blm_minnesota", "blm_washington"]
mood_perc = [["fear", 0.78], ["anger", 1], ["sadness", 1], ["trust", 0.68],
             ["joy", 0.90], ["surprise", 0.0], ["anticipation", 0.0], ["disgust", 0.0]]
out_path = "master/img/baseline/"


# FILTER DATA BY PERCENTAGE
def filter_data_by_perc(df_input):

    df_out = pd.DataFrame()
    for mood, perc in mood_perc:
        df_tmp = BaselineViz.df_summary(df_input, mood, perc, out_path)
        df_out = df_out.append(df_tmp)
    return df_out


# LOOP DATASET
df = pd.DataFrame()
for folder_name in label_dataset_folder:

    folder_path = "{}{}/".format(dir_path, folder_name)
    os.chdir(folder_path)
    exec(open('script_0_init.py').read())

    # PROCESS INVIDIUAL DATASET
    dataset_file_path = "{}/baseline-dataset.csv".format(folder_path)
    ds_tmp = pd.read_csv(dataset_file_path, sep=",")
    ds_tmp = ds_tmp[["sentiment", "sentiment_score", "tweet_text"]]

    LogController.log("Added {} with {} rows".format(folder_name, len(ds_tmp.index)))
    df = df.append(ds_tmp, ignore_index=True)

df = filter_data_by_perc(df)
BaselineViz.run(df, out_path)
FileController.save_df_to_csv("{}master/baseline-dataset.csv".format(dir_path), df)
