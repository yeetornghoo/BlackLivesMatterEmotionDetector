import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation, FileController, DataSpellingCorrection


# EXCLUDE UNWANTED MOOD
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df.drop(['ori_sentiment'], axis=1, inplace=True)
df = df.loc[(df['sentiment'] != "guilt") & (df['sentiment'] != "guit") & (df['sentiment'] != "shame")]
df = df[['sentiment', 'tweet_text']]
FileController.save_df_to_csv("baseline-dataset.csv", df)
DataAssess.run(df)