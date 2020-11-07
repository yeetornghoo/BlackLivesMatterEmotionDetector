import pandas as pd
from Controller import FileController


# SETTING
dir_path = "C:/workspace/SocialMovementSentiment/dataset/"

# BASELINE DATASET
df = pd.DataFrame()
df = df.append(pd.read_csv(dir_path+"labeled/master/baseline-dataset.csv", sep=","))
df = df.append(pd.read_csv(dir_path+"unlabeled/master/baseline-dataset.csv", sep=","))

FileController.save_df_to_csv(dir_path+"master/baseline-dataset.csv", df)