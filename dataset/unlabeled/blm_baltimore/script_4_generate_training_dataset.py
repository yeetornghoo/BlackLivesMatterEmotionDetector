import pandas as pd
import seaborn as sns
from Controller.Baseline import BaselineViz
from Controller import GitController

# SETTING
sns.set_theme(style="whitegrid")
df = pd.read_csv("05-post-sentiment-dataset.csv", sep=",")
df = df[["nrc_sentiment", "nrc_sentiment_score", "text"]]
df.rename(columns={"nrc_sentiment": "sentiment",
                   "nrc_sentiment_score": "sentiment_score",
                   "text": "tweet_text"}, inplace=True)
out_path = "img/baseline/"

# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
BaselineViz.run_mood(df, out_path, 0.5)

# COMMIT TO GIT
#GitController.commit("auto: update latest unlabeled data - washington dc")