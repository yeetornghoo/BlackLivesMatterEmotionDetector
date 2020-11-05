import pandas as pd
from datetime import datetime

from Controller import DataAssess
from Controller.Visualization import BarPlotViz
from Controller.Visualization.Tweets import KdePlotViz, LinePlotViz
from Helper import DateHelper

# SETTING
date_format = "%Y-%m-%d %H:%M:%S"
min_intensity = 1.2
dir_path = "C:/workspace/SocialMovementSentiment/dataset/blm_minnesota/"
focus_from_date = "2020-05-23"
focus_to_date = "2020-06-05"

# LOAD AND PREPARE DATASET
df = pd.read_csv("05-post-sentiment-dataset.csv", sep=",")

# PREPARE THE ATTRIBUTE
df['tweet_created_date'] = df['tweet_created_dt'].apply(lambda x: datetime.strptime(str(x), date_format).date())
df['tweet_created_hour'] = df['tweet_created_dt'].apply(lambda x: DateHelper.get_date_with_hour(str(x), date_format))
DataAssess.run(df)

# LINE PLOT
LinePlotViz.plot_sentiment(df, "nrc", dir_path, min_intensity, focus_from_date, focus_to_date)
KdePlotViz.plot_sentiment(df, "nrc", dir_path, focus_from_date, focus_to_date)

# TWEET COUNT
img_path = dir_path+"img/tweet_count.png"
df_count = df.loc[:, ['sentiment', 'tweet_text']]
df_count = df_count.groupby("sentiment").count()
BarPlotViz.generate_barplot(df_count, "Baltimore Sentiment Tweet Account", "Sentiment", "# of Tweets", img_path)
