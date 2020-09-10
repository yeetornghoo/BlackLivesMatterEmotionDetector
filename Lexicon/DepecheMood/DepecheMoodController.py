import pandas as pd
from ast import literal_eval
from Controller import LogController, FileController
from Helper import AppConfigHelper
from Helper.StringHelper import compare_str
from Lexicon import StandardModel
from Lexicon.DepecheMood import DepecheMoodModel

# CONFIGURATION
dir_path = AppConfigHelper.get_app_config_by_key("app_dir")
selected_lexicon_path = "Lexicon/DepecheMood/DepecheMood++/"
mood_list = ['AFRAID', 'AMUSED', 'ANGRY', 'ANNOYED', 'DONT_CARE', 'HAPPY', 'INSPIRED', 'SAD']
word_indexs = ['afraid', 'afraid_score', 'amused', 'amused_score', 'angry', 'angry_score',
               'annoyed', 'annoyed_score', 'dontcare', 'dontcare_score', 'happy', 'happy_score',
               'inspired', 'inspired_score', 'sad', 'sad_score']

# LOAD LEXICON FILE
def load_lexicon(filename):
    df = pd.read_csv(dir_path + filename, sep="\t")
    df_l = df.values.tolist()
    return df_l


selected_lexicon = load_lexicon(DepecheMoodModel.depechemoodplus_lexicon_file)


def get_depechemood_value(mood_score_value, ttl_mood_count, ttl_mood_score):
    if mood_score_value > 0.00:
        ttl_mood_count += 1
        ttl_mood_score = ttl_mood_score + mood_score_value

    return ttl_mood_count, ttl_mood_score


def get_word_sentiment_value(word, sentence_model, is_standard):

    if not is_standard:

        afraid = sentence_model.get(key='afraid')
        afraid_score = sentence_model.get(key='afraid_score')
        amused = sentence_model.get(key='amused')
        amused_score = sentence_model.get(key='amused_score')
        angry = sentence_model.get(key='angry')
        angry_score = sentence_model.get(key='angry_score')
        annoyed = sentence_model.get(key='annoyed')
        annoyed_score = sentence_model.get(key='annoyed_score')
        dontcare = sentence_model.get(key='dontcare')
        dontcare_score = sentence_model.get(key='dontcare_score')
        happy = sentence_model.get(key='happy')
        happy_score = sentence_model.get(key='happy_score')
        inspired = sentence_model.get(key='inspired')
        inspired_score = sentence_model.get(key='inspired_score')
        sad = sentence_model.get(key='sad')
        sad_score = sentence_model.get(key='sad_score')

        for s in selected_lexicon:
            if compare_str(word, str(s[0])):
                afraid, afraid_score = get_depechemood_value(s[1], afraid, afraid_score)
                amused, amused_score = get_depechemood_value(s[2], amused, amused_score)
                angry, angry_score = get_depechemood_value(s[3], angry, angry_score)
                annoyed, annoyed_score = get_depechemood_value(s[4], annoyed, annoyed_score)
                dontcare, dontcare_score = get_depechemood_value(s[5], dontcare, dontcare_score)
                happy, happy_score = get_depechemood_value(s[6], happy, happy_score)
                inspired, inspired_score = get_depechemood_value(s[7], inspired, inspired_score)
                sad, sad_score = get_depechemood_value(s[8], sad, sad_score)
                break

        sentence_model = DepecheMoodModel.set_model(afraid, afraid_score, amused, amused_score,
                                                    angry, angry_score, annoyed, annoyed_score,
                                                    dontcare, dontcare_score, happy, happy_score,
                                                    inspired, inspired_score, sad, sad_score, is_standard)
    else:
        mood_score_model = ['anger', 'anger_score', 'disgust', 'disgust_score', 'fear', 'fear_score', 'joy',
                            'joy_score',
                            'sadness', 'sadness_score', 'surprise', 'surprise_score']

        anger = sentence_model.get(key='anger')
        anger_score = sentence_model.get(key='anger_score')
        disgust = sentence_model.get(key='disgust')
        disgust_score = sentence_model.get(key='disgust_score')
        fear = sentence_model.get(key='fear')
        fear_score = sentence_model.get(key='fear_score')
        joy = sentence_model.get(key='joy')
        joy_score = sentence_model.get(key='joy_score')
        sadness = sentence_model.get(key='sadness')
        sadness_score = sentence_model.get(key='sadness_score')
        surprise = sentence_model.get(key='surprise')
        surprise_score = sentence_model.get(key='surprise_score')

        for s in selected_lexicon:
            if compare_str(word, str(s[0])):
                fear, fear_score = get_depechemood_value(s[1], fear, fear_score)
                #joy, joy_score = get_depechemood_value(s[2], joy, joy_score)
                anger, anger_score = get_depechemood_value(s[3], anger, anger_score)
                disgust, disgust_score = get_depechemood_value(s[4], disgust, disgust_score)
                #dontcare, dontcare_score = get_depechemood_value(s[5], dontcare, dontcare_score)
                joy, joy_score = get_depechemood_value(s[6], joy, joy_score)
                surprise, surprise_score = get_depechemood_value(s[7], surprise, surprise_score)
                sadness, sadness_score = get_depechemood_value(s[8], sadness, sadness_score)
                break

        sentence_model = StandardModel.set_standard_model(anger, anger_score, disgust, disgust_score,
                                                          fear, fear_score, joy, joy_score,
                                                          sadness, sadness_score, surprise, surprise_score)

    return sentence_model


def get_sentence_mood(sentence, is_standard):
    # SET SENTENCE MODEL
    sentence_model = DepecheMoodModel.set_model(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, is_standard)

    # CONVERT TOKEN STRING TO LIST
    words = literal_eval(sentence)
    for word in words:
        sentence_model = get_word_sentiment_value(word, sentence_model, is_standard)

    top_mood = DepecheMoodModel.get_top_scores_moods(sentence_model, is_standard)
    sentence_model = sentence_model.append(top_mood)
    return sentence_model


def run(df, is_standard):

    LogController.log_h1("START DEPECHEMOOD++ SENTIMENT ANALYSIS")
    iCount = 0

    for index, row in df.iterrows():
        iCount += 1
        print(iCount)
        emotion_info = get_sentence_mood(row['lemma_tweet_text'], is_standard)

        if not is_standard:
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

        else:
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

        # TOP
        df.loc[index, 'dpm_sentiment'] = emotion_info.get(key='dpm_sentiment')
        df.loc[index, 'dpm_sentiment_count'] = emotion_info.get(key='dpm_sentiment_count')
        df.loc[index, 'dpm_sentiment_score'] = emotion_info.get(key='dpm_sentiment_score')

    FileController.save_df_to_csv("tmp/dpm-processed_dataset.csv", df)

    if is_standard:
        df.drop(['anger', 'anger_score', 'disgust', 'disgust_score',
                 'fear', 'fear_score', 'joy', 'joy_score', 'sadness', 'sadness_score',
                 'surprise', 'surprise_score'], axis=1, inplace=True)
    else:
        df.drop(['afraid', 'afraid_score', 'amused', 'amused_score', 'angry', 'angry_score',
                 'annoyed', 'annoyed_score', 'dontcare', 'dontcare_score', 'happy', 'happy_score',
                 'inspired', 'inspired_score', 'sad', 'sad_score'], axis=1, inplace=True)

    return df
