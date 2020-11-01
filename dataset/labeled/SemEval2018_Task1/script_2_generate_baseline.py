import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation
from Controller import FileController, DataSpellingCorrection, LogController, BaselineVizController

'''
# EXCLUDE UNWANTED MOOD
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df.drop(['ori_sentiment'], axis=1, inplace=True)
df = df[['sentiment', 'tweet_text']]

df = DataCleaning.run(df)
FileController.save_df_to_csv("baseline-dataset.csv", df)
DataAssess.run(df)

'''
df = pd.read_csv("baseline-dataset.csv", sep=",")
BaselineVizController.run(df)

LogController.log("Execution of 'script_2_generate_baseline.py' is completed.")