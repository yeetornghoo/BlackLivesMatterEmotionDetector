import pandas as pd
from Controller import DataCleaning, DataNLP, DataAssess, DataTranslation, FileController, DataSpellingCorrection

'''
file_name = "text_emotion.csv"

# LOAD DATA FROM DATASET
df = pd.read_csv(file_name, sep=",", names=["tweet_id", "sentiment", "author", "content"])

## DROP USELESS ATTRIBUTES
df['tweet_text'] = df['content']
DataAssess.run(df)

df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)
'''

# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)

# SPELLING
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
df.drop(['content', 'author', 'tweet_id'], axis=1, inplace=True)
df.rename(columns={"sentiment": "ori_sentiment"}, inplace=True)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)

'''
# NLP TOKEN
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df = DataNLP.run(df)
FileController.save_df_to_csv("03-post-nlp-"+file_name, df)
'''