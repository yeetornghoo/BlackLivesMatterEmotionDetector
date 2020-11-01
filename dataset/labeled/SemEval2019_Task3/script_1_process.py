import pandas as pd
from Controller import DataCleaning, DataAssess, FileController, DataNLP, DataTranslation, DataSpellingCorrection, \
    LogController

# LOAD AND PREPARE DATASET
df = pd.read_csv("dataset/train.txt", sep='\t', lineterminator='\r')
df["tweet_text"] = df["turn1"] + " " + df["turn2"] + " " + df["turn3"]
df.drop(['id', 'turn1', 'turn2', 'turn3'], axis=1, inplace=True)


# EXCLUDE NONE ENGLISH TEXT
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)


# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)


# SPELLING CORRECTION
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
df.rename(columns={"label": "ori_sentiment"}, inplace=True)


# REFACTOR MOOD
def change_mood_name(ori_mood):

    p_mood = ori_mood

    if ori_mood == "sad":
        p_mood = "sadness"
    elif ori_mood == "happy":
        p_mood = "joy"

    return p_mood


df['sentiment'] = df['ori_sentiment'].apply(lambda x: change_mood_name(str(x)))
df = df[['ori_sentiment', 'tweet_text', 'sentiment']]
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)


LogController.log("Execution of 'script_1_process.py' is completed.")