import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from Controller import PlutchikStandardController
from Helper import FolderHelper, DateHelper

plot_name = "kdeplot"


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


def plot_by_mood(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, legend_title, output_file, selected_mood):

    print(output_file)

    df_mood = df.loc[df[h_attr] == selected_mood]

    # PLOT SETTING
    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(20, 14))

    # CREATE LINE PLOT
    fig = sns.kdeplot(data=df_mood, x=x_attr, y=y_attr, common_norm=False, alpha=.5, levels=5, fill=True, thresh=0.15)
    fig.set(ylabel=y_attr_title.upper(), xlabel=x_attr_title.upper())
    plt.title("{}".format(selected_mood).upper(), fontsize='30')
    plt.savefig("{}_{}.png".format(output_file, selected_mood))
    plt.close()


def plot(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, legend_title, output_file):

    # PLOT SETTING
    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(20, 14))

    # CREATE LINE PLOT
    fig = sns.kdeplot(data=df, x=x_attr, y=y_attr, hue=h_attr, common_norm=False, levels=8, fill=False, thresh=0.15)
    fig.set(ylabel=y_attr_title.upper(), xlabel=x_attr_title.upper())
    plt.title(title.upper())
    fig.get_legend().set_title(legend_title.upper())
    plt.setp(fig.get_legend().get_texts(), fontsize='15')
    plt.setp(fig.get_legend().get_title(), fontsize='16')
    plt.savefig("{}.png".format(output_file))
    plt.close()


def plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, n_start_date, n_end_date):

    # PARAMETER
    senti_name = "sentiment"
    senti_key = "sentiment_score"

    # REMOVE NULL
    df = df[df[senti_name].notna()]

    # SET PLOT LEGEND AN OUTPUT
    y_attr_title = "Total Sentiment Score"
    x_attr_title = "Tweet Date"
    title = "Total ({}) Sentiment Score Group by Day ({} to {})".format(lexicon_name, n_start_date, n_end_date)
    legend_title = "{} Sentiment".format(lexicon_name.upper())

    # GENERATE DATAFRAME
    start_date = DateHelper.get_date_with_time(n_start_date).date()
    end_date = DateHelper.get_date_with_time(n_end_date).date()
    df = df.loc[(df['tweet_created_date'] > start_date) & (df['tweet_created_date'] <= end_date)]

    # INDIVIDUAL
    output_file = plot_folder_path(dir_path, False, lexicon_name) + "score_{}_by_day_by_period".format(plot_name)
    df_i = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name], as_index=False).sum()
    df_i['tweet_created_date'] = pd.to_datetime(df_i['tweet_created_date'], format='%Y-%m-%d')
    df_i[senti_name] = df_i[senti_name].astype(str)

    for mood in PlutchikStandardController.moods:
        print("MOOD:{}".format(mood))
        plot_by_mood(senti_key, "tweet_created_date", senti_name, df_i, y_attr_title,
                     x_attr_title, title, legend_title, output_file, mood)


def plot_sentiment_day_key(df, lexicon_name, dir_path):

    # PARAMETER
    senti_name = "sentiment"
    senti_key = "sentiment_score"

    # REMOVE NULL
    df = df[df[senti_name].notna()]

    # SET PLOT LEGEND AN OUTPUT
    y_attr_title = "Total Sentiment Score"
    x_attr_title = "Tweet Date"
    title = "Total ({}) Sentiment Score Group by Day".format(lexicon_name)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    df['tweet_created_date'] = pd.to_datetime(df['tweet_created_date'], format='%Y-%m-%d')

    output_file = plot_folder_path(dir_path, False, lexicon_name) + "score_{}_by_day".format(plot_name)
    df_i = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name], as_index=False).sum()
    plot(senti_key, "tweet_created_date", senti_name, df_i, y_attr_title, x_attr_title, title, legend_title, output_file)
    plot_facet_grid(senti_key, "tweet_created_date", senti_name, df_i, output_file)


def plot_sentiment(df, lexicon_name, dir_path, start_date, end_date):

    # RESET FOLDER
    FolderHelper.reset_dataset_viz_output_folder(dir_path, lexicon_name, plot_name)

    plot_sentiment_day_key(df, lexicon_name, dir_path)
    plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, start_date, end_date)

