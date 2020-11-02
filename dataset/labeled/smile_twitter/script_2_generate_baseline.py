import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation, FileController
from Controller import DataSpellingCorrection, LogController, BaselineVizController
from Controller import PlutchikStandardController

# EXCLUDE UNWANTED MOOD
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")

# RENAME MOOD
df = PlutchikStandardController.rename_mood(df)
df = PlutchikStandardController.get_standard(df)

# REFACTOR COLUMN
df.drop(['content', 'tweet_id'], axis=1, inplace=True)
df = df[['sentiment', 'tweet_text']]

# SAVE FILE
FileController.save_df_to_csv("baseline-dataset.csv", df)

# VISUALIZE BASELINE DATASET
df = pd.read_csv("baseline-dataset.csv", sep=",")
BaselineVizController.run(df)

# LOG
LogController.log("Execution of 'script_2_generate_baseline.py' is completed.")
