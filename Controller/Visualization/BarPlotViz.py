import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from Helper import FolderHelper

# SETTING
plot_name = "barplot"


def plot_folder_path(dir_path, is_standard, lexicon_name):
    outputFile = dir_path + "img/"

    if is_standard:
        is_standard_folder = "standard"
    else:
        is_standard_folder = "individual"

    return outputFile + "{}/{}/{}/".format(is_standard_folder, plot_name, lexicon_name)


def plot(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, legend_title, output_file, y_scale):

    # PLOT SETTING
    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(20, 14))
    ax.set(yscale=y_scale)

    g = sns.FacetGrid(df, col=h_attr)
    g.map(get_sub_plot(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, legend_title, output_file, "log"), h_attr)
    g.map(get_sub_plot(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, legend_title, output_file, "linear"), h_attr)
    plt.savefig("{}_{}.png".format(output_file, y_scale))
    plt.close()


def get_sub_plot(y_attr, x_attr, h_attr, df, y_attr_title, x_attr_title, title, legend_title, output_file, y_scale):

    # CREATE LINE PLOT
    fig, ax = sns.lineplot(y=y_attr, x=x_attr, hue=h_attr, data=df)
    #ax.set(yscale=y_scale)
    fig.set(ylabel=y_attr_title.upper(), xlabel=x_attr_title.upper())
    plt.title(title.upper())
    fig.get_legend().set_title(legend_title.upper())
    plt.setp(fig.get_legend().get_texts(), fontsize='15')
    plt.setp(fig.get_legend().get_title(), fontsize='16')
    return fig


def reset_plot_folder(dir_path, lexicon_name):

    standard_fdr = "{}img/standard/{}".format(dir_path, plot_name)
    individual_fdr = "{}img/individual/{}".format(dir_path, plot_name)

    FolderHelper.reset_folder(standard_fdr)
    FolderHelper.reset_folder(individual_fdr)

    FolderHelper.create_folder("{}/{}".format(standard_fdr, lexicon_name))
    FolderHelper.create_folder("{}/{}".format(individual_fdr, lexicon_name))


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
    f_df = df[["tweet_created_date", senti_name, senti_key]].groupby(["tweet_created_date", senti_name], as_index=False).sum()

    # CREATE LINE PLOT
    plot(senti_key, "tweet_created_date", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "linear")
    #plot(senti_key, "tweet_created_date", senti_name, f_df, yAttrTitle, xAttrTitle, title, legend_title, output_file, "log")


def plot_sentiment(df, lexicon_name, dir_path, is_standard, min_intensity, start_date, end_date):

    # RESET FOLDER
    reset_plot_folder(dir_path, lexicon_name)

    # LINE PLOT BY DAY
    plot_sentiment_day_key(df, lexicon_name, dir_path, is_standard, "score")
    #plot_sentiment_day_key(df, lexicon_name, dir_path, is_standard, "count")