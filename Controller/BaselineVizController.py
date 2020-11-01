import pandas as pd
import re
import matplotlib.pyplot as plt
from Controller import DataNLP
from Controller.Visualization.BarPlotViz import generate_barplot
from Controller.Visualization import WordClouldViz
from Controller.Visualization import WordFrequencyViz


def generate_count(df):
    df_plot = df.groupby("sentiment").count()
    img_path = "img/baseline/0_dataset_sentiment_count.png"
    generate_barplot(df_plot, "Baseline Dataset", "Sentiment", "# Records", img_path)


def generate_word_assessment_by_upos_type(df, upos_type):

    # GENERATE POS
    df['tweet_text_tmp'] = df['tweet_text'].apply(lambda x: DataNLP.get_sentence_by_pos(str(x), upos_type))

    # ASSESS BY MOOD
    mood_classes = df.sentiment.unique()

    for mood in mood_classes:

        mood_df = df.loc[(df['sentiment'] == mood)]
        text = ''.join(mood_df["tweet_text_tmp"].values.flatten())
        wordList = re.sub("[^\w]", " ", text).split()

        if len(wordList) > 0:

            fig, (ax1, ax2) = plt.subplots(1, 2)
            fig.suptitle("'{}' Word Visualization for '{}'".format(upos_type, mood))

            # GENERATE WORD FREQUENCY
            WordFrequencyViz.generate_by_axessubplot(ax1, wordList)

            # GENERATE WORD CLOUD
            WordClouldViz.generate_by_axessubplot(ax2, text)

            fig.tight_layout()
            img_path = "img/baseline/{}_{}_word_viz.png".format(upos_type, mood)
            plt.savefig(img_path.lower())

    plt.close()


def generate_word_assessment(df):
    generate_word_assessment_by_upos_type(df, "ADJ")
    generate_word_assessment_by_upos_type(df, "VERB")


def run(df):
    # CREATE SIMPLE COUNT BY SENTIMENT BAR PLOT
    generate_count(df)
    generate_word_assessment(df)
