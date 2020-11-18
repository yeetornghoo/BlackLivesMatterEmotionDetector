import transformers
import pandas as pd
from Controller import PlutchikStandardController
from Controller.Bert import BertController
import random

# SETTING
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'


def compare_str(ori_str, to_str, to_code):
    if ori_str == to_str:
        return str(to_code)
    return ori_str


def convert_mood_class(idf):
    # CONVERT MOOD TO CODE
    for mood_itm in PlutchikStandardController.moods_code:
        idf["sentiment"] = idf["sentiment"].apply(lambda x: compare_str(str(x), mood_itm[0], mood_itm[1]))

    idf = idf.astype({"sentiment": int})
    return idf


if __name__ == '__main__':
    # LOAD DATASET
    df = pd.read_csv("dataset/master/baseline-dataset.csv", sep=",", nrows=1000)
    df = df[["sentiment", "tweet_text"]]
    df = df[(df["sentiment"] != "surprise") & (df["sentiment"] != "disgust")]

    # CONVERT CLASS TO INTEGER
    df = convert_mood_class(df)

    # CREATE TOKEN
    tokenizer = transformers.BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)

    BertController.run(df, tokenizer)
