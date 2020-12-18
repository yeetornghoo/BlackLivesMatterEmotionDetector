import pandas as pd
import seaborn as sns
from datetime import datetime
from Controller import FileController, LogController
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection
from Controller.Visualization import LiveTweetViz
from Controller.Visualization.Tweets import LinePlotViz
from Controller.Baseline import BaselineViz

# SETTING
path = "C:/workspace/SocialMovementSentiment/dataset/RawTweets/Washington/"
date_format = "%Y-%m-%d %H:%M:%S"
n_start_date = "2020-05-22"
n_end_date = "2020-06-30"

df = pd.read_csv("_dataset/final-dataset.csv", sep=",")

# COUNT BY DAY
#LiveTweetViz.plot_line_by_day(df, date_format, n_start_date, n_end_date, path)

# COUNT BY HOUR
#LiveTweetViz.plot_line_by_hour(df, date_format, n_start_date, n_end_date, path)

# WORD CLOUD
LiveTweetViz.generate_word_assessment_by_upos_type(df, "ADJ", path)
LiveTweetViz.generate_word_assessment_by_upos_type(df, "VERB", path)
LiveTweetViz.generate_word_assessment_by_upos_type(df, "NOUN", path)
