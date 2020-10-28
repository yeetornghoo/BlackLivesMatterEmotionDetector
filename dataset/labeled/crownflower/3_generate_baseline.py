import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation, FileController, DataSpellingCorrection


# REFACTOR MOOD
def change_mood_name(ori_mood):

    p_mood = ori_mood

    if ori_mood == "worry":
        p_mood = "fear"
    elif ori_mood == "happiness":
        p_mood = "joy"
    elif ori_mood == "hate":
        p_mood = "disgust"

    return p_mood


# GENERATE BASELINE DATASET
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df.drop(['content', 'author', 'tweet_id'], axis=1, inplace=True)

# REFACTOR MOODS
df['sentiment'] = df['sentiment'].apply(lambda x: change_mood_name(str(x)))
df = df[['sentiment', 'tweet_text']]

# EXCLUDE UNWANTED MOOD
df = df.loc[(df['sentiment'] != "boredom")
            & (df['sentiment'] != "empty")
            & (df['sentiment'] != "enthusiasm")
            & (df['sentiment'] != "fun")
            & (df['sentiment'] != "love")
            & (df['sentiment'] != "neutral")
            & (df['sentiment'] != "relief")]

FileController.save_df_to_csv("baseline-dataset.csv", df)
