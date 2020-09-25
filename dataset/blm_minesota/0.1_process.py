import pandas as pd
import stanza
from collections import Counter

from Controller.Visualization import WordClouldViz
from Helper import StringHelper

#SETTING
stanza.download('en')
nlp = stanza.Pipeline(lang='en', processors='pos,tokenize', tokenize_no_ssplit=True)

# LOAD DATA FROM DATASET
file_name = "dataset.csv"
cleaned_df = pd.read_csv("04-post-sentiment-False-"+file_name, sep=",")


propn_words = []
noun_words = []
adj_words = []
verb_words = []

iCount = 0
for index, row in cleaned_df.iterrows():
    doc = nlp(row["text"])
    iCount += 1

    for i, sentence in enumerate(doc.sentences):
        for word in sentence.words:
            if StringHelper.compare_str(word.upos, "PROPN"):
                propn_words.append(word.text)
            elif StringHelper.compare_str(word.upos, "NOUN"):
                noun_words.append(word.text)
            elif StringHelper.compare_str(word.upos, "ADJ"):
                adj_words.append(word.text)
            elif StringHelper.compare_str(word.upos, "VERB"):
                verb_words.append(word.text)


def create_wordcloud(obj, filename):
    obj_dict = dict(Counter(obj))
    texts = ""

    for item in obj_dict.items():
        texts = texts + " " + item[0]

    WordClouldViz.generate_word_cloud(texts, "img/", filename)


create_wordcloud(propn_words, "propn")
create_wordcloud(noun_words, "noun")
create_wordcloud(adj_words, "adj")
create_wordcloud(verb_words, "verb")
