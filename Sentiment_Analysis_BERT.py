import transformers
import pandas as pd
from Controller import PlutchikStandardController
from Controller.Bert import BertController
import random

# SETTING
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'

# LOAD DATASET
df = pd.read_csv("dataset/master/baseline-dataset_small.csv", sep=",")
df = df[["sentiment", "tweet_text"]]
df = df[(df["sentiment"] != "surprise") & (df["sentiment"] != "disgust")]


def compare_str(ori_str, to_str, to_code):
    if ori_str == to_str:
        return str(to_code)
    return ori_str


# CONVERT MOOD TO CODE
for mood_itm in PlutchikStandardController.moods_code:
    df["sentiment"] = df["sentiment"].apply(lambda x: compare_str(str(x), mood_itm[0], mood_itm[1]))

df = df.astype({"sentiment": int})
tokenizer = transformers.BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)

print("---MAIN--1-")
if __name__ == '__main__':
    print("---MAIN--2-")
    BertController.run(df, tokenizer)
