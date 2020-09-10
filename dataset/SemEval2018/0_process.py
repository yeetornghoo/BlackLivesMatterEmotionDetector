import pandas as pd
from Controller import DataCleaning, DataAssess, FileController, DataNLP

file_name = "2018-E-c-En-test-gold.txt"

# LOAD DATA FROM DATASET
df = pd.read_csv(file_name, sep="\t")

DataAssess.run(df)

# DROP USELESS ATTRIBUTES
df.drop(['ID'], axis=1, inplace=True)
df['tweet_text'] = df['Tweet']

'''
# DATA TRANSLATION (en,pt,es,ru,fr)
#df = DataTranslation.run(df, "en")
#FileController.save_df_to_csv("01-post-translate-dataset.csv", df)
'''

# DATA CLEANING
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)

# NLP TOKEN
df = DataNLP.run(df)
FileController.save_df_to_csv("03-post-nlp-dataset.csv", df)