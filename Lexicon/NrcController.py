import pandas as pd
from ast import literal_eval
from Controller import LogController, FileController
from Helper import AppConfigHelper

dir_path = AppConfigHelper.get_app_config_by_key("app_dir")
selected_lexicon_path = "Lexicon/nrc/"
mood_list = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
min_sentiment_score = float(AppConfigHelper.get_app_config_by_key("min_sentiment_score"))


def load_lexicon(lexicon_type, filename):
    lexicon_path = dir_path + selected_lexicon_path + "NRC-Emotion-Intensity-Lexicon-v1/OneFilePerEmotion/"
    df = pd.read_csv(lexicon_path + filename, sep="\t")
    return df.values.tolist()


anger_scores = load_lexicon("nrc", "anger-scores.txt")
anticipation_scores = load_lexicon("nrc", "anticipation-scores.txt")
disgust_scores = load_lexicon("nrc", "disgust-scores.txt")
fear_scores = load_lexicon("nrc", "fear-scores.txt")
joy_scores = load_lexicon("nrc", "joy-scores.txt")
sadness_scores = load_lexicon("nrc", "sadness-scores.txt")
surprise_scores = load_lexicon("nrc", "surprise-scores.txt")
trust_scores = load_lexicon("nrc", "trust-scores.txt")


def get_sentiment_value(mood, word):
    if mood == "anger":
        mood_scores = anger_scores
    elif mood == "anticipation":
        mood_scores = anticipation_scores
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
    elif mood == "trust":
        mood_scores = trust_scores

    for s in mood_scores:
        if word.strip() == s[0].strip():
            return True, s[1]

    return False, 0.0000


def emotion_calculation(str_words):
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

    words = literal_eval(str_words)

    # TODO: NOT SURE IF NEED TO COUNT SENTIMENT ONLY BY UNIQUE WORD OR REPEATED WORDS
    #used = set()
    #unique = [x for x in words if x not in used and (used.add(x) or True)]
    #for word in unique:

    for word in words:

        freq = words.count(word)

        # ANGER
        isFound, scoreValue = get_sentiment_value("anger", word)
        if isFound & (scoreValue > min_sentiment_score):
            anger = anger + freq
            anger_score = anger_score + scoreValue

        # ANTICIPATION
        isFound, scoreValue = get_sentiment_value("anticipation", word)
        if isFound & (scoreValue > min_sentiment_score):
            anticipation = anticipation + freq
            anticipation_score = anticipation_score + scoreValue

        # DISGUST
        isFound, scoreValue = get_sentiment_value("disgust", word)
        if isFound & (scoreValue > min_sentiment_score):
            disgust = disgust + freq
            disgust_score = disgust_score + scoreValue

        # FEAR
        isFound, scoreValue = get_sentiment_value("fear", word)
        if isFound & (scoreValue > min_sentiment_score):
            fear = fear + freq
            fear_score = fear_score + scoreValue

        # JOY
        isFound, scoreValue = get_sentiment_value("joy", word)
        if isFound & (scoreValue > min_sentiment_score):
            joy = joy + freq
            joy_score = joy_score +scoreValue

        # SADNESS
        isFound, scoreValue = get_sentiment_value("sadness", word)
        if isFound & (scoreValue > min_sentiment_score):
            sadness = sadness + freq
            sadness_score = sadness_score + scoreValue

        # SURPRISE
        isFound, scoreValue = get_sentiment_value("surprise", word)
        if isFound & (scoreValue > min_sentiment_score):
            surprise = surprise + freq
            surprise_score = surprise_score + scoreValue

        # TRUST
        isFound, scoreValue = get_sentiment_value("trust", word)
        if isFound & (scoreValue > min_sentiment_score):
            trust = trust + freq
            trust_score = trust_score + scoreValue

    emotion_info = {
        'anger': anger,
        'anger_score': anger_score,
        'anticipation': anticipation,
        'anticipation_score': anticipation_score,
        'disgust': disgust,
        'disgust_score': disgust_score,
        'fear': fear,
        'fear_score': fear_score,
        'joy': joy,
        'joy_score': joy_score,
        'sadness': sadness,
        'sadness_score': sadness_score,
        'surprise': surprise,
        'surprise_score': surprise_score,
        'trust': trust,
        'trust_score': trust_score
    }

    indexs = ['anger', 'anger_score', 'anticipation', 'anticipation_score', 'disgust', 'disgust_score',
              'fear', 'fear_score', 'joy', 'joy_score', 'sadness', 'sadness_score', 'surprise', 'surprise_score',
              'trust', 'trust_score']

    return pd.Series(emotion_info, index=indexs)


def run(df):

    LogController.log_h1("START NRC SENTIMENT ANALYSIS")
    iCount = 0

    for index, row in df.iterrows():
        iCount += 1
        print(iCount)

        emotion_info = emotion_calculation(row['tweet_text'])
        df.loc[index, 'anger'] = emotion_info.get(key='anger')
        df.loc[index, 'anger_score'] = emotion_info.get(key='anger_score')
        df.loc[index, 'anticipation'] = emotion_info.get(key='anticipation')
        df.loc[index, 'anticipation_score'] = emotion_info.get(key='anticipation_score')
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
        df.loc[index, 'trust'] = emotion_info.get(key='trust')
        df.loc[index, 'trust_score'] = emotion_info.get(key='trust_score')

        final_sentiment = ""
        final_sentiment_score = 0.0000
        l_sentiment_score = float(min_sentiment_score)

        for mood in mood_list:

            mood_score = emotion_info.get(key=mood+'_score')

            if mood_score > l_sentiment_score:
                final_sentiment = mood
                final_sentiment_score = mood_score
                l_sentiment_score = mood_score

        df.loc[index, 'nrc_sentiment'] = final_sentiment
        df.loc[index, 'nrc_sentiment_score'] = final_sentiment_score

    FileController.save_df_to_csv("tmp/nrc-processed_dataset.csv", df)

    return df
