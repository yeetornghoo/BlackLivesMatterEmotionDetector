import pandas as pd
from Controller import FileController, DataAssess, DataNLP, DataCleaning, DataSpellingCorrection

# NLP TOKEN
df = pd.read_csv("baseline-dataset.csv", sep=",")


# DATA CLEANING
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)


# SPELLING
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)


# NLP
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df = DataNLP.run(df)
df.drop(['tweet_text'], axis=1, inplace=True)
df.rename(columns={"final_tweet_text": "tweet_text"}, inplace=True)
FileController.save_df_to_csv("test-1-post-nlp-dataset.csv", df)
