import pandas as pd
from Controller.Validation import QuickValidation

df = pd.read_csv("baseline-dataset.csv", sep=",")
df = df[df['sentiment'].notna()]
QuickValidation.run(df, "blm_washington")