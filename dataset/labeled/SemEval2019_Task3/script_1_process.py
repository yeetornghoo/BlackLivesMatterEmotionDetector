import pandas as pd
from Controller import FileController, LogController
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection, DataAssess, DataNLP
from Controller import BaselineVizController, PlutchikStandardController

# LOAD AND PREPARE DATASET
df = pd.read_csv("dataset/train.txt", sep='\t', lineterminator='\r')
df["tweet_text"] = df["turn1"] + " " + df["turn2"] + " " + df["turn3"]
df.drop(['id', 'turn1', 'turn2', 'turn3'], axis=1, inplace=True)
DataAssess.run(df)

# EXCLUDE NONE ENGLISH TEXT
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)


# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)

# SPELLING CORRECTION
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
df.rename(columns={"label": "sentiment"}, inplace=True)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)


# LOG
LogController.log("Execution of 'script_1_process.py' is completed.")