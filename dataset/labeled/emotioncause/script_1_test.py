import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt

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


fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(df.sentiment)
plt.xlabel("Number of tweets by score")
plt.xticks(rotation=50)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 9), textcoords='offset points')
plt.savefig("data_count.png")