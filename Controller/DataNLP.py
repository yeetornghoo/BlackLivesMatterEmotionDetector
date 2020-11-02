import stanza
from Helper import StringHelper
from Controller import LogController
stanza.download('en')

allowed_upos = ['PUNCT', 'SYM']
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma', tokenize_no_ssplit=True)


# https://universaldependencies.org/u/pos/
def get_sentence_by_pos(sentence, upos_type):

    words = ""

    if not StringHelper.isEmpty(sentence):
        doc = nlp(sentence)

        for i, sentence in enumerate(doc.sentences):
            for word in sentence.words:
                if word.upos == upos_type:
                    words = words + "{} ".format(word.text.lower())

    return words


def process_sentence(sentence):

    if StringHelper.isEmpty(sentence):
        print("Excluded: {}".format(sentence))
        return ""

    doc = nlp(sentence)
    words = []

    for i, sentence in enumerate(doc.sentences):
        for word in sentence.words:
            if word.upos not in allowed_upos:
                words.append(word.text.lower())
                if not StringHelper.compare_str(word.text.lower(), word.lemma.lower()):
                    words.append(word.lemma.lower())

    return words


def run(df):
    LogController.log_h1("NATURAL LANGUAGE PROCESSING TASKS")

    LogController.log("tokenize AND CLEAN WORDS")
    df['final_tweet_text'] = df['tweet_text'].apply(lambda x: process_sentence(str(x)))

    return df
