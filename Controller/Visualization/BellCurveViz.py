import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

sns.set_theme(style="whitegrid")
plt.style.use('fivethirtyeight')


def generate_bellcurve(df, class_name, percentage, img_path, ax):

    min_value = round(df["sentiment_score"].min(), 4)
    max_value = round(df["sentiment_score"].max(), 4)
    std_value = round(df["sentiment_score"].std(), 4)
    mean_value = round(df["sentiment_score"].mean(), 4)
    q3_value = round(df["sentiment_score"].quantile(percentage), 4)

    # BELL CURVE
    x = np.arange(min_value, max_value, 0.001)
    y = norm.pdf(x, mean_value, std_value)
    ax.plot(x, y)
    #ax.text(4, 0.2, "Total Record : {}".format(len(df.index)), fontsize=15, color='red')


    # PLOT
    plt.axvline(x=q3_value, linestyle="--", linewidth=2, color="r")
    plt.text(q3_value + 0.1, 0.4, "upper Quantitle of {}% ({})".format(percentage * 100, round(q3_value, 4)))
    plt.axvline(x=mean_value, linestyle="--", linewidth=2, color="r")
    plt.text(mean_value + 0.05, 0.1, "Mean: {}".format(mean_value))
    plt.axvspan(q3_value, max_value, hatch="/", alpha=0.1)

    # PLOT
    plt.title("Bell Curve of '{}'".format(class_name))
    #plt.savefig("{}{}_bell_curve.png".format(img_path, class_name))