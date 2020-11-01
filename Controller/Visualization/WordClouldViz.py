from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


def generate_by_axessubplot(ax, text):
    wordcloud = generate_word_cloud_object(text, 100, 2000, 3000)
    if wordcloud is not None:
        ax.imshow(wordcloud)
        ax.axis('off')


def generate_word_cloud_object(text, max_words, width_value, height_value):
    if len(text.strip()) > 0:
        try:
            return WordCloud(width=width_value, height=height_value, background_color='white', max_words=max_words).generate(text)
        except:
            print("An exception occurred")


def generate_word_cloud(text, max_words, output_folder, file_name):
    try:
        wordcloud = generate_word_cloud_object(text, max_words, 3000, 2000)

        # plot the WordCloud image
        plt.figure(figsize=(16, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)

        plt.savefig("{}{}_wordclould.png".format(output_folder, file_name.lower()))
        plt.close()

    except:
        print("An exception occurred")
