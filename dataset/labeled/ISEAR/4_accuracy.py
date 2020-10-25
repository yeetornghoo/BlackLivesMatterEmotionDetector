import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# SETTING
from Controller import DataAssess, LogController
from Controller.Visualization.Accuracy import NrcReview, DepecheMoodReview, EmoSenticNetReview

dir_path = "C:/workspace/SocialMovementSentiment/dataset/ISEAR/"
sentiment_dataset_file = "{}04-post-sentiment-False-ISEAR.txt".format(dir_path)

# LOAD SENTIMENT FILES
df = pd.read_csv(sentiment_dataset_file, sep=",")
DataAssess.run(df)

# FIXED guilt and guit
df.loc[df['ori_sentiment'] == 'guit', 'ori_sentiment'] = 'guilt'

# REVIEW ORIGINAL AND NRC
NrcReview.run(df, dir_path, "isear")
DepecheMoodReview.run(df, dir_path, "isear")
EmoSenticNetReview.run(df, dir_path, "isear")
