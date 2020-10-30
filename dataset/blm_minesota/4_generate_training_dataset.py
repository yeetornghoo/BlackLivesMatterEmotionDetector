import pandas as pd
from Controller import FileController, DataAssess, DataNLP
from Lexicon.DepecheMood import DepecheMoodController
from Lexicon.EmoSenticNet import EmoSenticNetController
from Lexicon.NRC import NrcController

# LOAD LABELED DATASET
df = pd.read_csv("04-post-sentiment-False-dataset.csv", sep=",")

print (df)