import pandas as pd

from Controller import FileController, DataAssess
from Lexicon.DepecheMood import DepecheMoodController
from Lexicon.EmoSenticNet import EmoSenticNetController
from Lexicon.NRC import NrcController

file_name = "text_emotion.csv"
is_standard_model = False
# LOAD DATASET
df = pd.read_csv("03-post-nlp-"+file_name, sep=",")

DataAssess.run(df)

# RUN NRC SENTIMENT
df = NrcController.run(df, is_standard_model)

# RUN DEPECHEMOOD SENTIMENT
df = DepecheMoodController.run(df, is_standard_model)

# RUN ECO SENTIC NET
df = EmoSenticNetController.run(df)

FileController.save_df_to_csv("04-post-sentiment-{}-{}".format(is_standard_model, file_name), df)
