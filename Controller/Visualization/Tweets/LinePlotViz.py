import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from Helper import FolderHelper

# SETTING
from Lexicon.DepecheMood import DepecheMoodController
from Lexicon.NRC import NrcController

plot_name = "lineplot"


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
    ridge_plot.map(plt.scatter, x_attr, y_attr)
    ridge_plot.map(sns.lineplot, x_attr, y_attr, color='black', linewidth=0.5)
    ridge_plot.despine(bottom=True, left=False)
    ridge_plot.fig.subplots_adjust(hspace=0.5)

    for ax in ridge_plot.axes.flatten():
        ax.tick_params(labelbottom=True)
        ax.tick_params(labelsize='10')

    plt.savefig("{}_facetgrid.png".format(output_file))
    plt.close()


def plot(y_attr, x_attr, g_attr, df, y_attr_title, x_attr_title, title, legend_title, output_file, y_scale):

    # PLOT SETTING
    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(20, 14))
    ax.set(yscale=y_scale)

    # CREATE LINE PLOT
    fig = sns.lineplot(y=y_attr, x=x_attr, hue=g_attr, data=df)
    fig.set(ylabel=y_attr_title.upper(), xlabel=x_attr_title.upper())
    plt.title(title.upper())

    fig.get_legend().set_title(legend_title.upper())
    plt.setp(fig.get_legend().get_texts(), fontsize='15')
    plt.setp(fig.get_legend().get_title(), fontsize='16')
    plt.savefig("{}_{}.png".format(output_file, y_scale))
    plt.close()


def plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, selected_key, n_start_date, n_end_date):

    # PARAMETER
    senti_name = "sentiment"
    senti_key = "sentiment_score"

    # REMOVE NULL
    df = df[df[senti_name].notna()]

    # SET PLOT LEGEND AN OUTPUT
    y_attr_title = "Total Sentiment {}".format(selected_key)
    x_attr_title = "Tweet Date"
    title = "Total ({}) Sentiment {} Group by Day ({} to {})".format(lexicon_name, selected_key, n_start_date, n_end_date)
    legend_title = "{} Sentiment".format(lexicon_name.upper())

    # FILTER
    start_date = datetime.strptime(n_start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(n_end_date, "%Y-%m-%d").date()
    df = df.loc[(df['tweet_created_date'] > start_date) & (df['tweet_created_date'] <= end_date)]

    # INDIVIDUAL
    output_file = plot_folder_path(dir_path, False, lexicon_name) + "{}_{}_by_day_by_period".format(selected_key, plot_name)
    df_i = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name], as_index=False).sum()
    plot(senti_key, "tweet_created_date", senti_name, df_i, y_attr_title, x_attr_title, title, legend_title, output_file, "linear")
    plot(senti_key, "tweet_created_date", senti_name, df_i, y_attr_title, x_attr_title, title, legend_title, output_file, "log")
    plot_facet_grid(senti_key, "tweet_created_date", senti_name, df_i, output_file)


def plot_sentiment_day_key_with_intensity(df, lexicon_name, dir_path, selected_key, min_intensity):

    # PARAMETER
    senti_name = "sentiment"
    senti_key = "sentiment_score"

    # REMOVE NULL
    df = df[df[senti_name].notna()]

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Sentiment {}".format(selected_key)
    xAttrTitle = "Tweet Date"
    title = "Total ({}) Sentiment {} Group by Day With Intensity ({})".format(lexicon_name, selected_key, min_intensity)
    legend_title = "{} Sentiment".format(lexicon_name.upper())

    # FILTER
    df = df.loc[(df[senti_key] > min_intensity)]

    # INDIVIDUAL
    output_file = plot_folder_path(dir_path, False, lexicon_name) + "{}_{}_by_day_with_intensity".format(selected_key, plot_name)
    df_i = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name]).sum()
    plot(senti_key, "tweet_created_date", senti_name, df_i, yAttrTitle, xAttrTitle, title, legend_title, output_file, "linear")
    plot(senti_key, "tweet_created_date", senti_name, df_i, yAttrTitle, xAttrTitle, title, legend_title, output_file, "log")


def plot_sentiment_day_key(df, lexicon_name, dir_path, selected_key):

    # PARAMETER
    senti_name = "sentiment"
    senti_key = "sentiment_score"

    # REMOVE NULL
    df = df[df[senti_name].notna()]

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Sentiment {}".format(selected_key)
    xAttrTitle = "Tweet Date"
    title = "Total ({}) Sentiment {} Group by Day".format(lexicon_name, selected_key)
    legend_title = "{} Sentiment".format(lexicon_name.upper())

    # INDIVIDUAL
    output_file = plot_folder_path(dir_path, False, lexicon_name) + "{}_{}_by_day".format(selected_key, plot_name)
    df_i = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name]).sum()
    plot(senti_key, "tweet_created_date", senti_name, df_i, yAttrTitle, xAttrTitle, title, legend_title, output_file, "linear")
    plot(senti_key, "tweet_created_date", senti_name, df_i, yAttrTitle, xAttrTitle, title, legend_title, output_file, "log")

