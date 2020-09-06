import pandas as pd
from Controller import DataCleaning, DataNLP, DataAssess, DataTranslation, FileController
i_file_name = "blm_minesota_summary.csv"

# LOAD DATA FROM DATASET
df = pd.read_csv("dataset/"+i_file_name, sep=";")

# DROP USELESS ATTRIBUTES
df.drop(['permalink', 'to_person', 'username', 'state', 'mentions', 'hashtags', 'geo',
         'record_inserted_date', 'radius', 'search_keyword'], axis=1, inplace=True)
df['tweet_text'] = df['text']
# DataAssess.run(df)

# DATA TRANSLATION (en,pt,es,ru,fr)
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-"+i_file_name, df)
# DataAssess.run(df)


# DATA CLEANING
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-"+i_file_name, df)
# DataAssess.run(df)

# NLP TOKEN
df = DataNLP.run(df)
FileController.save_df_to_csv("03-"+i_file_name, df)
# DataAssess.run(df)