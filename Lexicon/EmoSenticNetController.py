import string

import pandas as pd
from ast import literal_eval
from Controller import LogController, FileController
from Helper import AppConfigHelper

# SETTING
dir_path = AppConfigHelper.get_app_config_by_key("app_dir")
mood_list = ['anger', 'disgust', 'joy', 'sad', 'surprise', 'fear']

# LEXICON LIBRARY
selected_lexicon_path = "Lexicon/EmoSenticNet/"
lexicon_df = pd.read_csv(dir_path + selected_lexicon_path + "emosenticnet.csv", sep=",")
lexicon_list = lexicon_df.values.tolist()


def get_sentiment_value(word, emotion_obj):

    anger = emotion_obj.get(key='anger')
    disgust = emotion_obj.get(key='disgust')
    joy = emotion_obj.get(key='joy')
    sad = emotion_obj.get(key='sad')
    surprise = emotion_obj.get(key='surprise')
    fear = emotion_obj.get(key='fear')

    for s in lexicon_list:

        if word.strip() == str(s[0]).strip():
            anger = anger + int(s[1])
            disgust = disgust + int(s[2])
            joy = joy + int(s[3])
            sad = sad + int(s[4])
            surprise = surprise + int(s[5])
            fear = fear + int(s[6])

    emotion_info = {
        'anger': anger,
        'disgust': disgust,
        'joy': joy,
        'sad': sad,
        'surprise': surprise,
        'fear': fear
    }

    print(emotion_info)

    return pd.Series(emotion_info, index=mood_list)


def emotion_calculation(str_words):
    emotion_info = {
        'anger': 0, 'disgust': 0, 'joy': 0, 'sad': 0, 'surprise': 0, 'fear': 0
    }

    emotion_obj = pd.Series(emotion_info, index=mood_list)
    words = literal_eval(str_words)
    for word in words:
        emotion_obj = get_sentiment_value(word, emotion_obj)
    return emotion_obj


# START
def run(df):

    LogController.log_h1("START EMO SENTIC NET SENTIMENT ANALYSIS")
    iCount = 0

    for index, row in df.iterrows():
        iCount += 1
        print(iCount)

        emotion_info = emotion_calculation(row['lemma_tweet_text'])
        df.loc[index, 'anger'] = emotion_info.get(key='anger')
        df.loc[index, 'disgust'] = emotion_info.get(key='disgust')
        df.loc[index, 'joy'] = emotion_info.get(key='joy')
        df.loc[index, 'sad'] = emotion_info.get(key='sad')
        df.loc[index, 'surprise'] = emotion_info.get(key='surprise')
        df.loc[index, 'fear'] = emotion_info.get(key='fear')

        # CHECK ROW BEST SENTIMENT
        row_sentiment = ""
        row_sentiment_count = 0
        row_min_mood_count = 0

        for mood in mood_list:
            mood_count = emotion_info.get(key=mood)
            if mood_count > row_min_mood_count:
                row_sentiment = mood
                row_sentiment_count = mood_count
                row_min_mood_count = mood_count

        df.loc[index, 'esn_sentiment'] = row_sentiment
        df.loc[index, 'esn_sentiment_count'] = row_sentiment_count

    FileController.save_df_to_csv("tmp/esn-processed_dataset.csv", df)

    return df
