import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation
from Controller import FileController, DataSpellingCorrection, LogController, BaselineVizController

'''
# REFACTOR MOOD
def change_mood_name(ori_mood):
    p_mood = ori_mood
    if ori_mood == "sad":
        p_mood = "sadness"
    return p_mood
    

# EXCLUDE UNWANTED MOOD
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
#df.drop(['content', 'author', 'tweet_id'], axis=1, inplace=True)


# REFACTOR MOODS
df['sentiment'] = df['sentiment'].apply(lambda x: change_mood_name(str(x)))
df = df[['sentiment', 'tweet_text']]


# EXCLUDE UNWANTED MOOD
df = df.loc[(df['sentiment'] != "shame")]
            
            
df = DataCleaning.run(df)
FileController.save_df_to_csv("baseline-dataset.csv", df)
'''

df = pd.read_csv("baseline-dataset.csv", sep=",")
BaselineVizController.run(df)


LogController.log("Execution of 'script_2_generate_baseline.py' is completed.")