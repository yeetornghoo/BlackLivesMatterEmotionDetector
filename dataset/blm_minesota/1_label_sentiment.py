import pandas as pd

from Lexicon.DepecheMood import DepecheMoodController
from Lexicon.NRC import NrcController

file_name = "dataset.csv"
is_standard_model = True
# LOAD DATASET
df = pd.read_csv("03-post-nlp-"+file_name, sep=",")
'''
DataAssess.run(df)
'''

# RUN NRC SENTIMENT
df = NrcController.run(df, is_standard_model)


# RUN DEPECHEMOOD SENTIMENT
df = DepecheMoodController.run(df, is_standard_model)
print(df.columns)
'''
# df = WordNetAffectController.run(df)

# df = EmoSenticNetController.run(df)
# df.drop(['anger', 'disgust', 'joy', 'sad', 'surprise', 'fear'], axis=1, inplace=True)

FileController.save_df_to_csv("04-post-sentiment-"+file_name, df)
'''
