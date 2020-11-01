from Controller import LogController
import matplotlib.pyplot as plt

from Controller.Visualization.BarPlotViz import generate_barplot


def run(df):
    LogController.log_h1("START DATA ASSESS")

    LogController.log_h2("Show Dataframe head")
    print(df.head())
    LogController.log_h2("Show Dataframe info")
    print(df.info)
    LogController.log_h2("Show Dataframe describe")
    print(df.describe())
    LogController.log_h2("Show Dataframe number of null")
    print(df.isna().sum())


def viz(df):

    df_plot = df.groupby("sentiment").count()
    img_path = "img/data_access/0_dataset_sentiment_count.png"
    generate_barplot(df_plot, "Baseline Dataset", "Sentiment", "# Records", img_path)
