import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from Controller import DataAssess
from Helper import DateHelper

# SETTING
dir_path = "C:/workspace/SocialMovementSentiment/SecondDataset/SaintPaulCrimeIncident/"
source_dataset_file = dir_path+"dataset.csv"
source_date_format = "%Y/%m/%d %H:%M:%S+00"
focus_from_date = "2020/05/01"
focus_to_date = "2020/07/01"

# SEABORN SETTING
sns.color_palette("tab10")
sns.set_style("ticks")
sns.set_theme(style="whitegrid")

# FILTER
start_date = DateHelper.get_datetime64(focus_from_date, "%Y/%m/%d")
end_date = DateHelper.get_datetime64(focus_to_date, "%Y/%m/%d")


def get_blm_minesota(from_date, to_date):

    primary_dir_path = "C:/workspace/SocialMovementSentiment/dataset/blm_minnesota/"
    primary_dataset_source_file = "{}dataset.csv".format(primary_dir_path)

    # PRIMARY SOURCE
    primary_dataset_source_df = pd.read_csv(primary_dataset_source_file, sep=";")
    primary_dataset_source_df.drop(['permalink', 'username', 'to_person', 'mentions', 'hashtags', 'geo',
                 'record_inserted_date', 'state', 'radius', 'search_keyword'], axis=1, inplace=True)
    primary_dataset_source_df['tweet_created_date'] = primary_dataset_source_df['tweet_created_dt'].astype('datetime64[ns]')

    primary_dataset_sentiment_file = "{}04-post-sentiment-False-dataset.csv".format(primary_dir_path)
    primary_dataset_sentiment_df = pd.read_csv(primary_dataset_sentiment_file, sep=",")

    return_df = pd.merge(primary_dataset_sentiment_df, primary_dataset_source_df, on="text")
    return_df = return_df.loc[(return_df['tweet_created_date'] >= from_date) & (return_df['tweet_created_date'] <= to_date)]
    return_df['tweet_created_date'] = return_df['tweet_created_date'].apply(lambda x: datetime.strptime(str(x), DateHelper.standard_date_format).date())
    return return_df


# LOAD DATA FROM DATASET
df = pd.read_csv(source_dataset_file, sep=",")


# GENERATE CHART TO COMPARE WITH MINESOTA DATA
primary_df = get_blm_minesota(start_date, end_date)
primary_df_group = primary_df[["tweet_created_date", "tweet_id"]].groupby(["tweet_created_date"], as_index=False).count()


def generate_plot(df_s, df_p, start_date, end_date, x_attr, y_attr, h_attr, y_factor, sub_report_name):

    # FIXED DATA ISSUE
    df_s[x_attr] = df_s[x_attr].astype('datetime64[ns]')

    # CREATE LINE PLOT FROM PRIMARY DATA
    df_s = df_s.loc[(df_s[x_attr] >= start_date) & (df_s[x_attr] <= end_date)]
    df_s[x_attr] = df_s[x_attr].apply(lambda x: datetime.strptime(str(x), DateHelper.standard_date_format).date())
    df_group = df_s[[x_attr, y_attr, h_attr]].groupby([x_attr, h_attr], as_index=False).count()
    df_group[y_attr] = df_group[y_attr]*y_factor

    # PLOT
    fig, ax = plt.subplots(figsize=(25, 15))

    # CREATE LINE PLOT FROM PRIMARY DATA
    fig = sns.lineplot(y="tweet_id", x="tweet_created_date", data=df_p, ax=ax, linewidth=2.5, color='#000000')
    fig.set(ylabel="Totol Tweet Count", xlabel="Date")
    fig.set_xlabel(fig.get_xlabel(), fontsize=16)
    fig.set_ylabel(fig.get_ylabel(), fontsize=16)

    # CREATE SCATTER PLOT FROM SECONDARY DATA
    fig = sns.lineplot(x=x_attr, y=y_attr, hue=h_attr, palette="muted", data=df_group)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize='14')
    plt.setp(ax.get_yticklabels(), rotation_mode="anchor",  fontsize='14')
    plt.setp(fig.get_legend().get_texts(), fontsize='18')
    plt.setp(fig.get_legend().get_title(), fontsize='22')

    plt.title("Total #BLM Tweets v.s. Saint Paul Criminal Incident ({})".format(sub_report_name.replace("_", " ")).upper(), fontsize='25')
    plt.savefig("{}img/lineplot_comparison_{}.png".format(dir_path, sub_report_name).lower())
    plt.close()


generate_plot(df, primary_df_group, start_date, end_date, "DATE", "CASE NUMBER", "INCIDENT", 10, "by_INCIDENT")