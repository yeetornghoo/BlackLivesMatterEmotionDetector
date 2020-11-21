import pandas as pd
from Controller import FileController
from Controller.Validation import PreliminaryValidation

# SETTING
dir_path = "C:/workspace/SocialMovementSentiment/dataset/labeled/master/"

# BASELINE DATASET
df = pd.read_csv(dir_path+"baseline-dataset.csv", sep=",")
df = df[["sentiment", "tweet_text"]]

print(df.groupby("sentiment").count())

# VALIDATE BY MACHINE LEARNING
PreliminaryValidation.run(df, dir_path)
