import pandas as pd
import seaborn as sns
from Controller.Baseline import BaselineViz
from Controller import GitController, FileController, DataCleaning, PlutchikStandardController

# SETTING
from Controller.Visualization import BarPlotViz

sns.set_theme(style="whitegrid")
df = pd.read_csv("05-post-sentiment-dataset.csv", sep=",")
out_path = "img/baseline/"

# FILTER WORD OF TWEET
df['ttl_tweet_text_word'] = df['tweet_text'].str.split().str.len()
df = df.loc[(df['ttl_tweet_text_word'] > 2)]
df = df[['sentiment', 'sentiment_count', 'sentiment_score', "tweet_text"]]
df = df[df['sentiment'].notna()]

print(df.groupby("sentiment").count())
df.drop_duplicates(inplace=True)
print(df.groupby("sentiment").count())

# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
BaselineViz.run_mood(df, out_path, 0.0)

# SAVE FILE
df = df[["sentiment", "sentiment_score", "tweet_text"]]
FileController.save_df_to_csv("baseline-dataset.csv", df)

# TWEET COUNT
dir_path = "C:/workspace/SocialMovementSentiment/dataset/unlabeled/blm_washington/"
img_path = dir_path+"img/final_tweet_count.png"
df_count = df.loc[:, ['sentiment', 'tweet_text']]
df_count = df_count.groupby("sentiment").count()
BarPlotViz.generate_barplot(df_count, "Baltimore Sentiment Tweet Account", "Sentiment", "# of Tweets", img_path)