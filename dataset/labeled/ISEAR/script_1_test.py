import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt

# LOAD AND PREPARE DATASET
df = pd.read_csv("dataset/ISEAR.csv", sep=",", names=['sentiment', 'text', 'other'])
df['tweet_text'] = df['text']

fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(df.sentiment)
plt.xlabel("Number of tweets by score")
plt.xticks(rotation=50)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 9), textcoords='offset points')
plt.savefig("data_count.png")