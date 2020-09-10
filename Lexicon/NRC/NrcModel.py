from Helper import AppConfigHelper
from Lexicon import StandardModel
import pandas as pd

model_folder = "Lexicon/NRC/NRC-Emotion-Intensity-Lexicon-v1/OneFilePerEmotion/"
model_moods = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
mood_score_model = ['anger', 'anger_score', 'disgust', 'disgust_score', 'fear', 'fear_score', 'joy', 'joy_score',
                    'sadness', 'sadness_score', 'surprise', 'surprise_score', 'anticipation', 'anticipation_score'
                    'trust', 'trust_score']
min_sentiment_score = float(AppConfigHelper.get_app_config_by_key("min_sentiment_score"))
selected_top_mood_name = 'nrc_sentiment'
selected_top_mood_count_name = 'nrc_sentiment_count'
selected_top_mood_score_name = 'nrc_sentiment_score'

# LEXICON FILE
anger_lexicon_file = model_folder + "anger-scores.txt"
anticipation_lexicon_file = model_folder + "anticipation-scores.txt"
disgust_lexicon_file = model_folder + "disgust-scores.txt"
fear_lexicon_file = model_folder + "fear-scores.txt"
joy_lexicon_file = model_folder + "joy-scores.txt"
sadness_lexicon_file = model_folder + "sadness-scores.txt"
surprise_lexicon_file = model_folder + "surprise-scores.txt"
trust_lexicon_file = model_folder + "trust-scores.txt"


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

    top_sentiment = pd.Series({selected_top_mood_name: sentence_top_mood,
                               selected_top_mood_count_name: sentence_top_count,
                               selected_top_mood_score_name: sentence_top_score})

    return top_sentiment


# SET NRC MODEL
def set_model(anger, anger_score, anticipation, anticipation_score,
              disgust, disgust_score, fear, fear_score,
              joy, joy_score, sadness, sadness_score,
              surprise, surprise_score, trust, trust_score, is_standard):

    model = StandardModel.set_standard_model(anger, anger_score, disgust, disgust_score,
                                             fear, fear_score, joy, joy_score,
                                             sadness, sadness_score, surprise, surprise_score)
    if not is_standard:
        additional_moods = pd.Series({'anticipation': anticipation,
                                      'anticipation_score': anticipation_score,
                                      'trust': trust,
                                      'trust_score': trust_score})
        model = model.append(additional_moods)

    # CHECK TOP 1 MODEL
    top_mood = get_top_scores_moods(model, is_standard)
    model = model.append(top_mood)

    return model
