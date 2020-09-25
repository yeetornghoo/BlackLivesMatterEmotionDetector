from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


def generate_word_cloud(text, output_folder, file_name):

    wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='salmon', colormap='Pastel1',
                          collocations=False, max_words=300, stopwords=STOPWORDS).generate(text)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.savefig("{}{}_wordclould.png".format(output_folder, file_name))
    plt.close()