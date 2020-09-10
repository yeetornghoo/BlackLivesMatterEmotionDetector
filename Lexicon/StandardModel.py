import pandas as pd
# STANDARD MODEL

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




