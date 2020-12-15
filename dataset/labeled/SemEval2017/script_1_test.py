import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt

'''
# LOAD AND PREPARE DATASET
colnames=['id', 'tweet_text', 'sentiment', 'sentiment_score']
anger_df = pd.read_csv("dataset/anger-all.txt", sep="\t", names=colnames, header=None)
fear_df = pd.read_csv("dataset/fear-all.txt", sep="\t", names=colnames, header=None)
joy_df = pd.read_csv("dataset/joy-all.txt", sep="\t", names=colnames, header=None)
sadness_df = pd.read_csv("dataset/sadness-all.txt", sep="\t", names=colnames, header=None)

frames = [anger_df, fear_df, joy_df, sadness_df]
df = pd.concat(frames)
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