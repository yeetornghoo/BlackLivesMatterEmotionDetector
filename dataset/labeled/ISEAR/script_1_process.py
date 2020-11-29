import pandas as pd
from Controller import FileController, LogController
from Controller import DataCleaning, DataTranslation, DataSpellingCorrection

'''
# LOAD AND PREPARE DATASET
df = pd.read_csv("dataset/ISEAR.csv", sep=",", names=['sentiment', 'text', 'other'])
df['tweet_text'] = df['text']

# EXCLUDE NONE ENGLISH TEXT
df = DataTranslation.run(df, "en")
FileController.save_df_to_csv("01-post-translate-dataset.csv", df)
'''

# DATA CLEANING
df = pd.read_csv("01-post-translate-dataset.csv", sep=",")
print("AFTER TRAX: {}".format(len(df)))
df = DataCleaning.run(df)
FileController.save_df_to_csv("02-post-cleaning-dataset.csv", df)

print("AFTER CLEANING: {}".format(len(df)))

# SPELLING CORRECTION
df = pd.read_csv("02-post-cleaning-dataset.csv", sep=",")
df = DataSpellingCorrection.run(df)
FileController.save_df_to_csv("03-post-spelling-dataset.csv", df)

print("SPEL TRAX: {}".format(len(df)))

# LOG
LogController.log("Execution of 'script_1_process.py' is completed.")
