import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Controller.Baseline import BaselineViz
from Controller.Visualization import BarPlotViz
from Controller.Visualization import BoxplotViz

sns.set_theme(style="whitegrid")

dir_path = "C:/workspace/SocialMovementSentiment/dataset/"
# BASELINE DATASET
df = pd.read_csv(dir_path+"master/baseline-dataset.csv", sep=",")

# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
BaselineViz.run(df, dir_path+"master/img/baseline/")

'''
df['word_count'] = df['tweet_text'].apply(lambda x: len(x.split()))


# GENERATE BOXPLOT BY EMOTION
fig, [[ax1, ax2], [ax3, ax4], [ax5, ax6], [ax7, ax8]] = plt.subplots(4, 2, figsize=(10, 14), squeeze=True) # X Y
fig.suptitle("")
fig.set_facecolor('red')
#fig.set_alpha(0.5)
BoxplotViz.generate_boxplot_wordcount_by_emotion(df, "joy", ax1)
BoxplotViz.generate_boxplot_wordcount_by_emotion(df, "sadness", ax2)
BoxplotViz.generate_boxplot_wordcount_by_emotion(df, "trust", ax3)
BoxplotViz.generate_boxplot_wordcount_by_emotion(df, "surprise", ax4)
BoxplotViz.generate_boxplot_wordcount_by_emotion(df, "anger", ax5)
BoxplotViz.generate_boxplot_wordcount_by_emotion(df, "fear", ax6)
BoxplotViz.generate_boxplot_wordcount_by_emotion(df, "anticipation", ax7)
BoxplotViz.generate_boxplot_wordcount_by_emotion(df, "disgust", ax8)
plt.savefig("img/boxplot_by_emotion.png", bbox_inches='tight', pad_inches=0.2, margin_inches="0.5", facecolor="white")
'''

'''
# WORD COUNT
import tokenize
token_lens = []

for txt in df.tweet_text:
  word_count = len(txt.split())
  token_lens.append(word_count)

sns_plot = sns.distplot(token_lens)
wc_fig = sns_plot.get_figure()
wc_fig.savefig("img/word_count.png", bbox_inches='tight', pad_inches=0.2, facecolor="white")
'''