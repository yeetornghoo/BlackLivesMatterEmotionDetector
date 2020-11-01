import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation, FileController, DataSpellingCorrection, LogController


# REFACTOR MOOD
def change_mood_name(ori_mood):

    p_mood = ori_mood

    if ori_mood == "angry":
        p_mood = "anger"
    elif ori_mood == "happiness":
        p_mood = "joy"
    elif ori_mood == "hate":
        p_mood = "disgust"

    return p_mood


# EXCLUDE UNWANTED MOOD
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df.drop(['ori_sentiment'], axis=1, inplace=True)

# REFACTOR MOODS
df['sentiment'] = df['sentiment'].apply(lambda x: change_mood_name(str(x)))

df = df[['sentiment', 'tweet_text']]
df = df.loc[(df['sentiment'] != "others")]
FileController.save_df_to_csv("baseline-dataset.csv", df)
DataAssess.run(df)


LogController.log("Execution of 'script_2_generate_baseline.py' is completed.")
