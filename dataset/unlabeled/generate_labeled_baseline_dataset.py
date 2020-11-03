import pandas as pd
import subprocess
from Controller import FileController
from Controller.Baseline import BaselineViz

df = pd.DataFrame()
dir_path = "C:/workspace/SocialMovementSentiment/dataset/unlabeled/"

# GENERATE BASELINE DATASET

# COMBINE FINAL BASELINE DATASET
ds_minnesota_file = "{}/blm_minnesota/05-post-sentiment-dataset.csv".format(dir_path)
ds_minnesota = pd.read_csv(ds_minnesota_file, sep=",")
ds_minnesota = ds_minnesota[["tweet_text", "nrc_sentiment", "nrc_sentiment_score"]]
ds_washington_file = "{}/blm_washington/04-post-sentiment-False-dataset.csv".format(dir_path)
ds_washington = pd.read_csv(ds_washington_file, sep=",")
ds_washington = ds_washington[["tweet_text", "nrc_sentiment", "nrc_sentiment_score"]]
df = pd.concat([ds_minnesota, ds_washington], axis=0)
df.rename(columns={"nrc_sentiment": "sentiment", "nrc_sentiment_score": "sentiment_score"}, inplace=True)
FileController.save_df_to_csv("{}master/baseline-dataset.csv".format(dir_path), df)


# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
df = pd.read_csv("{}master/baseline-dataset.csv".format(dir_path), sep=",")
out_path = "master/img/baseline/"
BaselineViz.run_mood(df, out_path, 0.75)


# UPLOAD TO GITHUB
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "AUTO: UPDATE LATEST UNLABELED BASELINE DATASET"])
subprocess.call(["git", "push"])
