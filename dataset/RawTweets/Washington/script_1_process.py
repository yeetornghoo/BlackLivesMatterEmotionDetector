import pandas as pd
from Controller import FileController, LogController
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection

# LOAD AND PREPARE DATASET
df = pd.read_csv("_dataset/dataset.csv", sep=";")
df['tweet_text'] = df['text']

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

# REMOVE USELESS COLUMN
#df = df[["tweet_created_dt", "tweet_text"]]
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)

# LOG
LogController.log("Execution of 'script_1_process.py' is completed.")