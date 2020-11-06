import pandas as pd
from Controller import FileController, LogController
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection
'''
# LOAD AND PREPARE DATASET
anger_df = pd.read_csv("dataset/EI-reg/training/EI-reg-En-anger-train.txt", sep="\t")
anger_df["sentiment"] = "anger"

fear_df = pd.read_csv("dataset/EI-reg/training/EI-reg-En-fear-train.txt", sep="\t")
fear_df["sentiment"] = "fear"

joy_df = pd.read_csv("dataset/EI-reg/training/EI-reg-En-joy-train.txt", sep="\t")
joy_df["sentiment"] = "joy"

sadness_df = pd.read_csv("dataset/EI-reg/training/EI-reg-En-sadness-train.txt", sep="\t")
sadness_df["sentiment"] = "sadness"

frames = [anger_df, fear_df, joy_df, sadness_df]
df = pd.concat(frames)

df['tweet_text'] = df['Tweet']
df.rename(columns={"Tweet": "tweet", "Affect Dimension": "affect_dimension", "Intensity Score": "intensity_score"}, inplace=True)
#DataAssess.run(df)

# EXCLUDE NONE ENGLISH TEXT
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)
'''
# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)


# SPELLING CORRECTION
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)


LogController.log("Execution of 'script_1_process.py' is completed.")