from Helper import AppConfigHelper
from Lexicon import StandardModel
import pandas as pd

model_folder = "Lexicon/DepecheMood/"
model_moods = ['afraid', 'amused', 'angry', 'annoyed', 'dontcare', 'happy', 'inspired', 'sad']
mood_score_model = ['afraid', 'afraid_score', 'amused', 'amused_score', 'angry', 'angry_score',
                    'annoyed', 'annoyed_score', 'dontcare', 'dontcare_score', 'happy', 'happy_score',
                    'inspired', 'inspired_score', 'sad', 'sad_score']
min_sentiment_score = float(AppConfigHelper.get_app_config_by_key("min_sentiment_score"))
selected_top_mood_name = 'dpm_sentiment'
selected_top_mood_count_name = 'dpm_sentiment_count'
selected_top_mood_score_name = 'dpm_sentiment_score'

# LEXICON FILE
depechemoodplus_lexicon_file = model_folder + "DepecheMood++/DepecheMood_english_token_full.tsv"


# SET TOP SCORE MOOD
def get_top_scores_moods(model, is_standard):

    mood_list = model_moods
    if is_standard:
        mood_list = StandardModel.model_moods

    mood_score_list = pd.Series({})

    sentence_top_mood = ""
    sentence_top_count = 0
    sentence_top_score = 0.0000
    l_min_sentiment_score = min_sentiment_score

    for mood in mood_list:

        mood_count = model.get(key="{}".format(mood))
        mood_score = model.get(key="{}_score".format(mood))

        if mood_score > l_min_sentiment_score:
            sentence_top_mood = mood
            sentence_top_count = mood_count
            sentence_top_score = mood_score
            l_min_sentiment_score = mood_score

    model = pd.Series({selected_top_mood_name: sentence_top_mood,
                       selected_top_mood_count_name: sentence_top_count,
                       selected_top_mood_score_name: sentence_top_score})

    return model


# SET DEPECHEMOOD MODEL
def set_model(afraid, afraid_score, amused, amused_score,
              angry, angry_score, annoyed, annoyed_score,
              dontcare, dontcare_score, happy, happy_score,
              inspired, inspired_score, sad, sad_score, is_standard):

    if not is_standard:

        model_dict = {
            'afraid': afraid, 'afraid_score': afraid_score, 'amused': amused, 'amused_score': amused_score,
            'angry': angry, 'angry_score': angry_score, 'annoyed': annoyed, 'annoyed_score': annoyed_score,
            'dontcare': dontcare, 'dontcare_score': dontcare_score, 'happy': happy, 'happy_score': happy_score,
            'inspired': inspired, 'inspired_score': inspired_score, 'sad': sad, 'sad_score': sad_score
        }

        model = pd.Series(model_dict, index=mood_score_model)

    else:

        std_anger = angry
        std_anger_score = angry_score
        std_disgust = annoyed
        std_disgust_score = annoyed_score
        std_fear = afraid
        std_fear_score = afraid_score
        std_joy = happy + amused
        std_joy_score = happy_score + amused_score
        std_sadness = sad
        std_sadness_score = sad_score
        std_surprise = inspired
        std_surprise_score = inspired_score

        model = StandardModel.set_standard_model(std_anger, std_anger_score, std_disgust, std_disgust_score,
                                                 std_fear, std_fear_score, std_joy, std_joy_score,
                                                 std_sadness, std_sadness_score, std_surprise, std_surprise_score)

    return model
