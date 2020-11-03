import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import norm

from Controller import PlutchikStandardController
from Controller.Visualization import BellCurveViz, BoxplotViz

# SETTING
sns.set_theme(style="whitegrid")
df = pd.read_csv("05-post-sentiment-dataset.csv", sep=",")
df = df.loc[:, ['tweet_id', 'nrc_sentiment', 'nrc_sentiment_score']]
df.rename(columns={"nrc_sentiment": "sentiment", "nrc_sentiment_score": "sentiment_score"}, inplace=True)
out_path = "img/baseline/"


def generate_viz(df, class_name, percentage):

    q3_value = df["sentiment_score"].quantile(percentage)
    df_q3 = df.loc[(df["sentiment_score"] >= q3_value)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle("Dataset Visualization by '{}' \n {} records for {} and above".format(class_name, len(df_q3.index), percentage))

    BellCurveViz.generate_bellcurve(df, percentage, ax1)
    BoxplotViz.generate_boxplot(df, percentage, ax2)
    plt.savefig("{}{}_bell_curve.png".format(out_path, class_name))
    plt.text(0.5, 0.5, "sssdfsfs", horizontalalignment='right')

    fig.clear()
    plt.close('all')

    #df_q3.to_csv("{}{}_dataset.csv".format(out_path, class_name), index=False, encoding='utf-8')


def df_summary(df, class_name, percentage):
    df_class = df.loc[(df["sentiment"] == class_name)]
    generate_viz(df_class, class_name, percentage)


min_perc = 0.5
df_summary(df, "fear", min_perc)
df_summary(df, "anger", min_perc)
df_summary(df, "sadness", min_perc)
df_summary(df, "trust", min_perc)
df_summary(df, "joy", min_perc)
df_summary(df, "surprise", min_perc)
df_summary(df, "anticipation", min_perc)
df_summary(df, "disgust", min_perc)