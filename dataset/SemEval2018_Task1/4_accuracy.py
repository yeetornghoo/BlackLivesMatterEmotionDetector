import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# SETTING
from Controller import DataAssess, LogController
from Controller.Visualization.Accuracy import NrcReview, DepecheMoodReview, EmoSenticNetReview

dir_path = "C:/workspace/SocialMovementSentiment/dataset/SemEval2018_Task1/"
sentiment_dataset_file = "{}04-post-sentiment-False-dataset.csv".format(dir_path)

# LOAD SENTIMENT FILES
df = pd.read_csv(sentiment_dataset_file, sep=",")
DataAssess.run(df)


# FIXED guilt and guit
df = df.rename(columns={'Tweet': 'text'})
df = df.rename(columns={'sentiment': 'ori_sentiment'})


# REVIEW ORIGINAL AND NRC
NrcReview.run(df, dir_path, "sameval2018")
DepecheMoodReview.run(df, dir_path, "sameval2018")
EmoSenticNetReview.run(df, dir_path, "sameval2018")