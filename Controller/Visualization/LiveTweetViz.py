import pandas as pd
import re
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from Controller import DataNLP, LogController
from Controller.Visualization import WordFrequencyViz, WordClouldViz
from Helper import DateHelper

sns.set_theme(style="whitegrid")
plt.style.use('classic')


def plot_line_by_hour(df, date_format, n_start_date, n_end_date, path):

    # PREPARE DATASET
    df['tweet_created_hour'] = df['tweet_created_dt'].apply(lambda x: DateHelper.get_date_with_hour(str(x), date_format)).dt.hour
    df['tweet_created_dt'] = df['tweet_created_dt'].apply(lambda x: datetime.strptime(str(x), date_format).date())
    start_date = datetime.strptime(n_start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(n_end_date, "%Y-%m-%d").date()
    df = df.loc[(df['tweet_created_dt'] > start_date) & (df['tweet_created_dt'] <= end_date)]

    # GROUP BY HOURS
    df_count = df.groupby("tweet_created_hour", as_index=False).count()
    df_count.rename(columns={"tweet_id": "no_count"}, inplace=True)
    df_count.drop(['retweets', 'favorites', 'tweet_text', 'tweet_created_dt'], inplace=True, axis=1)

    #CRAFT CHART
    fig, ax = plt.subplots(figsize=(14, 10))
    fig = sns.lineplot(y="no_count", x="tweet_created_hour", data=df_count, marker='*')
    fig.set(ylabel="Number of Tweets", xlabel="Hour")
    plt.xticks(rotation=50)
    plt.title("Total Tweets by Hour", size=22)
    fig.xaxis.set_major_locator(ticker.MultipleLocator(1))

    for x, y in zip(df_count['tweet_created_hour'], df_count['no_count']):
        plt.text(x=x, y=y, s='{}'.format(y))

    plt.savefig("{}img/viz/line_by_hour.png".format(path), pad_inches=0.5, margin_inches=0.5, facecolor="white")
    plt.close()


def plot_line_by_day(df, date_format, n_start_date, n_end_date, path):

    # PREPARE DATASET
    df['tweet_created_dt'] = df['tweet_created_dt'].apply(lambda x: datetime.strptime(str(x), date_format).date())
    start_date = datetime.strptime(n_start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(n_end_date, "%Y-%m-%d").date()
    df = df.loc[(df['tweet_created_dt'] > start_date) & (df['tweet_created_dt'] <= end_date)]
    df_count = df.groupby("tweet_created_dt", as_index=False).count()
    df_count.rename(columns={"tweet_id": "no_count"}, inplace=True)
    df_count.drop(['retweets', 'favorites', 'tweet_text'], inplace=True, axis=1)
    print(df_count)
    #CRAFT CHART
    fig, ax = plt.subplots(figsize=(14, 10))
    fig = sns.lineplot(y="no_count", x="tweet_created_dt", data=df_count, marker='*')
    fig.set(ylabel="Number of Tweets", xlabel="Date")
    plt.xticks(rotation=50)
    plt.title("Total Tweets by Day", size=22)
    fig.xaxis.set_major_locator(ticker.MultipleLocator(1))

    for x, y in zip(df_count['tweet_created_dt'], df_count['no_count']):
        plt.text(x=x, y=y, s='{}'.format(y))

    plt.savefig("{}img/viz/line_by_day.png".format(path), pad_inches=0.5, margin_inches=0.5, facecolor="white")
    plt.close()


def generate_word_assessment_by_upos_type(df, upos_type, out_path):

    LogController.log("processing {}...".format(upos_type))

    # GENERATE POS
    df['tweet_text_tmp'] = df['tweet_text'].apply(lambda x: DataNLP.get_sentence_by_pos(str(x), upos_type))

    text = ''.join(df["tweet_text_tmp"].values.flatten())
    wordList = re.sub("[^\w]", " ", text).split()

    if len(wordList) > 0:

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        fig.suptitle("'{}' Word Visualization".format(upos_type), size=22)

        # GENERATE WORD FREQUENCY
        WordFrequencyViz.generate_by_axessubplot(ax1, wordList)

        # GENERATE WORD CLOUD
        WordClouldViz.generate_by_axessubplot_with_max(ax2, text, 30)

        fig.tight_layout()
        img_path = ("{}/img/viz/{}_word_viz.png".format(out_path, upos_type))
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0)

        plt.close('all')