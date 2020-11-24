import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt

# LOAD AND PREPARE DATASET
# LOAD AND PREPARE DATASET
anger_df = pd.read_csv("dataset/EI-reg/training/EI-reg-En-anger-train.txt", sep="\t")
anger_df["sentiment"] = "anger"

fear_df = pd.read_csv("dataset/EI-reg/training/EI-reg-En-fear-train.txt", sep="\t")
fear_df["sentiment"] = "fear"

joy_df = pd.read_csv("dataset/EI-reg/training/EI-reg-En-joy-train.txt", sep="\t")
joy_df["sentiment"] = "joy"

sadness_df = pd.read_csv("dataset/EI-reg/training/EI-reg-En-sadness-train.txt", sep="\t")
sadness_df["sentiment"] = "sadness"

frames = [anger_df, fear_df, joy_df, sadness_df]
df = pd.concat(frames)

df['tweet_text'] = df['Tweet']
df.rename(columns={"Tweet": "tweet", "Affect Dimension": "affect_dimension", "Intensity Score": "intensity_score"}, inplace=True)
#DataAssess.run(df)

fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(df.sentiment)
plt.xlabel("Number of tweets by score")
plt.xticks(rotation=50)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 9), textcoords='offset points')
plt.savefig("data_count.png")