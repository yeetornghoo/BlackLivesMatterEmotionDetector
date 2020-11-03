import string

import pandas as pd
from ast import literal_eval
from Controller import LogController, FileController
from Helper import AppConfigHelper

# TEST


dir_path = AppConfigHelper.get_app_config_by_key("app_dir")
selected_lexicon_path = "Lexicon/WordNetAffectEmotionLists/"
mood_list = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']
# min_sentiment_score = float(AppConfigHelper.get_app_config_by_key("min_sentiment_score"))


def load_lexicon(filename):
    lexicon_path = dir_path + selected_lexicon_path
    f = open(lexicon_path + filename, "r")
    return_list = []
    for _line in f:
        for _word in _line.split():
            if _word not in return_list:
                return_list.append(_word)
    return return_list


anger_scores = load_lexicon("anger.txt")
disgust_scores = load_lexicon("disgust.txt")
fear_scores = load_lexicon("fear.txt")
joy_scores = load_lexicon("joy.txt")
sadness_scores = load_lexicon("sadness.txt")
surprise_scores = load_lexicon("surprise.txt")


def get_sentiment_value(mood, word):

    if mood == "anger":
        mood_scores = anger_scores
    elif mood == "disgust":
        mood_scores = disgust_scores
    elif mood == "fear":
        mood_scores = fear_scores
    elif mood == "joy":
        mood_scores = joy_scores
    elif mood == "sadness":
        mood_scores = sadness_scores
    elif mood == "surprise":
        mood_scores = surprise_scores

    for s in mood_scores:
        if word.strip() == s[0].strip():
            return 1
    return 0


def emotion_calculation(str_words):
    anger = 0
    disgust = 0
    fear = 0
    joy = 0
    sadness = 0
    surprise = 0

    words = literal_eval(str_words)

    for word in words:

        for mood in mood_list:

            if get_sentiment_value(mood, word):
                if mood == "anger":
                    anger += 1
                elif mood == "disgust":
                    disgust += 1
                elif mood == "fear":
                    fear += 1
                elif mood == "joy":
                    joy += 1
                elif mood == "sadness":
                    sadness += 1
                elif mood == "surprise":
                    surprise += 1

    emotion_info = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'surprise': surprise
    }

    return pd.Series(emotion_info, index=['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise'])


def run(df):

    LogController.log_h1("START NRC SENTIMENT ANALYSIS")
    iCount = 0

    for index, row in df.iterrows():
        iCount += 1
        print(iCount)

        emotion_info = emotion_calculation(row['lemma_tweet_text'])
        df.loc[index, 'anger'] = emotion_info.get(key='anger')
        df.loc[index, 'disgust'] = emotion_info.get(key='disgust')
        df.loc[index, 'fear'] = emotion_info.get(key='fear')
        df.loc[index, 'joy'] = emotion_info.get(key='joy')
        df.loc[index, 'sadness'] = emotion_info.get(key='sadness')
        df.loc[index, 'surprise'] = emotion_info.get(key='surprise')

        final_sentiment = ""
        final_sentiment_count = 0
        min_mood_count = 0

        for mood in mood_list:
            mood_count = emotion_info.get(key=mood)
            if mood_count > min_mood_count:
                final_sentiment = mood
                final_sentiment_count = mood_count
                min_mood_count = mood_count

        df.loc[index, 'wna_sentiment'] = final_sentiment
        df.loc[index, 'wna_sentiment_count'] = final_sentiment_count

    FileController.save_df_to_csv("tmp/wna-processed_dataset.csv", df)

    return df
