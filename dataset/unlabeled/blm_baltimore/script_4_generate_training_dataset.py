import pandas as pd
import seaborn as sns
from Controller.Baseline import BaselineViz
from Controller import GitController, PlutchikStandardController, FileController

# tweet_created_dt,retweets,favorites,tweet_text,sentiment,sentiment_count,sentiment_score

# SETTING
sns.set_theme(style="whitegrid")
df = pd.read_csv("05-post-sentiment-dataset.csv", sep=",")
out_path = "img/baseline/"

# FILTER WORD OF TWEET
df['ttl_tweet_text_word'] = df['tweet_text'].str.split().str.len()
df = df.loc[(df['ttl_tweet_text_word'] > 2)]
df = df[["tweet_text", "sentiment", "sentiment_score"]]
df = df[df['sentiment'].notna()]

# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
BaselineViz.run_mood(df, out_path, 0.0)

# SAVE FILE
df = df[["sentiment", "sentiment_score", "tweet_text"]]
FileController.save_df_to_csv("baseline-dataset.csv", df)
