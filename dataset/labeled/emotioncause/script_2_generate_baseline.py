import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation, FileController, DataSpellingCorrection, LogController
'''
# EXCLUDE UNWANTED MOOD
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("baseline-dataset.csv", df)
'''

df = pd.read_csv("baseline-dataset.csv", sep=",")
DataAssess.viz(df)


LogController.log("Execution of 'script_2_generate_baseline.py' is completed.")
