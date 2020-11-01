import pandas as pd
from Controller import DataCleaning, DataAssess, DataTranslation, FileController, DataSpellingCorrection


# EXCLUDE UNWANTED MOOD
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")
df = DataCleaning.run(df)
FileController.save_df_to_csv("baseline-dataset.csv", df)
DataAssess.run(df)
