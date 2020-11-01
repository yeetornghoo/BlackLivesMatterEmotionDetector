import pandas as pd
from Controller import DataCleaning, DataNLP, DataAssess, DataTranslation, FileController, DataSpellingCorrection, \
    LogController

# LOAD AND PREPARE DATASET
df = pd.read_csv("dataset/ISEAR.csv", sep=",", names=['ori_sentiment', 'text', 'other'])
df.drop(['other'], axis=1, inplace=True)
df['tweet_text'] = df['text']
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
df.drop(['text'], axis=1, inplace=True)
df['sentiment'] = df['ori_sentiment']
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)


LogController.log("Execution of 'script_1_process.py' is completed.")