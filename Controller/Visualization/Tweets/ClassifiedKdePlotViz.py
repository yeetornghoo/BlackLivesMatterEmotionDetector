import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from Controller import PlutchikStandardController
from Helper import FolderHelper, DateHelper

viz_folder_name = "3_classified_viz"
plot_name = "kdeplot"
title_font_size = 28
'''
def plot_folder_path(dir_path, is_standard, lexicon_name):
    outputFile = dir_path + "img/"

    if is_standard:
        is_standard_folder = "standard"
    else:
        is_standard_folder = "individual"

    return outputFile + "{}/{}/{}/".format(is_standard_folder, lexicon_name, plot_name)


def plot_facet_grid(y_attr, x_attr, h_attr, df, output_file):

    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set(style='darkgrid', color_codes=True)
    ridge_plot = sns.FacetGrid(df, row=h_attr, hue=h_attr, aspect=4)
    ridge_plot.map(sns.kdeplot, x_attr, y_attr, alpha=.5, levels=5, fill=True, thresh=0.15)
    #ridge_plot.map(plt.scatter, x_attr, y_attr)
    ridge_plot.map(sns.lineplot, x_attr, y_attr, color='black', linewidth=0.5, size=1)
    ridge_plot.despine(bottom=True, left=False)
    ridge_plot.fig.subplots_adjust(hspace=0.5)

    for ax in ridge_plot.axes.flatten():
        ax.tick_params(labelbottom=True)

    plt.savefig("{}_facetgrid.png".format(output_file))
    plt.close()
'''


def plot_by_mood(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, output_dir, selected_mood):

    df_mood = df.loc[df[h_attr] == selected_mood]

    # PLOT SETTING
    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(12, 10))

    # CREATE LINE PLOT
    fig = sns.kdeplot(data=df_mood, x=x_attr, y=y_attr, common_norm=False, alpha=.5, levels=10, fill=True, thresh=0.15)
    fig.set(ylabel=y_attr_title.upper(), xlabel=x_attr_title.upper())
    plt.title(title, fontsize=title_font_size)
    plt.savefig("{}/{}_{}_plot.png".format(output_dir, plot_name, selected_mood))
    plt.close()


def plot(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, output_dir):

    # PLOT SETTING
    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(20, 14))

    # CREATE LINE PLOT
    fig = sns.kdeplot(data=df, x=x_attr, y=y_attr, hue=h_attr, common_norm=False, levels=8, fill=False, thresh=0.15)
    fig.set(ylabel=y_attr_title.upper(), xlabel=x_attr_title.upper())
    plt.title(title.upper(), fontsize=title_font_size)
    plt.setp(fig.get_legend().get_texts(), fontsize='15')
    plt.setp(fig.get_legend().get_title(), fontsize='16')
    plt.savefig("{}/{}_emotion_plot.png".format(output_dir, plot_name))
    plt.close()


def plot_sentiment_day_key_with_period(df, dir_path, location_nanme):

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Count"
    xAttrTitle = "Tweet Date"
    title = "Total Emotion Count Group by Day at {}".format(location_nanme)

    df_i = df[["tweet_created_date", "sentiment", "tweet_id"]].groupby(["tweet_created_date", "sentiment"], as_index=False).count()
    df_i['tweet_created_date'] = pd.to_datetime(df_i['tweet_created_date'], format='%Y-%m-%d')
    plot("tweet_id", "tweet_created_date", "sentiment", df_i, yAttrTitle, xAttrTitle, title, dir_path)
    df_i["sentiment"] = df_i["sentiment"].astype(str)

    for mood in PlutchikStandardController.moods:
        title = "Density Chart for {} at {}".format(mood.upper(), location_nanme)
        plot_by_mood("tweet_id", "tweet_created_date", "sentiment", df_i, yAttrTitle, xAttrTitle, title, dir_path, mood)


def plot_sentiment_day_key(df, dir_path, location_nanme):

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Sentiment Score"
    xAttrTitle = "Tweet Date"
    title = "Total Emotion Count Group by Day at {}".format(location_nanme)

    df_i = df[["tweet_created_date", "sentiment", "tweet_id"]].groupby(["tweet_created_date", "sentiment"], as_index=False).count()
    df_i['tweet_created_date'] = pd.to_datetime(df_i['tweet_created_date'], format='%Y-%m-%d')
    plot("tweet_id", "tweet_created_date", "sentiment", df_i, yAttrTitle, xAttrTitle, title, dir_path)


def plot_sentiment(df, dir_path, location_nanme):

    output_dir = "{}/img/{}".format(dir_path, viz_folder_name)

    # REMOVE NULL
    df = df[df["sentiment"].notna()]

    plot_sentiment_day_key(df, output_dir, location_nanme)
    #plot_sentiment_day_key_with_period(df, output_dir, location_nanme)
