import pandas as pd
from Controller import FileController, LogController
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection, DataAssess, DataNLP
from Controller import BaselineVizController, PlutchikStandardController

# EXCLUDE UNWANTED MOOD
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")

# RENAME MOOD
df = PlutchikStandardController.rename_mood(df)
df = PlutchikStandardController.get_standard(df)

# REFACTOR COLUMN
df.drop(['tweet', 'affect_dimension', 'intensity_score'], axis=1, inplace=True)
df = df[['sentiment', 'tweet_text']]

# FILTER WORD OF TWEET
df['ttl_tweet_text_word'] = df['tweet_text'].str.split().str.len()
df = df.loc[(df['ttl_tweet_text_word'] > 2)]
df.drop(columns=['ttl_tweet_text_word'], inplace=True)

# SAVE FILE
FileController.save_df_to_csv("baseline-dataset.csv", df)

# VISUALIZE BASELINE DATASET
df = pd.read_csv("baseline-dataset.csv", sep=",")
BaselineVizController.run(df)

# LOG
LogController.log("Execution of 'script_2_generate_baseline.py' is completed.")