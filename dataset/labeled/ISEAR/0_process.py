import pandas as pd
from Controller import DataCleaning, DataNLP, DataAssess, DataTranslation, FileController, DataSpellingCorrection


'''
# LOAD DATA FROM DATASET
df = pd.read_csv("ISEAR.csv", sep=",", names=['ori_sentiment', 'text', 'other'])

# DROP USELESS ATTRIBUTES
df.drop(['other'], axis=1, inplace=True)
df['tweet_text'] = df['text']
DataAssess.run(df)

df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)


# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)


# SPELLING
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
df.drop(['text'], axis=1, inplace=True)
df['sentiment'] = df['ori_sentiment']
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)
'''

# FINAL DATASET
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df = df.loc[(df['sentiment'] != "guilt") & (df['sentiment'] != "guit") & (df['sentiment'] != "shame")]
FileController.save_df_to_csv("train-dataset.csv", df)
DataAssess.run(df)