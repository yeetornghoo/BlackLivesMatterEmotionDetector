import pandas as pd
import re
import matplotlib.pyplot as plt
from Controller import LogController, DataNLP
from Controller.Visualization import BarPlotViz, WordClouldViz, BellCurveViz, BoxplotViz, WordFrequencyViz


def generate_count(df, out_path):
    df_plot = df.groupby("sentiment")["sentiment"].count()
    img_path = "{}0_dataset_sentiment_count.png".format(out_path)
    BarPlotViz.generate_barplot(df_plot, "Baseline Dataset", "Sentiment", "# Records", img_path)


def generate_word_assessment_by_upos_type(df, upos_type, out_path):

    LogController.log("processing {}...".format(upos_type))

    # GENERATE POS
    df['tweet_text_tmp'] = df['tweet_text'].apply(lambda x: DataNLP.get_sentence_by_pos(str(x), upos_type))

    # ASSESS BY MOOD
    mood_classes = df.sentiment.unique()

    for mood in mood_classes:

        mood_df = df.loc[(df['sentiment'] == mood)]
        text = ''.join(mood_df["tweet_text_tmp"].values.flatten())
        wordList = re.sub("[^\w]", " ", text).split()

        if len(wordList) > 0:

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
            fig.suptitle("'{}' Word Visualization for '{}'".format(upos_type, mood))

            # GENERATE WORD FREQUENCY
            WordFrequencyViz.generate_by_axessubplot(ax1, wordList)

            # GENERATE WORD CLOUD
            WordClouldViz.generate_by_axessubplot(ax2, text)

            fig.tight_layout()
            img_path = "{}{}_{}_word_viz.png".format(out_path, upos_type, mood)
            plt.savefig(img_path.lower())

    plt.close('all')


def generate_mood_viz(df, class_name, percentage, out_path):

    q3_value = df["sentiment_score"].quantile(percentage)
    df_q3 = df.loc[(df["sentiment_score"] >= q3_value)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle("Dataset Visualization by '{}' \n {} records for {} and above".format(class_name, len(df_q3.index), percentage))

    BellCurveViz.generate_bellcurve(df, percentage, ax1)
    BoxplotViz.generate_boxplot(df, percentage, ax2)
    plt.savefig("{}{}_bell_curve.png".format(out_path, class_name))
    plt.text(0.5, 0.5, "sssdfsfs", horizontalalignment='right')

    fig.clear()
    plt.close('all')


def df_summary(df, class_name, percentage, out_path):
    df_class = df.loc[(df["sentiment"] == class_name)]
    generate_mood_viz(df_class, class_name, percentage, out_path)


def generate_mood_assessment(df, out_path, min_perc):
    df_summary(df, "fear", min_perc, out_path)
    df_summary(df, "anger", min_perc, out_path)
    df_summary(df, "sadness", min_perc, out_path)
    df_summary(df, "trust", min_perc, out_path)
    df_summary(df, "joy", min_perc, out_path)
    df_summary(df, "surprise", min_perc, out_path)
    df_summary(df, "anticipation", min_perc, out_path)
    df_summary(df, "disgust", min_perc, out_path)


def generate_word_assessment(df, out_path):
    generate_word_assessment_by_upos_type(df, "ADJ", out_path)
    generate_word_assessment_by_upos_type(df, "VERB", out_path)


def run(df, out_path):

    LogController.log_h1("Visualize Baseline Dataset")

    # CREATE SIMPLE COUNT BY SENTIMENT BAR PLOT
    generate_count(df, out_path)
    #generate_word_assessment(df, out_path)


def run_mood(df, out_path, min_perc):

    run(df, out_path)
    generate_mood_assessment(df, out_path, min_perc)
