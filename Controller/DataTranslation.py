from googletrans import Translator
from Controller import LogController
translator = Translator()


def run(df, lang):
    LogController.log_h1("START DATA TRANSLATION")
    LogController.log("Detect Language of The Tweets")
    df['tweet_langague'] = df['tweet_text'].apply(lambda x: get_sentence_language(str(x)))

    if lang != "":
        LogController.log("Return Tweets only for " + lang)
        filter_masking = df.tweet_langague == lang
        df = df[filter_masking]

    return df


def get_sentence_language(sentence):
    trs_obj = translator.detect(sentence)
    if trs_obj.confidence > 0.95:
        return trs_obj.lang
    return "UNKNOWN"
