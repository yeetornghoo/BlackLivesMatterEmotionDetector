from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


def generate_barplot(df, title, xLabel, yLabel, img_path):

    fig, ax = plt.subplots(figsize=(8, 6))
    df.plot.bar(ax=ax)
    plt.xticks(rotation=50)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.1f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 9), textcoords='offset points')
    plt.savefig(img_path)
    plt.close()
