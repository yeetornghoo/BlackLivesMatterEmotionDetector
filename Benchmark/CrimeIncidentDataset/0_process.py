import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from Controller import DataAssess
from Helper import DateHelper

# SETTING
dir_path = "C:/workspace/SocialMovementSentiment/Benchmark/CrimeIncidentDataset/"
source_dataset_file = dir_path+"dataset.csv"
source_date_format = "%m/%d/%Y"
focus_from_date = "05/01/2020"
focus_to_date = "06/30/2020"


def get_blm_minesota(from_date, to_date):

    primary_dir_path = "C:/workspace/SocialMovementSentiment/dataset/blm_minesota/"
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

# FIXED DATA ISSUE
df['DATE'] = df['DATE'].astype('datetime64[ns]')

# FILTER
start_date = DateHelper.get_datetime64(focus_from_date, source_date_format)
end_date = DateHelper.get_datetime64(focus_to_date, source_date_format)
df = df.loc[(df['DATE'] >= start_date) & (df['DATE'] <= end_date)]
df_group = df[["DATE", "CASE NUMBER", "INCIDENT"]].groupby(["DATE", "INCIDENT"], as_index=False).count()
df_group["CASE NUMBER"] = df_group["CASE NUMBER"]*10

# GENERATE CHART TO COMPARE WITH MINESOTA DATA
primary_df = get_blm_minesota(start_date, end_date)
primary_df_group = primary_df[["tweet_created_date", "tweet_id"]].groupby(["tweet_created_date"], as_index=False).count()

# CREATE LINE PLOT FROM PRIMARY DATA

sns.color_palette("tab10")
sns.set_style("ticks")
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(25, 15))

# CREATE LINE PLOT FROM PRIMARY DATA
fig = sns.lineplot(y="tweet_id", x="tweet_created_date", data=primary_df_group, ax=ax, linewidth=2.5, color='#000000')
fig.set(ylabel="Totol Tweet Count", xlabel="Dates")
fig.set_xlabel(fig.get_xlabel(), fontsize=16)
fig.set_ylabel(fig.get_ylabel(), fontsize=16)

# CREATE SCATTER PLOT FROM SECONDARY DATA
fig = sns.lineplot(x="DATE", y="CASE NUMBER", hue="INCIDENT", palette="muted", data=df_group)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize='14')
plt.setp(ax.get_yticklabels(), rotation_mode="anchor",  fontsize='14')
plt.setp(fig.get_legend().get_texts(), fontsize='18')
plt.setp(fig.get_legend().get_title(), fontsize='22')

plt.title("Total #BLM Tweets v.s. Police Crime Reports")
plt.savefig("{}img/lineplot_comparison.png".format(dir_path))
plt.close()