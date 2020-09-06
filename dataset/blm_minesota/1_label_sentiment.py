import pandas as pd
from Controller import DataAssess, FileController
from Lexicon import NrcController

file_name = "dataset.csv"

# LOAD DATASET
df = pd.read_csv("03-post-nlp-"+file_name, sep=",")
DataAssess.run(df)


# RUN NRC SENTIMENT
NrcController.run(df)

df.drop(['Unnamed: 0', 'tweet_langague'], axis=1, inplace=True)

FileController.save_df_to_csv("04-post-nrc-"+file_name, df)