import pandas as pd
import subprocess
from Controller import FileController, GitController, LogController
from Controller.Baseline import BaselineViz

df = pd.DataFrame()
dir_path = "C:/workspace/SocialMovementSentiment/dataset/unlabeled/"
dataset = "baseline-dataset.csv"

# GENERATE BASELINE DATASET
# - MINNESOTA
ds_minnesota_file = "{}blm_minnesota/{}".format(dir_path, dataset)
ds_minnesota = pd.read_csv(ds_minnesota_file, sep=",")
ds_minnesota = ds_minnesota[["tweet_text", "sentiment", "sentiment_score"]]
LogController.log("Added {} rows".format(len(ds_minnesota.index)))
df = df.append(ds_minnesota, ignore_index=True)

'''
# - WASHINGTON DC
ds_washington_file = "{}blm_washington/{}".format(dir_path, dataset)
ds_washington = pd.read_csv(ds_washington_file, sep=",")
ds_washington = ds_washington[["tweet_text", "sentiment", "sentiment_score"]]
LogController.log("Added {} rows".format(len(ds_washington.index)))
df = df.append(ds_washington, ignore_index=True)

# - DAVID EANTONIE
ds_davideantonio_file = "{}blm_davideantonio/{}".format(dir_path, dataset)
ds_davideantonio = pd.read_csv(ds_davideantonio_file, sep=",")
ds_davideantonio = ds_davideantonio[["tweet_text", "sentiment", "sentiment_score"]]
LogController.log("Added {} rows".format(len(ds_davideantonio.index)))
df = df.append(ds_davideantonio, ignore_index=True)

# - BALTIMORE
ds_baltimore_file = "{}blm_baltimore/{}".format(dir_path, dataset)
ds_baltimore = pd.read_csv(ds_baltimore_file, sep=",")
ds_baltimore = ds_baltimore[["tweet_text", "sentiment", "sentiment_score"]]
LogController.log("Added {} rows".format(len(ds_baltimore.index)))
df = df.append(ds_baltimore, ignore_index=True)
'''

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

# COMMIT TO GIT
#GitController.commit("auto: update latest labeled datasets")
'''
