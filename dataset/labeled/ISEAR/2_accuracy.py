import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# SETTING
from Controller import DataAssess, LogController
from Controller.Visualization.Accuracy import NrcReview, DepecheMoodReview, EmoSenticNetReview

dir_path = "C:/workspace/SocialMovementSentiment/dataset/labeled/ISEAR/"


# LOAD SENTIMENT FILES
df = pd.read_csv("05-post-sentiment-dataset.csv", sep=",")
DataAssess.run(df)

# FIXED guilt and guit
df.loc[df['ori_sentiment'] == 'guit', 'sentiment'] = 'guilt'

# REVIEW ORIGINAL AND NRC
#NrcReview.run(df, dir_path, "isear")
#DepecheMoodReview.run(df, dir_path, "isear")
EmoSenticNetReview.run(df, dir_path, "isear")
