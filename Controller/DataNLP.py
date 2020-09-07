import pandas as pd
import stanza
stanza.download('en')
from Controller import LogController

allowed_upos = ['PUNCT', 'SYM']
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma', tokenize_no_ssplit=True)


def process_sentence(sentence, islemm):
    doc = nlp(sentence)
    words = []

    for i, sentence in enumerate(doc.sentences):
        for word in sentence.words:
            if word.upos not in allowed_upos:
                if islemm:
                    words.append(word.lemma.lower())
                else:
                    words.append(word.text.lower())

    return words


def run(df):
    LogController.log_h1("NATURAL LANGUAGE PROCESSING TASKS")
    LogController.log("tokenize AND CLEAN WORDS")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: process_sentence(str(x), False))
    df['lemma_tweet_text'] = df['tweet_text'].apply(lambda x: process_sentence(str(x), True))
    return df
