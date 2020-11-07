import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import norm
from Controller import PlutchikStandardController, FileController
from Controller.Baseline import BaselineViz
from Controller.Visualization import BellCurveViz, BoxplotViz


def update_message(str_input):
    str_input = str_input.replace('\n', ' ').replace('\r', '')
    return str_input


df = pd.read_csv("baseline-dataset.csv", sep=",")
df = df[df['sentiment'].notna()]
df['tweet_text'] = df['tweet_text'].apply(lambda x: update_message(str(x)))
print(len(df.index))

out_path="total"

#BaselineViz.df_summary(df, "fear", min_perc, out_path)
#BaselineViz.df_summary(df, "anger", min_perc, out_path)
#BaselineViz.df_summary(df, "sadness", min_perc, out_path)
#BaselineViz.df_summary(df, "joy", min_perc, out_path)

BaselineViz.df_summary(df, "anticipation", 0.0, out_path)
BaselineViz.df_summary(df, "disgust", 0.3, out_path)
BaselineViz.df_summary(df, "trust", 0.68, out_path)
BaselineViz.df_summary(df, "surprise", 0.0, out_path)


#FileController.save_df_to_csv("tmp_baseline-dataset.csv", df)
