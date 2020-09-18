import pandas as pd
from datetime import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from Controller import DataAssess
from Controller.Visualization import LinePlotViz
from Helper import DateHelper

# SETTING
date_format = "%Y-%m-%d %H:%M:%S"
min_intensity = 1.2
dir_path = "C:/workspace/SocialMovementSentiment/dataset/blm_minesota/"
key_focus = "score"
mood_set = "individual"
master_dataset_file = dir_path+"dataset.csv"
sentiment_dataset_file = dir_path+"04-post-sentiment-True-dataset.csv"
focus_from_date = "28-05-2020"
focus_to_date = "01-06-2020"
isStandard = True

# LOAD AND COMBINE DATASET FILE
ori_df = pd.read_csv(master_dataset_file, sep=";")
ori_df.drop(['permalink', 'username', 'to_person', 'mentions', 'hashtags', 'geo',
             'record_inserted_date', 'state', 'radius', 'search_keyword'], axis=1, inplace=True)
sentiment_df = pd.read_csv(sentiment_dataset_file, sep=",")
df = pd.merge(sentiment_df, ori_df, on="text")

# PREPARE THE ATTRIBUTE
df['tweet_created_date'] = df['tweet_created_dt'].apply(lambda x: datetime.strptime(str(x), date_format).date())
df['tweet_created_hour'] = df['tweet_created_dt'].apply(lambda x: DateHelper.get_date_with_hour(str(x), date_format))

DataAssess.run(df)

# SCORE AND COUNT COMPARISON
l_sentiment_date = "tweet_created_date"
## BY DAY

LinePlotViz.line_plot_sentiment(df, "nrc", dir_path, isStandard, min_intensity, focus_from_date, focus_to_date)
LinePlotViz.line_plot_sentiment(df, "dpm", dir_path, isStandard, min_intensity, focus_from_date, focus_to_date)
'''
## BY HOUR
LinePlotViz.line_plot_sentiment_hour(df, "nrc", dir_path, isStandard, "score")
LinePlotViz.line_plot_sentiment_hour(df, "nrc", dir_path, isStandard, "count")
LinePlotViz.line_plot_sentiment_hour_with_min_intensity(df, "nrc", dir_path, isStandard, "score", min_intensity)
LinePlotViz.line_plot_sentiment_hour_with_min_intensity(df, "nrc", dir_path, isStandard, "count", min_intensity)
'''

# SCORE AND COUNT COMPARISON/ INTENSITY


# SCORE AND COUNT COMPARISON / FIXED DATE / DATE


# SCORE AND COUNT COMPARISON / FIXED DATE / HOUR


# LINEAR V.S. LOG

