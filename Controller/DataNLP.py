import pandas as pd
import stanza
stanza.download('en')
from Controller import LogController

allowed_upos = ['PUNCT', 'SYM']


def run(df):
    LogController.log_h1("NATURAL LANGUAGE PROCESSING TASKS")

    LogController.log("tokenize AND CLEAN WORDS")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: process_sentence(str(x)))

    return df


def process_sentence(sentence):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma', tokenize_no_ssplit=True)
    doc = nlp(sentence)
    words = []

    for i, sentence in enumerate(doc.sentences):
        for word in sentence.words:
            if word.upos not in allowed_upos:
                words.append(word.text)
                #if word.text != word.lemma:
                #    words.append(word.lemma)
                #else:
                #    words.append(word.text)

    return words
