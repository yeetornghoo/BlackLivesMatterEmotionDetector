import pandas as pd

from Controller import FileController
from Lexicon.DepecheMood import DepecheMoodController
from Lexicon.EmoSenticNet import EmoSenticNetController
from Lexicon.NRC import NrcController


is_standard_model = False


def process(file_name):

    # LOAD DATASET
    df = pd.read_csv(file_name, sep=",")

    # RUN NRC SENTIMENT
    df = NrcController.run(df, is_standard_model)

    # RUN DEPECHEMOOD SENTIMENT
    df = DepecheMoodController.run(df, is_standard_model)

    # RUN ECO SENTIC NET
    df = EmoSenticNetController.run(df)


    FileController.save_df_to_csv("04-post-sentiment-False-{}".format(is_standard_model, file_name), df)


process("03-post-nlp-dataset_p1.csv")
process("03-post-nlp-dataset_p2.csv")
process("03-post-nlp-dataset_p3.csv")
process("03-post-nlp-dataset_p4.csv")