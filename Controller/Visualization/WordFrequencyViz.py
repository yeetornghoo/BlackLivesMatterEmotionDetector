from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


def generate_by_axessubplot(ax, wordlist):
    try:
        wordfreq = []

        for w in wordlist:
            word = [w, wordlist.count(w)]
            if word not in wordfreq:
                wordfreq.append(word)

        df = pd.DataFrame(wordfreq)
        df.rename(columns={0: "word", 1: "count"}, inplace=True)
        df.sort_values(by='count', ascending=False, inplace=True)
        df.iloc[:10].plot.bar(ax=ax, x='word', y='count', rot=90)
    except:
        print("An exception occurred")
