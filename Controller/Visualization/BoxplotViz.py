import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

sns.set_theme(style="whitegrid")
plt.style.use('fivethirtyeight')


def generate_boxplot(df, percentage, ax):

    q3_value = round(df["sentiment_score"].quantile(percentage), 4)

    # CREATE BOXPLOT
    green_diamond = dict(markerfacecolor='g', marker='D')
    ax.boxplot(df["sentiment_score"], vert=False, flierprops=green_diamond)

    # DECORATION
    ax.title.set_text('Box Plot')
    ax.axvline(x=q3_value, linestyle="--", linewidth=2, color="r")
    ax.text(q3_value + 0.1, 1.2, "upper quantitle of {}% ({})".format(percentage * 100, round(q3_value, 4)))
