import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

sns.set_theme(style="whitegrid")
plt.style.use('fivethirtyeight')


def generate_bellcurve(df, percentage, ax):

    min_value = round(df["sentiment_score"].min(), 4)
    max_value = round(df["sentiment_score"].max(), 4)
    std_value = round(df["sentiment_score"].std(), 4)
    mean_value = round(df["sentiment_score"].mean(), 4)
    q3_value = round(df["sentiment_score"].quantile(percentage), 4)

    # BELL CURVE
    x = np.arange(min_value, max_value, 0.001)
    y = norm.pdf(x, mean_value, std_value)
    ax.plot(x, y)

    # DECORATION
    ax.text((q3_value+0.1), 0.4, "{} (Upper Quantitle of {}%)".format(q3_value, (percentage * 100)))
    ax.text((mean_value-0.1), 0.05, "Mean: {}".format(mean_value), horizontalalignment='right')
    ax.axvline(x=q3_value, linestyle="--", linewidth=2, color="r")
    ax.axvline(x=mean_value, linestyle="--", linewidth=1, color="b")
    ax.axvspan(q3_value, max_value, hatch="/", alpha=0.1)
    ax.title.set_text('Bell Curve')
