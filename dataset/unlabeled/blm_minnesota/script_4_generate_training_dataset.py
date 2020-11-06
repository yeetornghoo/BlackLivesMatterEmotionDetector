import pandas as pd
import seaborn as sns
from Controller.Baseline import BaselineViz
from Controller import GitController, FileController, PlutchikStandardController

out_path = "img/baseline/"

# SETTING
sns.set_theme(style="whitegrid")
df = pd.read_csv("05-post-sentiment-dataset.csv", sep=",")

# FILTER WORD OF TWEET
df['ttl_tweet_text_word'] = df['tweet_text'].str.split().str.len()
df = df.loc[(df['ttl_tweet_text_word'] > 2)]
df = df.loc[:, ['sentiment', 'sentiment_count', 'sentiment_score', "tweet_text"]]

# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
BaselineViz.run_mood(df, out_path, 0.75)

# COMBINE TMP FILE
final_df = pd.DataFrame()
for mood in PlutchikStandardController.moods:
    tmp_df = pd.DataFrame()
    tmp_df = pd.read_csv("tmp/tmp-{}-dataset.csv".format(mood), sep=",")
    final_df.append(tmp_df)

BaselineViz.generate_count(df, out_path)

# SAVE FILE
FileController.save_df_to_csv("baseline-dataset.csv", df)

