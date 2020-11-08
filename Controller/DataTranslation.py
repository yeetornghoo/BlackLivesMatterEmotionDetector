from googletrans import Translator
from Controller import LogController
translator = Translator()


def get_sentence_language(sentence):

    trs_obj = translator.detect(sentence)
    if trs_obj.confidence > 0.95:
        return trs_obj.lang

    return "UNKNOWN"


def run(df, lang):

    if lang != "":

        try:

            LogController.log_h1("START DATA TRANSLATION")

            # GET TWEET LANGUAGE
            LogController.log("Detect Language of The Tweets")
            df['tweet_language'] = df['tweet_text'].apply(lambda x: get_sentence_language(str(x)))

            # FILTER LANGUAGE
            LogController.log("Return Tweets only for " + lang)
            filter_masking = df.tweet_language == lang
            df = df[filter_masking]
            df = df.drop(['tweet_language'], axis=1)

        except:
            print("DataTranslation > Something went wrong")

    return df
