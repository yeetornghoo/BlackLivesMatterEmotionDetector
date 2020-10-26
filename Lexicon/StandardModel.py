import pandas as pd
import numpy as np
from ast import literal_eval

# STANDARD MODEL
from Helper import StringHelper

model_moods = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']
mood_score_model = ['anger', 'anger_score', 'disgust', 'disgust_score', 'fear', 'fear_score', 'joy', 'joy_score',
                    'sadness', 'sadness_score', 'surprise', 'surprise_score']


def set_standard_model(
        anger, anger_score,
        disgust, disgust_score,
        fear, fear_score,
        joy, joy_score,
        sadness, sadness_score,
        surprise, surprise_score):

    emotion_score = {
        'anger': anger, 'anger_score': anger_score,
        'disgust': disgust, 'disgust_score': disgust_score,
        'fear': fear, 'fear_score': fear_score,
        'joy': joy, 'joy_score': joy_score,
        'sadness': sadness, 'sadness_score': sadness_score,
        'surprise': surprise, 'surprise_score': surprise_score,
    }

    return pd.Series(emotion_score, index=mood_score_model)


def get_top_mood_by_count(model, att_mood_name, att_mood_count_name):

    sentence_top_mood = ""
    sentence_top_count = 0
    l_min_sentiment_count = 0

    for mood in model_moods:
        mood_count = int(model.get(key="{}".format(mood)))
        #print("mood:{} : {} > {} ?".format(mood, mood_count, l_min_sentiment_count))
        if mood_count == l_min_sentiment_count:
            #print("----------SAME")
            sentence_top_mood = ""
            sentence_top_count = 0
        elif mood_count > l_min_sentiment_count:
            #print("---------LARGER")
            sentence_top_mood = mood
            sentence_top_count = mood_count
            l_min_sentiment_count = mood_count

    #print("TOP MOOD:" + str(sentence_top_mood))
    #print("TOO MOOD COUNT" + str(sentence_top_count))
    model = pd.Series({att_mood_name: sentence_top_mood, att_mood_count_name: sentence_top_count})

    return model


def get_unique_words(row):
    if not pd.isnull(row['final_tweet_text']):
        #lemma_form = literal_eval(row['lemma_tweet_text'])
        #stand_form = literal_eval(row['tweet_text'])
        final_tweet = literal_eval(row['final_tweet_text'])
        return list(set(final_tweet))
    return []
