import pandas as pd
from Controller.Validation import PreliminaryValidation
dir_path = "C:/workspace/SocialMovementSentiment/dataset/labeled/"
df = pd.read_csv("baseline-dataset.csv", sep=",")
PreliminaryValidation.run(df, dir_path+"ISEAR")