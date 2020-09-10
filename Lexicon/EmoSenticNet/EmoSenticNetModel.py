from Helper import AppConfigHelper
from Lexicon import StandardModel
import pandas as pd

model_folder = "Lexicon/EmoSenticNet/"
model_moods = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise']
mood_score_model = ['anger', 'anger_score', 'disgust', 'disgust_score', 'fear', 'fear_score',
                    'joy', 'joy_score', 'sadness', 'sadness_score', 'surprise', 'surprise_score']
selected_top_mood_name = 'esn_sentiment'
selected_top_mood_count_name = 'esn_sentiment_count'
selected_top_mood_score_name = 'esn_sentiment_score'


# SET TOP SCORE MOOD
def get_top_mood(model):
    model = StandardModel.get_top_mood_by_count(model, selected_top_mood_name, selected_top_mood_count_name)
    return model


# SET EMO SENTIC NET MODEL
def set_model(anger, anger_score, disgust, disgust_score,
              fear, fear_score, joy, joy_score, sadness, sadness_score,
              surprise, surprise_score):

    model = StandardModel.set_standard_model(anger, anger_score,
                                             disgust, disgust_score,
                                             fear, fear_score,
                                             joy, joy_score,
                                             sadness, sadness_score,
                                             surprise, surprise_score)
    return model
