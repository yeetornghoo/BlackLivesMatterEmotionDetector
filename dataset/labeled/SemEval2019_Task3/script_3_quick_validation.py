import pandas as pd

from Controller.Validation import QuickValidation

df = pd.read_csv("baseline-dataset.csv", sep=",")
QuickValidation.run(df, "SemEval2019_Task3")