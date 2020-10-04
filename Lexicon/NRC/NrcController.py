import pandas as pd
from ast import literal_eval
from Controller import LogController, FileController
from Helper import AppConfigHelper
from Helper.StringHelper import compare_str
from Lexicon import StandardModel
from Lexicon.NRC import NrcModel

# CONFIGURATION
dir_path = AppConfigHelper.get_app_config_by_key("app_dir")
mood_list = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']


# LOAD LEXICON FILE
def load_lexicon(filename):
    df = pd.read_csv(dir_path + filename, sep="\t")
    return df.values.tolist()


anger_lexicon = load_lexicon(NrcModel.anger_lexicon_file)
anticipation_lexicon = load_lexicon(NrcModel.anticipation_lexicon_file)
disgust_lexicon = load_lexicon(NrcModel.disgust_lexicon_file)
fear_lexicon = load_lexicon(NrcModel.fear_lexicon_file)
joy_lexicon = load_lexicon(NrcModel.joy_lexicon_file)
sadness_lexicon = load_lexicon(NrcModel.sadness_lexicon_file)
surprise_lexicon = load_lexicon(NrcModel.surprise_lexicon_file)
trust_lexicon = load_lexicon(NrcModel.trust_lexicon_file)


def get_word_sentiment_value(lexicon, word, mood_ttl_count, mood_ttl_score, mood):
    for s in lexicon:
        if compare_str(word, s[0]):
            mood_ttl_count += 1
            mood_ttl_score = mood_ttl_score + s[1]
            # print("--- M:{} W:{} NS:{} TC:{} TS:{})".format(mood, word, s[1], mood_ttl_count, mood_ttl_score))
            return mood_ttl_count, mood_ttl_score
    return mood_ttl_count, mood_ttl_score


def set_emotion_model(anger, anger_score, anticipation, anticipation_score,
                      disgust, disgust_score, fear, fear_score,
                      joy, joy_score, sadness, sadness_score,
                      surprise, surprise_score, trust, trust_score):

    model = {
        'anger': anger, 'anger_score': anger_score,
        'anticipation': anticipation, 'anticipation_score': anticipation_score,
        'disgust': disgust, 'disgust_score': disgust_score,
        'fear': fear, 'fear_score': fear_score,
        'joy': joy, 'joy_score': joy_score,
        'sadness': sadness, 'sadness_score': sadness_score,
        'surprise': surprise, 'surprise_score': surprise_score,
        'trust': trust, 'trust_score': trust_score
    }

    index = ['anger', 'anger_score', 'anticipation', 'anticipation_score', 'disgust', 'disgust_score',
             'fear', 'fear_score', 'joy', 'joy_score', 'sadness', 'sadness_score',
             'surprise', 'surprise_score', 'trust', 'trust_score']

    return pd.Series(model, index=index)


def get_sentence_mood(words, is_standard):

    # LOCAL VARIABLES
    anger = 0
    anger_score = 0.0000
    anticipation = 0
    anticipation_score = 0.0000
    disgust = 0
    disgust_score = 0.0000
    fear = 0
    fear_score = 0.0000
    joy = 0
    joy_score = 0.0000
    sadness = 0
    sadness_score = 0.0000
    surprise = 0
    surprise_score = 0.0000
    trust = 0
    trust_score = 0.0000

    # ITEMIZE THE WORDS
    for word in words:
        # GET DEFAULT SENTIMENT BY MOOD TYPE
        anger, anger_score = get_word_sentiment_value(anger_lexicon, word, anger, anger_score, "anger")
        disgust, disgust_score = get_word_sentiment_value(disgust_lexicon, word, disgust, disgust_score, "disgust")
        fear, fear_score = get_word_sentiment_value(fear_lexicon, word, fear, fear_score, "fear")
        joy, joy_score = get_word_sentiment_value(joy_lexicon, word, joy, joy_score, "joy")
        sadness, sadness_score = get_word_sentiment_value(sadness_lexicon, word, sadness, sadness_score, "sadness")
        surprise, surprise_score = get_word_sentiment_value(surprise_lexicon, word, surprise, surprise_score, "surprise")

        if not is_standard:
            anticipation, anticipation_score = get_word_sentiment_value(anticipation_lexicon, word, anticipation, anticipation_score, "anticipation")
            trust, trust_score = get_word_sentiment_value(trust_lexicon, word, trust, trust_score, "trust")

    # CREATE MOOD MODEL TO BE RETURN
    model = NrcModel.set_model(anger, anger_score, anticipation, anticipation_score,
                               disgust, disgust_score, fear, fear_score,
                               joy, joy_score, sadness, sadness_score,
                               surprise, surprise_score, trust, trust_score, is_standard)
    return model


def run(df, is_standard_model):

    LogController.log_h1("START NRC SENTIMENT ANALYSIS")
    iCount = 0

    for index, row in df.iterrows():

        iCount += 1
        print(iCount)

        token_word = StandardModel.get_unique_words(row)

        if len(pd.isnull(token_word)) > 0:

            emotion_info = get_sentence_mood(token_word, is_standard_model)
            df.loc[index, 'anger'] = emotion_info.get(key='anger')
            df.loc[index, 'anger_score'] = emotion_info.get(key='anger_score')
            df.loc[index, 'disgust'] = emotion_info.get(key='disgust')
            df.loc[index, 'disgust_score'] = emotion_info.get(key='disgust_score')
            df.loc[index, 'fear'] = emotion_info.get(key='fear')
            df.loc[index, 'fear_score'] = emotion_info.get(key='fear_score')
            df.loc[index, 'joy'] = emotion_info.get(key='joy')
            df.loc[index, 'joy_score'] = emotion_info.get(key='joy_score')
            df.loc[index, 'sadness'] = emotion_info.get(key='sadness')
            df.loc[index, 'sadness_score'] = emotion_info.get(key='sadness_score')
            df.loc[index, 'surprise'] = emotion_info.get(key='surprise')
            df.loc[index, 'surprise_score'] = emotion_info.get(key='surprise_score')

            if not is_standard_model:
                df.loc[index, 'anticipation'] = emotion_info.get(key='anticipation')
                df.loc[index, 'anticipation_score'] = emotion_info.get(key='anticipation_score')
                df.loc[index, 'trust'] = emotion_info.get(key='trust')
                df.loc[index, 'trust_score'] = emotion_info.get(key='trust_score')

            df.loc[index, 'nrc_sentiment'] = emotion_info.get(key='nrc_sentiment')
            df.loc[index, 'nrc_sentiment_count'] = emotion_info.get(key='nrc_sentiment_count')
            df.loc[index, 'nrc_sentiment_score'] = emotion_info.get(key='nrc_sentiment_score')

    FileController.save_df_to_csv("tmp/NRC-processed_dataset.csv", df)

    if is_standard_model:
        df.drop(['anger', 'anger_score', 'disgust', 'disgust_score',
                 'fear', 'fear_score', 'joy', 'joy_score', 'sadness', 'sadness_score',
                 'surprise', 'surprise_score'], axis=1, inplace=True)
    else:
        df.drop(['anger', 'anger_score', 'anticipation', 'anticipation_score', 'disgust', 'disgust_score',
                 'fear', 'fear_score', 'joy', 'joy_score', 'sadness', 'sadness_score',
                 'surprise', 'surprise_score', 'trust', 'trust_score'], axis=1, inplace=True)

    return df


def get_standard_model(df):
    mask = ((df['nrc_sentiment'] != "trust") & (df['nrc_sentiment'] != "anticipation"))
    df = df.loc[mask]
    return df
