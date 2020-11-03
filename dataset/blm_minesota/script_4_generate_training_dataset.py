import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import norm
from Controller.Visualization import BellCurveViz

# SETTING


sns.set_theme(style="whitegrid")
df = pd.read_csv("05-post-sentiment-dataset.csv", sep=",")
df = df.loc[:, ['tweet_id', 'nrc_sentiment', 'nrc_sentiment_score']]
df.rename(columns={"nrc_sentiment": "sentiment", "nrc_sentiment_score": "sentiment_score"}, inplace=True)
out_path = "img/baseline/"


def generate_viz(df, class_name, percentage):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle("Dataset Visualization by '{}'".format(class_name))

    generate_viz(df, class_name, percentage)
    BellCurveViz.generate_bellcurve(df, class_name, percentage, out_path, ax1)
    #plt.savefig("{}{}_bell_curve.png".format(out_path, class_name))

    fig.clear()
    plt.close(fig)


def create_box_plot(df_obj, class_name, q3_value, percentage):
    class_sentiment_scores = df_obj["nrc_sentiment_score"]
    fig1, ax1 = plt.subplots(figsize=(9, 6))
    plt.style.use('fivethirtyeight')
    ax1.boxplot(class_sentiment_scores, vert=False)
    plt.title("Boxplot of '{}'".format(class_name))
    plt.axvline(x=q3_value, linestyle="--", linewidth=2, color="r")
    plt.text(q3_value + 0.1, 1.2, "upper quantitle of {}% ({})".format(percentage * 100, round(q3_value, 4)))
    plt.savefig("{}{}_boxplot.png".format(out_path, class_name))
    #plt.show()


def df_summary(df, class_name, percentage):
    generate_viz(df, class_name, percentage)
    #BellCurveViz.generate_bellcurve(df, class_name, percentage, out_path)
    '''
    df_1 = df.loc[(df["nrc_sentiment"] == class_name)]

    min_value = df_1["nrc_sentiment_score"].min()
    max_value = df_1["nrc_sentiment_score"].max()
    std_value = df_1["nrc_sentiment_score"].std()
    mean_value = df_1["nrc_sentiment_score"].mean()
    q3_value = df_1["nrc_sentiment_score"].quantile(percentage)

    print("std: {}".format(std_value))
    print("mean: {}".format(mean_value))
    print("min: {}".format(min_value))
    print("max: {}".format(max_value))
    print("quantile ({}%) : {}".format(percentage * 100, q3_value))

    create_bell_curve(min_value, max_value, mean_value, std_value, q3_value, class_name, percentage)
    create_box_plot(df_1, class_name, q3_value, percentage)

    # SAVE FILE
    df_final = df.loc[(df["nrc_sentiment"] == class_name) & (df["nrc_sentiment_score"] >= q3_value)]
    df_final.to_csv("{}{}_dataset.csv".format(out_path, class_name), index=False, encoding='utf-8')
    '''

upper_quatile = 0.75
df_summary(df, "fear", upper_quatile)