import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# SETTING
from Controller import DataAssess, LogController
from Controller.Visualization.Accuracy import NrcReview, DepecheMoodReview, EmoSenticNetReview

dir_path = "C:/workspace/SocialMovementSentiment/dataset/SamEval2019_Task3/"
sentiment_dataset_file = "{}04-post-sentiment-False-dataset.csv".format(dir_path)

# LOAD SENTIMENT FILES
df = pd.read_csv(sentiment_dataset_file, sep=",")
#DataAssess.run(df)


# FIXED guilt and guit
df = df.rename(columns={'tweet_text': 'text'})
df = df.rename(columns={'label': 'ori_sentiment'})

# REVIEW ORIGINAL AND NRC
NrcReview.run(df, dir_path, "sameval2019")
DepecheMoodReview.run(df, dir_path, "sameval2019")
EmoSenticNetReview.run(df, dir_path, "sameval2019")
