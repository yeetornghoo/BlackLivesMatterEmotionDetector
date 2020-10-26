import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation, FileController, DataSpellingCorrection

'''
# LOAD DATA FROM DATASET
df = pd.read_csv("text_emotion.csv", sep=",", names=["tweet_id", "sentiment", "author", "content"])


## DROP USELESS ATTRIBUTES
df['tweet_text'] = df['content']
DataAssess.run(df)


df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)


# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)
'''

# SPELLING
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)


# REFACTOR COLUMNS NAME
df.drop(['content', 'author', 'tweet_id'], axis=1, inplace=True)
df.rename(columns={"sentiment": "ori_sentiment"}, inplace=True)


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


df['sentiment'] = df['ori_sentiment'].apply(lambda x: change_mood_name(str(x)))

df = df[['ori_sentiment', 'tweet_text', 'sentiment']]
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)
