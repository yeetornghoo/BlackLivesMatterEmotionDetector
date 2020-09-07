import pandas as pd
from ast import literal_eval
from Controller import LogController, FileController
from Helper import AppConfigHelper

dir_path = AppConfigHelper.get_app_config_by_key("app_dir")
selected_lexicon_path = "Lexicon/DepecheMood_v2.0/DepecheMood++/"
mood_list = ['AFRAID', 'AMUSED', 'ANGRY', 'ANNOYED', 'DONT_CARE', 'HAPPY', 'INSPIRED', 'SAD']
word_indexs = ['afraid', 'afraid_score', 'amused', 'amused_score', 'angry', 'angry_score',
               'annoyed', 'annoyed_score', 'dontcare', 'dontcare_score', 'happy', 'happy_score',
               'inspired', 'inspired_score', 'sad', 'sad_score']
min_sentiment_score = float(AppConfigHelper.get_app_config_by_key("min_sentiment_score"))

# GET LEXICON LIBRARY
def load_lexicon():
    filename = dir_path + selected_lexicon_path + "DepecheMood_english_token_full.tsv"
    df = pd.read_csv(filename, sep="\t")
    df_l = df.values.tolist()
    return df_l


mood_scores = load_lexicon()


def get_sentiment_value(word, emotion_obj):

    afraid = emotion_obj.get(key='afraid')
    afraid_score = emotion_obj.get(key='afraid_score')
    amused = emotion_obj.get(key='amused')
    amused_score = emotion_obj.get(key='amused_score')
    angry = emotion_obj.get(key='angry')
    angry_score = emotion_obj.get(key='angry_score')
    annoyed = emotion_obj.get(key='annoyed')
    annoyed_score = emotion_obj.get(key='annoyed_score')
    dontcare = emotion_obj.get(key='dontcare')
    dontcare_score = emotion_obj.get(key='dontcare_score')
    happy = emotion_obj.get(key='happy')
    happy_score = emotion_obj.get(key='happy_score')
    inspired = emotion_obj.get(key='inspired')
    inspired_score = emotion_obj.get(key='inspired_score')
    sad = emotion_obj.get(key='sad')
    sad_score = emotion_obj.get(key='sad_score')

    for s in mood_scores:
        if word.strip() == str(s[0]).strip():

            # AFRAID
            if s[1] > min_sentiment_score:
                afraid += 1
                afraid_score = afraid_score + s[1]

            # AMUSED
            if s[2] > min_sentiment_score:
                amused += 1
                amused_score = amused_score + s[2]

            # ANGRY
            if s[3] > min_sentiment_score:
                angry += 1
                angry_score = angry_score + s[3]

            # ANNOYED
            if s[4] > min_sentiment_score:
                annoyed += 1
                annoyed_score = annoyed_score + s[4]

            # DONT_CARE
            if s[5] > min_sentiment_score:
                dontcare += 1
                dontcare_score = dontcare_score + s[5]

            # HAPPY
            if s[6] > min_sentiment_score:
                happy += 1
                happy_score = happy_score + s[6]

            # INSPIRED
            if s[7] > min_sentiment_score:
                inspired += 1
                inspired_score = inspired_score + s[7]

            # SAD
            if s[8] > min_sentiment_score:
                sad += 1
                sad_score = sad_score + s[8]

    emotion_info = {
        'afraid': afraid,
        'afraid_score': afraid_score,
        'amused': amused,
        'amused_score': amused_score,
        'angry': angry,
        'angry_score': angry_score,
        'annoyed': annoyed,
        'annoyed_score': annoyed_score,
        'dontcare': dontcare,
        'dontcare_score': dontcare_score,
        'happy': happy,
        'happy_score': happy_score,
        'inspired': inspired,
        'inspired_score': inspired_score,
        'sad': sad,
        'sad_score': sad_score
    }

    #print(emotion_info)

    return pd.Series(emotion_info, index=word_indexs)


def emotion_calculation(str_words):

    emotion_info = {
        'afraid': 0, 'afraid_score': 0.0000,
        'amused': 0, 'amused_score': 0.0000,
        'angry': 0, 'angry_score': 0.0000,
        'annoyed': 0, 'annoyed_score': 0.0000,
        'dontcare': 0, 'dontcare_score': 0.0000,
        'happy': 0, 'happy_score': 0.0000,
        'inspired': 0, 'inspired_score': 0.0000,
        'sad': 0, 'sad_score': 0.0000
    }

    emotion_obj = pd.Series(emotion_info, index=word_indexs)

    # CONVERT TOKEN STRING TO LIST
    words = literal_eval(str_words)

    for word in words:
        freq = words.count(word)
        emotion_obj = get_sentiment_value(word, emotion_obj)

    return emotion_obj


def run(df):
    LogController.log_h1("START DEPECHEMOOD++ SENTIMENT ANALYSIS")
    iCount = 0


    for index, row in df.iterrows():
        iCount += 1
        print(iCount)

        emotion_info  = emotion_calculation(row['tweet_text'])
        df.loc[index, 'afraid'] = emotion_info.get(key='afraid')
        df.loc[index, 'afraid_score'] = emotion_info.get(key='afraid_score')
        df.loc[index, 'amused'] = emotion_info.get(key='amused')
        df.loc[index, 'amused_score'] = emotion_info.get(key='amused_score')
        df.loc[index, 'angry'] = emotion_info.get(key='angry')
        df.loc[index, 'angry_score'] = emotion_info.get(key='angry_score')
        df.loc[index, 'annoyed'] = emotion_info.get(key='annoyed')
        df.loc[index, 'annoyed_score'] = emotion_info.get(key='annoyed_score')
        df.loc[index, 'dontcare'] = emotion_info.get(key='dontcare')
        df.loc[index, 'dontcare_score'] = emotion_info.get(key='dontcare_score')
        df.loc[index, 'happy'] = emotion_info.get(key='happy')
        df.loc[index, 'happy_score'] = emotion_info.get(key='happy_score')
        df.loc[index, 'inspired'] = emotion_info.get(key='inspired')
        df.loc[index, 'inspired_score'] = emotion_info.get(key='inspired_score')
        df.loc[index, 'sad'] = emotion_info.get(key='sad')
        df.loc[index, 'sad_score'] = emotion_info.get(key='sad_score')

        final_sentiment = ""
        final_sentiment_score = 0.0000
        l_sentiment_score = float(min_sentiment_score)

        for mood in mood_list:
            selected_mood = mood.lower()
            mood_score_name = ("{}_score".format(selected_mood.replace("_", ""))).strip()
            mood_score = emotion_info.get(key=mood_score_name)

            if mood_score > l_sentiment_score:
                final_sentiment = selected_mood
                final_sentiment_score = mood_score
                l_sentiment_score = mood_score

        df.loc[index, 'dpm_sentiment'] = final_sentiment
        df.loc[index, 'dpm_sentiment_score'] = final_sentiment_score

    FileController.save_df_to_csv("tmp/dpm-processed_dataset.csv", df)

    return df
