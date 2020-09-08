import pandas as pd
from Controller import DataAssess, FileController
from Lexicon import NrcController, DepecheMoodController, WordNetAffectController, EmoSenticNetController

file_name = "dataset.csv"

# LOAD DATASET
df = pd.read_csv("03-post-nlp-"+file_name, sep=",", nrows=50)

DataAssess.run(df)

# RUN NRC SENTIMENT
df = NrcController.run(df)
df.drop(['anger', 'anger_score', 'anticipation', 'anticipation_score', 'disgust', 'disgust_score',
         'fear', 'fear_score', 'joy', 'joy_score', 'sadness', 'sadness_score',
         'surprise', 'surprise_score', 'trust', 'trust_score'], axis=1, inplace=True)

df = DepecheMoodController.run(df)
df.drop(['afraid', 'afraid_score', 'amused', 'amused_score', 'angry', 'angry_score',
         'annoyed', 'annoyed_score', 'dontcare', 'dontcare_score', 'happy', 'happy_score',
         'inspired', 'inspired_score', 'sad', 'sad_score'], axis=1, inplace=True)

# df = WordNetAffectController.run(df)

df = EmoSenticNetController.run(df)
df.drop(['anger', 'disgust', 'joy', 'sad', 'surprise', 'fear'], axis=1, inplace=True)

FileController.save_df_to_csv("04-post-sentiment-"+file_name, df)

