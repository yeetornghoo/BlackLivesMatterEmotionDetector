import pandas as pd
from datetime import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from Controller import DataAssess
from Controller.Visualization import LinePlotViz, KdePlotViz
from Helper import DateHelper

# SETTING
date_format = "%Y-%m-%d %H:%M:%S"
min_intensity = 1.2
dir_path = "C:/workspace/SocialMovementSentiment/dataset/blm_minesota/"
key_focus = "score"
mood_set = "individual"
master_dataset_file = dir_path+"dataset.csv"
sentiment_dataset_file = "{}04-post-sentiment-False-dataset.csv".format(dir_path)
focus_from_date = "2020-05-23"
focus_to_date = "2020-06-05"


# LOAD AND COMBINE DATASET FILE
ori_df = pd.read_csv(master_dataset_file, sep=";")
ori_df.drop(['permalink', 'username', 'to_person', 'mentions', 'hashtags', 'geo',
             'record_inserted_date', 'state', 'radius', 'search_keyword'], axis=1, inplace=True)
sentiment_df = pd.read_csv(sentiment_dataset_file, sep=",")
df = pd.merge(sentiment_df, ori_df, on="text")


# PREPARE THE ATTRIBUTE
df['tweet_created_date'] = df['tweet_created_dt'].apply(lambda x: datetime.strptime(str(x), date_format).date())
df['tweet_created_hour'] = df['tweet_created_dt'].apply(lambda x: DateHelper.get_date_with_hour(str(x), date_format))
#DataAssess.run(df)

# SCORE AND COUNT COMPARISON
l_sentiment_date = "tweet_created_date"

include_count = True
include_standard = True

# LINE PLOT
#LinePlotViz.plot_sentiment(df, "nrc", dir_path, min_intensity, focus_from_date, focus_to_date, include_count, include_standard)
#LinePlotViz.plot_sentiment(df, "dpm", dir_path, min_intensity, focus_from_date, focus_to_date, include_count, include_standard)
KdePlotViz.plot_sentiment(df, "nrc", dir_path, min_intensity, focus_from_date, focus_to_date, include_count, include_standard)
#KdePlotViz.plot_sentiment(df, "dpm", dir_path, isStandard, min_intensity, focus_from_date, focus_to_date)
