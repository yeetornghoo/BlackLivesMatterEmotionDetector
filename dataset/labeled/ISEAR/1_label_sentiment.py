import pandas as pd
from Controller import FileController, DataAssess, DataNLP
from Lexicon.DepecheMood import DepecheMoodController
from Lexicon.EmoSenticNet import EmoSenticNetController
from Lexicon.NRC import NrcController

# NLP TOKEN
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df = DataNLP.run(df)
FileController.save_df_to_csv("test-1-post-nlp-dataset.csv", df)


# CHECK SENTIMENT
df = pd.read_csv("test-1-post-nlp-dataset.csv", sep=",")
df = NrcController.run(df)
df = DepecheMoodController.run(df)
df = EmoSenticNetController.run(df)
FileController.save_df_to_csv("test-2-post-sentiment-dataset.csv", df)
