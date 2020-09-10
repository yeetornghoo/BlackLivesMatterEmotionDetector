import pandas as pd
import stanza
stanza.download('en')
from Controller import LogController

allowed_upos = ['PUNCT', 'SYM']
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma', tokenize_no_ssplit=True)

corr_df = pd.read_csv('C:/workspace/SocialMovementSentiment/dataset/_custome/correction.csv')


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


# SPELLING CORRECTION
def spelling_correction(df):
    for index, row in corr_df.iterrows():
        df["tweet_text"] = df["tweet_text"].str.replace(" {} ".format(row["from_text"]), " {} ".format(row["to_text"]))
    return df


def run(df):
    LogController.log_h1("NATURAL LANGUAGE PROCESSING TASKS")

    LogController.log("Spelling Correction")
    df = spelling_correction(df)

    LogController.log("tokenize AND CLEAN WORDS")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: process_sentence(str(x), False))
    df['lemma_tweet_text'] = df['tweet_text'].apply(lambda x: process_sentence(str(x), True))

    return df
