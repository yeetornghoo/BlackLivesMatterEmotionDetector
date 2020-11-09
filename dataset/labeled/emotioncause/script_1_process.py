import pandas as pd
from Controller import FileController, LogController
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection, DataAssess


def replace_char(str_obj, fr_str, to_str):
    str_obj = str_obj.replace(fr_str, to_str)
    return str_obj


def extract_class_mood(str_obj):
    char_end_index = str_obj.index(">")
    return str_obj[1:char_end_index]


def process_class(df, class_mood):
    open_tag = "<{}>".format(class_mood)
    close_tag = "<\{}>".format(class_mood)
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_char(str(x), open_tag, ""))
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_char(str(x), close_tag, ""))
    return df


# LOAD AND PREPARE DATASET
df = pd.read_table("dataset/Emotion_Cause.txt", names=["tweet_text"])
df['sentiment'] = "NA"
df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_char(str(x), "<cause>", ""))
df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_char(str(x), "<\cause>", ""))
df['sentiment'] = df['tweet_text'].apply(lambda x: extract_class_mood(str(x)))
df = process_class(df, "happy")
df = process_class(df, "sad")
df = process_class(df, "disgust")
df = process_class(df, "anger")
df = process_class(df, "fear")
df = process_class(df, "shame")
#DataAssess.run(df)

# EXCLUDE NONE ENGLISH TEXT
DataAssess.run(df)
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)


# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)

# SPELLING CORRECTION
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)

LogController.log("Execution of 'script_1_process.py' is completed.")