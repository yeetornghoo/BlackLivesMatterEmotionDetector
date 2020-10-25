import pandas as pd
from Controller import DataCleaning, DataAssess, FileController, DataNLP, DataTranslation, DataSpellingCorrection

# LOAD DATA FROM DATASET
df = pd.read_csv("train.txt", sep='\t', lineterminator='\r')
df["tweet_text"] = df["turn1"] + " " + df["turn2"] + " " + df["turn3"]
df.drop(['id', 'turn1', 'turn2', 'turn3'], axis=1, inplace=True)

df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)

# DATA CLEANING
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)

# SPELLING
df = DataSpellingCorrection.run(df)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)

'''
# NLP TOKEN
df = DataNLP.run(df)
FileController.save_df_to_csv("03-post-nlp-dataset.csv", df)
'''