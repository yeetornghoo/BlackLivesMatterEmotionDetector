import pandas as pd

from Controller.Validation import PreliminaryValidation

df = pd.read_csv("baseline-dataset.csv", sep=",")
PreliminaryValidation.run(df, "SemEval2019_Task3")