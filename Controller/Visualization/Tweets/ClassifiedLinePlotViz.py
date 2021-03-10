import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from Helper import FolderHelper

viz_folder_name = "3_classified_viz"
plot_name = "lineplot"


def plot(y_attr, x_attr, df, y_attr_title, x_attr_title, title, output_dir, y_scale):

    # PLOT SETTING
    sns.color_palette("tab10")
    sns.set_style("ticks")
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set(yscale=y_scale)

    # CREATE LINE PLOT
    fig = sns.lineplot(y=y_attr, x=x_attr, hue="sentiment", data=df)
    fig.set(ylabel=y_attr_title.upper(), xlabel=x_attr_title.upper())
    plt.title(title.upper())

    plt.setp(fig.get_legend().get_texts(), fontsize='15')
    plt.setp(fig.get_legend().get_title(), fontsize='16')
    plt.savefig("{}/{}_{}_by_emotion_.png".format(output_dir, y_scale, plot_name))
    plt.close()


def plot_sentiment(df, dir_path, location_nanme):

    output_dir = "{}img/{}".format(dir_path, viz_folder_name)

    # REMOVE NULL
    df = df[df["sentiment"].notna()]

    # SET PLOT LEGEND AN OUTPUT
    yAttrTitle = "Total Tweets"
    xAttrTitle = "Tweet Date"
    title = "Total Tweets by Emotion Group by Day at {}".format(location_nanme)

    df_i = df[["tweet_created_date", "sentiment", "tweet_id"]].groupby(["tweet_created_date", "sentiment"]).count()
    plot("tweet_id", "tweet_created_date", df_i, yAttrTitle, xAttrTitle, title, output_dir, "linear")
    plot("tweet_id", "tweet_created_date", df_i, yAttrTitle, xAttrTitle, title, output_dir, "log")
