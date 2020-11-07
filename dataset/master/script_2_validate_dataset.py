import pandas as pd
from Controller.Validation import QuickValidation


# SETTING
dir_path = "C:/workspace/SocialMovementSentiment/dataset/"

# BASELINE DATASET
df = pd.read_csv(dir_path+"master/baseline-dataset.csv", sep=",")

# VALIDATE BY MACHINE LEARNING
QuickValidation.run(df, "master")
