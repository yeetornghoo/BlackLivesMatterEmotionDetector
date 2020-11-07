import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import norm
from Controller import PlutchikStandardController, FileController
from Controller.Visualization import BellCurveViz, BoxplotViz


def update_message(str_input):
    str_input = str_input.replace('\n', ' ').replace('\r', '')
    return str_input


df = pd.read_csv("baseline-dataset.csv", sep=",")
print(len(df.index))
df['tweet_text'] = df['tweet_text'].apply(lambda x: update_message(str(x)))
print(len(df.index))
df = df[df['sentiment'].notna()]
print(len(df.index))
FileController.save_df_to_csv("tmp_baseline-dataset.csv", df)
