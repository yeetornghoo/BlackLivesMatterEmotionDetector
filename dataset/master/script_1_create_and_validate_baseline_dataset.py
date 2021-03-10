import pandas as pd
import seaborn as sns
from Controller import FileController
from Controller.Validation import PreliminaryValidation

sns.set_theme(style="whitegrid")

# SETTING
from Controller.Visualization import BarPlotViz, LiveTweetViz

dir_path = "C:/workspace/SocialMovementSentiment/dataset/"
# BASELINE DATASET


labeled_df = pd.read_csv(dir_path+"labeled/master/baseline-dataset.csv", sep=",")
print(labeled_df.groupby("sentiment").count())

unlabeled_df = pd.read_csv(dir_path+"unlabeled/master/baseline-dataset.csv", sep=",")
print(unlabeled_df.groupby("sentiment").count())

frames = [labeled_df, unlabeled_df]
df = pd.concat(frames)
df = df[["sentiment", "tweet_text"]]

print(df.groupby("sentiment").count())
FileController.save_df_to_csv(dir_path+"master/baseline-dataset.csv", df)


df = pd.read_csv(dir_path+"master/baseline-dataset.csv", sep=",")

# VALIDATE BY MACHINE LEARNING
#PreliminaryValidation.run(df, dir_path + "master")

# TWEET COUNT
img_path = dir_path+"master/img/final_tweet_count.png"
df_count = df.loc[:, ['sentiment', 'tweet_text']]
df_count = df_count.groupby("sentiment").count()
BarPlotViz.generate_barplot(df_count, "Master Training Dataset", "Emotion", "# of Tweets", img_path)

# WORD CLOUD
path = "C:/workspace/SocialMovementSentiment/dataset/master"
LiveTweetViz.generate_word_assessment_by_upos_type(df, "ADJ", path)
LiveTweetViz.generate_word_assessment_by_upos_type(df, "VERB", path)
LiveTweetViz.generate_word_assessment_by_upos_type(df, "NOUN", path)