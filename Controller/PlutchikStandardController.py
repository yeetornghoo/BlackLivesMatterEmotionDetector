from Controller import LogController
from Helper import StringHelper

moods_code = [["fear", 1], ["anger", 2], ["sadness", 3], ["joy", 4], ["surprise", 5], ["anticipation", 6], ["disgust", 7], ["trust", 8]]
moods = ['fear', 'anger', 'sadness', 'joy', 'surprise', 'anticipation', 'disgust', 'trust']
joy_mood_synonyms = ["happy", "happiness"]
sadness_mood_synonyms = ["sad"]
anger_mood_synonyms = ["angry"]
fear_mood_synonyms = ["worry"]
disgust_mood_synonyms = ["hate"]


def get_standard(df):

    LogController.log_h1("Filter data with Pluntchil's Standard")

    df = df.loc[(df['sentiment'].isin(moods))]
    df = df[df['sentiment'].notna()]

    return df


def rename_to_fear(from_mood):
    if from_mood in fear_mood_synonyms:
        return "fear"
    return from_mood


def rename_to_disgust(from_mood):
    if from_mood in disgust_mood_synonyms:
        return "disgust"
    return from_mood


def rename_to_anger(from_mood):
    if from_mood in anger_mood_synonyms:
        return "anger"
    return from_mood


def rename_to_joy(from_mood):
    if from_mood in joy_mood_synonyms:
        return "joy"
    return from_mood


def rename_to_sadness(from_mood):
    if from_mood in sadness_mood_synonyms:
        return "sadness"
    return from_mood


def rename_mood(df):

    LogController.log_h1("Rename the mood to Pluntchil's Standard")

    # TRIM SENTIMENT WHITE SPACE
    df['sentiment'] = df['sentiment'].apply(lambda x: StringHelper.trim_word(str(x)))

    # UPDATE MOOD
    df['sentiment'] = df['sentiment'].apply(lambda x: rename_to_joy(str(x)))
    df['sentiment'] = df['sentiment'].apply(lambda x: rename_to_sadness(str(x)))
    df['sentiment'] = df['sentiment'].apply(lambda x: rename_to_anger(str(x)))
    df['sentiment'] = df['sentiment'].apply(lambda x: rename_to_fear(str(x)))
    df['sentiment'] = df['sentiment'].apply(lambda x: rename_to_disgust(str(x)))
    return df
