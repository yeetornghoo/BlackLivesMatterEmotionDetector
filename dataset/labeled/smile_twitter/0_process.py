import pandas as pd
from Controller import DataCleaning, DataNLP, DataAssess, DataTranslation, FileController
sub_dir="3187909/"
file_name = "smile-annotations-final.csv"

# LOAD DATA FROM DATASET
df = pd.read_csv(sub_dir+file_name, sep=",", names=["tweet_id", "content", "sentiment"])


## DROP USELESS ATTRIBUTES
df['tweet_text'] = df['content']
DataAssess.run(df)

# DATA TRANSLATION (en,pt,es,ru,fr)
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-"+file_name, df)

# DATA CLEANING
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-"+file_name, df)

'''
# NLP TOKEN
df = DataNLP.run(df)
FileController.save_df_to_csv("03-post-nlp-"+file_name, df)
'''