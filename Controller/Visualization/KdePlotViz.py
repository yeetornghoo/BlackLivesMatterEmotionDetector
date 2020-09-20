import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from Helper import FolderHelper, DateHelper

# SETTING
plot_name = "kdeplot"


def plot_folder_path(dir_path, is_standard, lexicon_name):
    outputFile = dir_path + "img/"

    if is_standard:
        is_standard_folder = "standard"
    else:
        is_standard_folder = "individual"

    return outputFile + "{}/{}/{}/".format(is_standard_folder, plot_name, lexicon_name)


def reset_plot_folder(dir_path, lexicon_name):

    standard_fdr = "{}img/standard/{}".format(dir_path, plot_name)
    individual_fdr = "{}img/individual/{}".format(dir_path, plot_name)

    FolderHelper.reset_folder(standard_fdr)
    FolderHelper.reset_folder(individual_fdr)

    FolderHelper.create_folder("{}/{}".format(standard_fdr, lexicon_name))
    FolderHelper.create_folder("{}/{}".format(individual_fdr, lexicon_name))


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
        #ax.tick_params(labelsize='15')

    plt.savefig("{}_facetgrid.png".format(output_file))
    plt.close()


def plot(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, legend_title, output_file):

    # PLOT SETTING
    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(20, 14))

    # CREATE LINE PLOT
    fig = sns.kdeplot(data=df, x=x_attr, y=y_attr, hue=h_attr, common_norm=False, alpha=.5, levels=8, fill=True, thresh=0.15)
    #fig = sns.lineplot(data=df, x=x_attr, y=y_attr, hue=h_attr)
    fig.set(ylabel=y_attr_title.upper(), xlabel=x_attr_title.upper())
    plt.title(title.upper())
    fig.get_legend().set_title(legend_title.upper())
    plt.setp(fig.get_legend().get_texts(), fontsize='15')
    plt.setp(fig.get_legend().get_title(), fontsize='16')
    plt.savefig("{}.png".format(output_file))
    plt.close()


def plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, is_standard, selected_key, n_start_date, n_end_date):

    # PARAMETER
    senti_name = "{}_sentiment".format(lexicon_name)
    senti_key = "{}_sentiment_{}".format(lexicon_name, selected_key)

    # SET PLOT LEGEND AN OUTPUT
    y_attr_title = "Total Sentiment {}".format(selected_key)
    x_attr_title = "Tweet Date"
    title = "Total ({}) Sentiment {} Group by Day ({} to {})".format(lexicon_name, selected_key, n_start_date, n_end_date)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    output_file = plot_folder_path(dir_path, is_standard, lexicon_name) + "{}_{}_by_day_by_period".format(selected_key, plot_name)

    # GENERATE DATAFRAME
    start_date = datetime.strptime(n_start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(n_end_date, "%Y-%m-%d").date()
    df = df.loc[(df['tweet_created_date'] > start_date) & (df['tweet_created_date'] <= end_date)]

    grouper = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name])
    f_df = grouper[senti_key].sum().to_frame(name=senti_key).reset_index()
    f_df['tweet_created_date'] = pd.to_datetime(f_df['tweet_created_date'], format='%Y-%m-%d')
    f_df[senti_name] = f_df[senti_name].astype(str)

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_date", senti_name, f_df, y_attr_title, x_attr_title, title, legend_title, output_file)
    plot_facet_grid(senti_key, "tweet_created_date", senti_name, f_df, output_file)


def plot_sentiment_day_key(df, lexicon_name, dir_path, is_standard, selected_key):
    
    # PARAMETER
    senti_name = "{}_sentiment".format(lexicon_name)
    senti_key = "{}_sentiment_{}".format(lexicon_name, selected_key)

    # SET PLOT LEGEND AN OUTPUT
    y_attr_title = "Total Sentiment {}".format(selected_key)
    x_attr_title = "Tweet Date"
    title = "Total ({}) Sentiment {} Group by Day".format(lexicon_name, selected_key)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    output_file = plot_folder_path(dir_path, is_standard, lexicon_name) + "{}_{}_by_day".format(selected_key, plot_name)

    df['tweet_created_date'] = pd.to_datetime(df['tweet_created_date'], format='%Y-%m-%d')

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_date", senti_name, df, y_attr_title, x_attr_title, title, legend_title, output_file)
    plot_facet_grid(senti_key, "tweet_created_date", senti_name, df, output_file)


def plot_sentiment(df, lexicon_name, dir_path, is_standard, min_intensity, start_date, end_date):

    # RESET FOLDER
    reset_plot_folder(dir_path, lexicon_name)

    # LINE PLOT BY DAY
    plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, is_standard, "score", start_date, end_date)
    # plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, is_standard, "count", start_date, end_date)
    plot_sentiment_day_key(df, lexicon_name, dir_path, is_standard, "score")
    # plot_sentiment_day_key(df, lexicon_name, dir_path, is_standard, "count")