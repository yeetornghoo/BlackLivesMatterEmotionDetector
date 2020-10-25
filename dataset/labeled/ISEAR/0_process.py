import pandas as pd
from Controller import DataCleaning, DataNLP, DataAssess, DataTranslation, FileController, DataSpellingCorrection

file_name = "ISEAR.csv"

# LOAD DATA FROM DATASET
df = pd.read_csv(file_name, sep=",", names=['ori_sentiment', 'text', 'other'])

# DROP USELESS ATTRIBUTES
df.drop(['other'], axis=1, inplace=True)
df['tweet_text'] = df['text']
DataAssess.run(df)

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

FileController.save_df_to_csv("03-post-nlp-"+file_name, df)
'''