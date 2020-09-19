import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from Helper import FolderHelper

# SETTING
plot_name = "lineplot"


def plot_folder_path(dir_path, is_standard, lexicon_name):
    outputFile = dir_path + "img/"

    if is_standard:
        is_standard_folder = "standard"
    else:
        is_standard_folder = "individual"

    return outputFile + "{}/{}/{}/".format(is_standard_folder, plot_name, lexicon_name)


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


def plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, is_standard, selected_key, n_start_date, n_end_date):

    # PARAMETER
    senti_name = "{}_sentiment".format(lexicon_name)
    senti_key = "{}_sentiment_{}".format(lexicon_name, selected_key)

    # SET PLOT LEGEND AN OUTPUT
    y_attr_title = "Total Sentiment {}".format(selected_key)
    x_attr_title = "Tweet Date"
    title = "Total ({}) Sentiment {} Group by Day ({} to {})".format(lexicon_name, selected_key, n_start_date, n_end_date)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    output_file = plot_folder_path(dir_path, is_standard, lexicon_name) + "{}_lineplot_by_day_by_period".format(selected_key)

    # GENERATE DATAFRAME
    start_date = datetime.strptime(n_start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(n_end_date, "%Y-%m-%d").date()
    mask = (df['tweet_created_date'] > start_date) & (df['tweet_created_date'] <= end_date)
    df = df.loc[mask]
    f_df = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name], as_index=False).sum()

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_date", senti_name, f_df, y_attr_title, x_attr_title, title, legend_title, output_file, "linear")
    plot(senti_key, "tweet_created_date", senti_name, f_df, y_attr_title, x_attr_title, title, legend_title, output_file, "log")


def plot_sentiment_day_key_with_intensity(df, lexicon_name, dir_path, is_standard, selected_key, min_intensity):

    # PARAMETER
    senti_name = "{}_sentiment".format(lexicon_name)
    senti_key = "{}_sentiment_{}".format(lexicon_name, selected_key)

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Sentiment {}".format(selected_key)
    xAttrTitle = "Tweet Date"
    title = "Total ({}) Sentiment {} Group by Day With Intensity ({})".format(lexicon_name, selected_key, min_intensity)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    output_file = plot_folder_path(dir_path, is_standard, lexicon_name) + "{}_lineplot_by_day_with_intensity".format(selected_key)

    # GENERATE DATAFRAME
    f_df = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name]).sum()

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_date", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "linear")
    plot(senti_key, "tweet_created_date", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "log")


def plot_sentiment_day_key(df, lexicon_name, dir_path, is_standard, selected_key):
    # PARAMETER
    senti_name = "{}_sentiment".format(lexicon_name)
    senti_key = "{}_sentiment_{}".format(lexicon_name, selected_key)  # SCORE OR COUNT

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Sentiment {}".format(selected_key)
    xAttrTitle = "Tweet Date"
    title = "Total ({}) Sentiment {} Group by Day".format(lexicon_name, selected_key)
    legend_title = "{} Sentiment".format(lexicon_name.upper())
    output_file = plot_folder_path(dir_path, is_standard, lexicon_name) + "{}_lineplot_by_day".format(selected_key)

    # GENERATE DATAFRAME
    f_df = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name]).sum()

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_date", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "linear")
    plot(senti_key, "tweet_created_date", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "log")


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

    f_df = df[["tweet_created_hour", senti_name, senti_key]].groupby(["tweet_created_hour", senti_name]).sum()

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_hour", senti_name, f_df, y_attr_title, x_attr_title, title, legend_title, output_file, "linear")
    plot(senti_key, "tweet_created_hour", senti_name, f_df, y_attr_title, x_attr_title, title, legend_title, output_file, "log")


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
    plot(senti_key, "tweet_created_hour", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "log")


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


def reset_plot_folder(dir_path, lexicon_name):

    standard_fdr = "{}img/standard/{}".format(dir_path, plot_name)
    individual_fdr = "{}img/individual/{}".format(dir_path, plot_name)

    FolderHelper.reset_folder(standard_fdr)
    FolderHelper.reset_folder(individual_fdr)

    FolderHelper.create_folder("{}/{}".format(standard_fdr, lexicon_name))
    FolderHelper.create_folder("{}/{}".format(individual_fdr, lexicon_name))


def plot_sentiment(df, lexicon_name, dir_path, is_standard, min_intensity, start_date, end_date):

    # RESET FOLDER
    reset_plot_folder(dir_path, lexicon_name)

    # LINE PLOT BY DAY
    plot_sentiment_day_key(df, lexicon_name, dir_path, is_standard, "score")
    plot_sentiment_day_key(df, lexicon_name, dir_path, is_standard, "count")
    plot_sentiment_day_key_with_intensity(df, lexicon_name, dir_path, is_standard, "score", min_intensity)
    plot_sentiment_day_key_with_intensity(df, lexicon_name, dir_path, is_standard, "count", min_intensity)
    plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, is_standard, "score", start_date, end_date)
    plot_sentiment_day_key_with_period(df, lexicon_name, dir_path, is_standard, "count", start_date, end_date)

    # LINE PLOT BY HOUR
    plot_sentiment_hour_key(df, lexicon_name, dir_path, is_standard, "score")
    plot_sentiment_hour_key(df, lexicon_name, dir_path, is_standard, "count")
    plot_sentiment_hour_key_with_intensity(df, lexicon_name, dir_path, is_standard, "score", min_intensity)
    plot_sentiment_hour_key_with_intensity(df, lexicon_name, dir_path, is_standard, "count", min_intensity)
    plot_sentiment_hour_key_with_period(df, lexicon_name, dir_path, is_standard, "score", start_date, end_date)
    plot_sentiment_hour_key_with_period(df, lexicon_name, dir_path, is_standard, "count", start_date, end_date)
