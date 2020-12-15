import pandas as pd
from Controller import FileController, LogController, DataAssess
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection
'''
# LOAD AND PREPARE DATASET
colnames=['id', 'tweet_text', 'sentiment', 'sentiment_score']
anger_df = pd.read_csv("dataset/anger-all.txt", sep="\t", names=colnames, header=None)
fear_df = pd.read_csv("dataset/fear-all.txt", sep="\t", names=colnames, header=None)
joy_df = pd.read_csv("dataset/joy-all.txt", sep="\t", names=colnames, header=None)
sadness_df = pd.read_csv("dataset/sadness-all.txt", sep="\t", names=colnames, header=None)

frames = [anger_df, fear_df, joy_df, sadness_df]
df = pd.concat(frames)
DataAssess.run(df)

# EXCLUDE NONE ENGLISH TEXT
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)

'''
# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)

# SPELLING CORRECTION
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)

LogController.log("Execution of 'script_1_process.py' is completed.")
