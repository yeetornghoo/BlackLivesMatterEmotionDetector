import pandas as pd
from Controller import FileController
from Controller.Validation import PreliminaryValidation

# SETTING
dir_path = "C:/workspace/SocialMovementSentiment/dataset/"
# BASELINE DATASET

labeled_df = pd.read_csv(dir_path+"labeled/master/baseline-dataset.csv", sep=",")
print(labeled_df.groupby("sentiment").count())

unlabeled_df = pd.read_csv(dir_path+"unlabeled/master/baseline-dataset.csv", sep=",")
print(unlabeled_df.groupby("sentiment").count())

frames = [labeled_df, unlabeled_df]
df = pd.concat(frames)
df = df[["sentiment", "tweet_text"]]

print(df.groupby("sentiment").count())
FileController.save_df_to_csv(dir_path+"master/baseline-dataset.csv", df)

# VALIDATE BY MACHINE LEARNING
PreliminaryValidation.run(df, dir_path + "master")