'''
def plot_sentiment_hour_key_with_period(df, lexicon_name, dir_path, is_standard, selected_key, n_start_date, n_end_date):

    # PARAMETER
    senti_name = "{}_sentiment".format(lexicon_name)
    senti_key = "{}_sentiment_{}".format(lexicon_name, selected_key)

    # SET PLOT LEGEND AN OUTPUT
    y_attr_title = "Total Sentiment {}".format(selected_key)
    x_attr_title = "Tweet Hour"
    title = "Total ({}) Sentiment {} Group by Hour ({}-{})".format(lexicon_name, selected_key, n_start_date, n_end_date)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    output_file = plot_folder_path(dir_path, is_standard, lexicon_name) + "{}_lineplot_by_hour_by_period".format(selected_key)

    # GENERATE DATAFRAME
    start_date = datetime.strptime(n_start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(n_end_date, "%Y-%m-%d").date()
    mask = (df['tweet_created_date'] > start_date) & (df['tweet_created_date'] <= end_date)
    df = df.loc[mask]

    f_df = df[["tweet_created_hour", senti_name, senti_key]].groupby(["tweet_created_hour", senti_name], as_index=False).sum()

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_hour", senti_name, f_df, y_attr_title, x_attr_title, title, legend_title, output_file, "linear")
    #plot(senti_key, "tweet_created_hour", senti_name, f_df, y_attr_title, x_attr_title, title, legend_title, output_file, "log")
    plot_facet_grid(senti_key, "tweet_created_hour", senti_name, f_df, output_file)


def plot_sentiment_hour_key_with_intensity(df, lexicon_name, dir_path, is_standard, selected_key, min_intensity):

    # PARAMETER
    senti_name = "{}_sentiment".format(lexicon_name)
    senti_key = "{}_sentiment_{}".format(lexicon_name, selected_key)

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Sentiment {}".format(selected_key)
    xAttrTitle = "Tweet Hour"
    title = "Total ({}) Sentiment {} Group by Hour With Intensity ({})".format(lexicon_name, selected_key, min_intensity)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    output_file = plot_folder_path(dir_path, is_standard, lexicon_name) + "{}_lineplot_by_hour_with_intensity".format(selected_key)

    # GENERATE DATAFRAME
    f_df = df[["tweet_created_hour", senti_name, senti_key]].groupby(["tweet_created_hour", senti_name]).sum()

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_hour", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "linear")
    #plot(senti_key, "tweet_created_hour", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "log")


def plot_sentiment_hour_key(df, lexicon_name, dir_path, is_standard, selected_key):
    # PARAMETER
    senti_name = "{}_sentiment".format(lexicon_name)
    senti_key = "{}_sentiment_{}".format(lexicon_name, selected_key)  # SCORE OR COUNT

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Sentiment {}".format(selected_key)
    xAttrTitle = "Tweet Hour"
    title = "Total ({}) Sentiment {} Group by Hour".format(lexicon_name, selected_key)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    output_file = plot_folder_path(dir_path, is_standard, lexicon_name) + "{}_lineplot_by_hour".format(selected_key)

    # GENERATE DATAFRAME
    f_df = df[["tweet_created_hour", senti_name, senti_key]].groupby(["tweet_created_hour", senti_name]).sum()

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_hour", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "linear")
'''


def plot_sentiment(df, lexicon_name, dir_path, min_intensity, start_date, end_date):

    # RESET FOLDER
    FolderHelper.reset_dataset_viz_output_folder(dir_path, lexicon_name, plot_name)

    # LINE PLOT BY DAY
    plot_sentiment_day_key(df, lexicon_name, dir_path, "score")
    plot_sentiment_day_key_with_intensity(df, lexicon_name, dir_path, "score", min_intensity)
    plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, "score", start_date, end_date)

    '''
    # LINE PLOT BY HOUR
    plot_sentiment_hour_key(df, lexicon_name, dir_path, "score")
    plot_sentiment_hour_key(df, lexicon_name, dir_path, "count")
    plot_sentiment_hour_key_with_intensity(df, lexicon_name, dir_path, "score", min_intensity)
    plot_sentiment_hour_key_with_intensity(df, lexicon_name, dir_path, "count", min_intensity)
    plot_sentiment_hour_key_with_period(df, lexicon_name, dir_path, "score", start_date, end_date)
    plot_sentiment_hour_key_with_period(df, lexicon_name, dir_path, "count", start_date, end_date)
    '''