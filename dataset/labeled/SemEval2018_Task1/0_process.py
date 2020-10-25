import pandas as pd
from Controller import DataCleaning, DataAssess, FileController, DataNLP, DataTranslation

# LOAD DATA FROM DATASET
anger_df = pd.read_csv("EI-reg/training/EI-reg-En-anger-train.txt", sep="\t")
anger_df["sentiment"] = "anger"

fear_df = pd.read_csv("EI-reg/training/EI-reg-En-fear-train.txt", sep="\t")
fear_df["sentiment"] = "fear"

joy_df = pd.read_csv("EI-reg/training/EI-reg-En-joy-train.txt", sep="\t")
joy_df["sentiment"] = "joy"

sadness_df = pd.read_csv("EI-reg/training/EI-reg-En-sadness-train.txt", sep="\t")
sadness_df["sentiment"] = "sadness"

frames = [anger_df, fear_df, joy_df, sadness_df]
df = pd.concat(frames)
DataAssess.run(df)

# DROP USELESS ATTRIBUTES
df['tweet_text'] = df['Tweet']
df.drop(['ID'], axis=1, inplace=True)
df.rename(columns={"Tweet": "tweet", "Affect Dimension": "affect_dimension",
                   "Intensity Score": "intensity_score", "sentiment": "ori_sentiment"}, inplace=True)
DataAssess.run(df)

# DATA TRANSLATION
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)

# DATA CLEANING
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)

'''
# NLP TOKEN
df = DataNLP.run(df)
FileController.save_df_to_csv("03-post-nlp-dataset.csv", df)
'''