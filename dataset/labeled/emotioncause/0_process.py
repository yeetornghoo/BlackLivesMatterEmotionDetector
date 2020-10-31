import pandas as pd


def replace_char(str_obj, fr_str, to_str):
    str_obj = str_obj.replace(fr_str, to_str)
    return str_obj


def remove_cause(str_obj):
    str_obj = replace_char(str_obj, "<cause>", "")
    str_obj = replace_char(str_obj, "<\cause>", "")
    return str_obj


def process_happy_tweet(df):
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_char(str(x), "<happy>", ""))
    return df

# LOAD DATA FROM DATASET
df = pd.read_table("Dataset/Emotion_Cause.txt", names=["tweet_text"])
df['tweet_text'] = df['tweet_text'].apply(lambda x: remove_cause(str(x)))

df = process_happy_tweet(df)

print(df['tweet_text'])


#DataAssess.run(df)


'''
# DROP USELESS ATTRIBUTES
df['tweet_text'] = df['Tweet']
df.drop(['ID'], axis=1, inplace=True)
df.rename(columns={"Tweet": "tweet", "Affect Dimension": "affect_dimension",
                   "Intensity Score": "intensity_score", "sentiment": "ori_sentiment"}, inplace=True)
DataAssess.run(df)

df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)

# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)


# SPELLING
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
df.drop(['tweet', 'affect_dimension', 'intensity_score'], axis=1, inplace=True)
df['sentiment'] = df['ori_sentiment']
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)
'''