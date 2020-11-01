import pandas as pd
from Controller import DataCleaning, DataNLP, DataAssess, DataTranslation, FileController, DataSpellingCorrection, \
    LogController

# LOAD AND PREPARE DATASET
df = pd.read_csv("dataset/smile-annotations-final.csv", sep=",", names=["tweet_id", "content", "sentiment"])
df['tweet_text'] = df['content']
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
df.drop(['content', 'tweet_id'], axis=1, inplace=True)
df.rename(columns={"sentiment": "ori_sentiment"}, inplace=True)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)


LogController.log("Execution of 'script_1_process.py' is completed.")