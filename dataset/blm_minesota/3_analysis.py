import pandas as pd

from Controller import DataAssess

df = pd.read_csv("04-post-sentiment-dataset.csv", sep=",")
DataAssess.run(df)


