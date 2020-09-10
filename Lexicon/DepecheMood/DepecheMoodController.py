import pandas as pd
from ast import literal_eval
from Controller import LogController, FileController
from Helper import AppConfigHelper
from Helper.StringHelper import compare_str
from Lexicon import StandardModel
from Lexicon.DepecheMood import DepecheMoodModel

# CONFIGURATION
dir_path = AppConfigHelper.get_app_config_by_key("app_dir")

# LOAD LEXICON FILE
selected_lexicon_df = pd.read_csv(dir_path + DepecheMoodModel.depechemoodplus_lexicon_file, sep="\t")
selected_lexicon = selected_lexicon_df.values.tolist()


def get_sentiment_score_value(mood_score_value, ttl_mood_count, ttl_mood_score, mood):
    if mood_score_value > 0.00:
        ttl_mood_count += 1
        ttl_mood_score = ttl_mood_score + mood_score_value
        #print("---- M:{} NS:{} TC:{} TS:{})".format(mood, mood_score_value, ttl_mood_count, ttl_mood_score))
    return ttl_mood_count, ttl_mood_score


def get_word_sentiment_value(word, sentence_model, is_standard_model):

    #print("-- W:{}".format(word))

    if not is_standard_model:

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
                afraid, afraid_score = get_sentiment_score_value(s[1], afraid, afraid_score, "afraid")
                amused, amused_score = get_sentiment_score_value(s[2], amused, amused_score, "amused")
                angry, angry_score = get_sentiment_score_value(s[3], angry, angry_score, "angry")
                annoyed, annoyed_score = get_sentiment_score_value(s[4], annoyed, annoyed_score, "annoyed")
                dontcare, dontcare_score = get_sentiment_score_value(s[5], dontcare, dontcare_score, "dontcare")
                happy, happy_score = get_sentiment_score_value(s[6], happy, happy_score, "happy")
                inspired, inspired_score = get_sentiment_score_value(s[7], inspired, inspired_score, "inspired")
                sad, sad_score = get_sentiment_score_value(s[8], sad, sad_score, "sad")
                break

        sentence_model = DepecheMoodModel.set_model(afraid, afraid_score, amused, amused_score,
                                                    angry, angry_score, annoyed, annoyed_score,
                                                    dontcare, dontcare_score, happy, happy_score,
                                                    inspired, inspired_score, sad, sad_score, is_standard_model)
    else:

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
                fear, fear_score = get_sentiment_score_value(s[1], fear, fear_score, "fear")
                #joy, joy_score = get_sentiment_score_value(s[2], joy, joy_score, "joy")
                anger, anger_score = get_sentiment_score_value(s[3], anger, anger_score, "anger")
                disgust, disgust_score = get_sentiment_score_value(s[4], disgust, disgust_score, "disgust")
                #dontcare, dontcare_score = get_sentiment_score_value(s[5], dontcare, dontcare_score, "dontcare")
                joy, joy_score = get_sentiment_score_value(s[6], joy, joy_score, "joy")
                surprise, surprise_score = get_sentiment_score_value(s[7], surprise, surprise_score, "surprise")
                sadness, sadness_score = get_sentiment_score_value(s[8], sadness, sadness_score, "sadness")
                break

        sentence_model = StandardModel.set_standard_model(anger, anger_score, disgust, disgust_score,
                                                          fear, fear_score, joy, joy_score,
                                                          sadness, sadness_score, surprise, surprise_score)


    return sentence_model


def get_sentence_mood(words, is_standard_model):
    # SET SENTENCE MODEL
    sentence_model = DepecheMoodModel.set_model(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, is_standard_model)

    # CONVERT TOKEN STRING TO LIST
    for word in words:
        sentence_model = get_word_sentiment_value(word, sentence_model, is_standard_model)

    # GET TOP SENTIMENT BY SCORE
    top_mood = DepecheMoodModel.get_top_scores_moods(sentence_model, is_standard_model)
    sentence_model = sentence_model.append(top_mood)
    return sentence_model


def run(df, is_standard_model):

    LogController.log_h1("START DEPECHEMOOD++ SENTIMENT ANALYSIS")
    iCount = 0

    for index, row in df.iterrows():
        iCount += 1
        # print(iCount)
        emotion_info = get_sentence_mood(StandardModel.get_unique_words(row), is_standard_model)

        if not is_standard_model:
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
        df.loc[index, DepecheMoodModel.selected_top_mood_name] = emotion_info.get(key=DepecheMoodModel.selected_top_mood_name)
        df.loc[index, DepecheMoodModel.selected_top_mood_count_name] = emotion_info.get(key=DepecheMoodModel.selected_top_mood_count_name)
        df.loc[index, DepecheMoodModel.selected_top_mood_score_name] = emotion_info.get(key=DepecheMoodModel.selected_top_mood_score_name)

        print("{}] {} >> Tweet: {} ({})".format(iCount,
                                           emotion_info.get(key=DepecheMoodModel.selected_top_mood_name),
                                           row['text'],
                                           emotion_info.get(key=DepecheMoodModel.selected_top_mood_score_name)))

    FileController.save_df_to_csv("tmp/dpm-processed_dataset.csv", df)

    if is_standard_model:
        df.drop(['anger', 'anger_score', 'disgust', 'disgust_score',
                 'fear', 'fear_score', 'joy', 'joy_score', 'sadness', 'sadness_score',
                 'surprise', 'surprise_score'], axis=1, inplace=True)
    else:
        df.drop(['afraid', 'afraid_score', 'amused', 'amused_score', 'angry', 'angry_score',
                 'annoyed', 'annoyed_score', 'dontcare', 'dontcare_score', 'happy', 'happy_score',
                 'inspired', 'inspired_score', 'sad', 'sad_score'], axis=1, inplace=True)

    return df
