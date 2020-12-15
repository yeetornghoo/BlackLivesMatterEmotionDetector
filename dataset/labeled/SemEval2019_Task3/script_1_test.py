import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt

'''
df = pd.read_csv("dataset/train.txt", sep='\t', lineterminator='\r')
df["tweet_text"] = df["turn1"] + " " + df["turn2"] + " " + df["turn3"]
df.drop(['id', 'turn1', 'turn2', 'turn3'], axis=1, inplace=True)
'''

dir_path = "C:/workspace/SocialMovementSentiment/dataset/labeled/"
df = pd.read_csv("baseline-dataset.csv", sep=",")

fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(df.sentiment)
plt.xlabel("Number of tweets by score")
plt.xticks(rotation=50)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 9), textcoords='offset points')
plt.savefig("post-data_count.png")