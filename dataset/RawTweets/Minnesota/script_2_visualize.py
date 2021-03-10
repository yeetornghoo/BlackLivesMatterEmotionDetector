import pandas as pd
from datetime import datetime

from Controller.Visualization import LiveTweetViz
from Controller.Visualization.Tweets import ClassifiedLinePlotViz, ClassifiedKdePlotViz
from Helper import DateHelper


# SETTING
path = "C:/workspace/SocialMovementSentiment/dataset/RawTweets/Minnesota/"
date_format = "%Y-%m-%d %H:%M:%S"
focus_from_date = "2020-05-25"
focus_to_date = "2020-06-21"
df = pd.read_csv("_dataset/classified_dataset.csv", sep=",")

# PREPARE THE ATTRIBUTE
df['tweet_created_date'] = df['tweet_created_dt'].apply(lambda x: datetime.strptime(str(x), date_format).date())
df['tweet_created_hour'] = df['tweet_created_dt'].apply(lambda x: DateHelper.get_date_with_hour(str(x), date_format))

# FILTER BY DATE
start_date = DateHelper.get_date_with_time(focus_from_date).date()
end_date = DateHelper.get_date_with_time(focus_to_date).date()
df = df.loc[(df['tweet_created_date'] > start_date) & (df['tweet_created_date'] <= end_date)]

'''
# COUNT BY DAY
LiveTweetViz.plot_line_by_day(df, date_format, n_start_date, n_end_date, path)

# COUNT BY HOUR
LiveTweetViz.plot_line_by_hour(df, date_format, n_start_date, n_end_date, path)
'''

# WORD CLOUD
LiveTweetViz.generate_word_assessment_by_upos_type(df, "ADJ", path)
LiveTweetViz.generate_word_assessment_by_upos_type(df, "VERB", path)
LiveTweetViz.generate_word_assessment_by_upos_type(df, "NOUN", path)

'''
# LINE CHART
ClassifiedLinePlotViz.plot_sentiment(df, path, "Minnesota")
ClassifiedKdePlotViz.plot_sentiment(df, path, "Minnesota")
'''