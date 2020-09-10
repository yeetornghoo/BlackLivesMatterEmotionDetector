import string

import pandas as pd
from ast import literal_eval
from Controller import LogController, FileController
from Helper import AppConfigHelper

# SETTING
from Helper.StringHelper import compare_str
from Lexicon import StandardModel
from Lexicon.EmoSenticNet import EmoSenticNetModel

# CONFIGURATION
dir_path = AppConfigHelper.get_app_config_by_key("app_dir")

# LEXICON LIBRARY
selected_lexicon_df = pd.read_csv(dir_path + EmoSenticNetModel.model_folder + "emosenticnet.csv", sep=",")
selected_lexicon = selected_lexicon_df.values.tolist()


def get_sentiment_count_value(mood_count_value, ttl_mood_count, mood):
    if int(mood_count_value) > 0:
        ttl_mood_count = ttl_mood_count + mood_count_value
        #print("---- M:{} NS:{} TC:{}".format(mood, mood_count_value, ttl_mood_count))
    return ttl_mood_count


# SET EMOSENTICNET MODEL
def get_word_sentiment_value(word, sentence_model):

    anger = sentence_model.get(key='disgust')
    disgust = sentence_model.get(key='disgust')
    fear = sentence_model.get(key='fear')
    joy = sentence_model.get(key='joy')
    sadness = sentence_model.get(key='sadness')
    surprise = sentence_model.get(key='surprise')

    for s in selected_lexicon:
        if compare_str(word, str(s[0])):
            #print("-- W:{}".format(word))
            anger = get_sentiment_count_value(int(s[1]), anger, "anger")
            disgust = get_sentiment_count_value(int(s[2]), disgust, "disgust")
            joy = get_sentiment_count_value(int(s[3]), joy, "joy")
            sadness = get_sentiment_count_value(int(s[4]), sadness, "sadness")
            surprise = get_sentiment_count_value(int(s[5]), surprise, "surprise")
            fear = get_sentiment_count_value(int(s[6]), fear, "fear")

    sentence_model = EmoSenticNetModel.set_model(anger, 0.00, disgust, 0.00,
                                                 fear, 0.00, joy, 0.00, sadness, 0.00, surprise, 0.00)
    return sentence_model


def get_sentence_mood(words):

    # SET SENTENCE MODEL
    sentence_model = EmoSenticNetModel.set_model(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # CONVERT TOKEN STRING TO LIST
    for word in words:
        sentence_model = get_word_sentiment_value(word, sentence_model)

    # GET TOP SENTIMENT BY SCORE
    top_mood = EmoSenticNetModel.get_top_mood(sentence_model)
    sentence_model = sentence_model.append(top_mood)

    return sentence_model


def run(df):

    LogController.log_h1("START EMO SENTIC NET SENTIMENT ANALYSIS")

    iCount = 0

    for index, row in df.iterrows():
        iCount += 1

        emotion_info = get_sentence_mood(StandardModel.get_unique_words(row))

        df.loc[index, 'anger'] = emotion_info.get(key='anger')
        df.loc[index, 'disgust'] = emotion_info.get(key='disgust')
        df.loc[index, 'joy'] = emotion_info.get(key='joy')
        df.loc[index, 'sadness'] = emotion_info.get(key='sadness')
        df.loc[index, 'surprise'] = emotion_info.get(key='surprise')
        df.loc[index, 'fear'] = emotion_info.get(key='fear')

        # TOP
        df.loc[index, EmoSenticNetModel.selected_top_mood_name] = emotion_info.get(key=EmoSenticNetModel.selected_top_mood_name)
        df.loc[index, EmoSenticNetModel.selected_top_mood_count_name] = emotion_info.get(key=EmoSenticNetModel.selected_top_mood_count_name)

        print("{}] {} >> Tweet: {} ({})".format(iCount,
                                           emotion_info.get(key=EmoSenticNetModel.selected_top_mood_name),
                                           row['text'],
                                           emotion_info.get(key=EmoSenticNetModel.selected_top_mood_score_name)))

    FileController.save_df_to_csv("tmp/esn-processed_dataset.csv", df)
    df.drop(['anger', 'disgust', 'joy', 'sadness', 'surprise', 'fear'], axis=1, inplace=True)

    return df
