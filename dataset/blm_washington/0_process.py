import pandas as pd

from Controller import DataAssess, DataTranslation, FileController, DataCleaning, DataNLP


def process(file_name):
    # LOAD DATA FROM DATASET
    df = pd.read_csv(file_name, sep=";")

    # DROP USELESS ATTRIBUTES
    df.drop(['tweet_id', 'tweet_created_dt', 'retweets', 'favorites', 'permalink', 'to_person',
             'username', 'state', 'mentions', 'hashtags', 'geo', 'record_inserted_date',
             'radius', 'search_keyword'], axis=1, inplace=True)
    df['tweet_text'] = df['text']
    DataAssess.run(df)

    # DATA TRANSLATION (en,pt,es,ru,fr)
    df = DataTranslation.run(df, "en")
    FileController.save_df_to_csv("01-post-translate-"+file_name, df)

    # DATA CLEANING
    df = DataCleaning.run(df)
    FileController.save_df_to_csv("02-post-cleaning-"+file_name, df)

    # NLP TOKEN
    df = DataNLP.run(df)
    FileController.save_df_to_csv("03-post-nlp-"+file_name, df)


#process("dataset_p1.csv")
process("dataset_p2.csv")
process("dataset_p3.csv")
process("dataset_p4.csv")