import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

from Controller import LogController


def run(df, dir_path):

    LogController.log_h2("check esn sentiment")
    df_nrc = df[["text", "esn_sentiment"]].groupby(["esn_sentiment"], as_index=False).count()
    print(df_nrc)

    LogController.log_h2("check ori sentiment")
    df_ori = df[["text", "ori_sentiment"]].groupby(["ori_sentiment"], as_index=False).count()
    print(df_ori)

    df_tmp = df[["text", "ori_sentiment", "esn_sentiment"]].groupby(["ori_sentiment", "esn_sentiment"], as_index=False).count()

    # CREATE PLIT
    save_file_name = "bar_isear_vs_esn.png"
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots(figsize=(15, 6))
    sns.color_palette("tab10")
    fig = sns.barplot(x="ori_sentiment", y="text", data=df_ori, label="Total", color="y", alpha=0.2)
    sns.barplot(x="ori_sentiment", y="text", hue="esn_sentiment", data=df_tmp)
    plt.savefig("{}img/{}".format(dir_path, save_file_name))
    plt.close()

    LogController.log("chart {} is created".format(save_file_name))
