import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# SETTING
from Controller import DataAssess, LogController
from Controller.Visualization.Accuracy import NrcReview, DepecheMoodReview

dir_path = "C:/workspace/SocialMovementSentiment/dataset/ISEAR/"
sentiment_dataset_file = "{}04-post-sentiment-False-ISEAR.txt".format(dir_path)

# LOAD SENTIMENT FILES
df = pd.read_csv(sentiment_dataset_file, sep=",")
DataAssess.run(df)

# FIXED guilt and guit
df.loc[df['ori_sentiment'] == 'guit', 'ori_sentiment'] = 'guilt'

'''
## ORIGINAL
LogController.log_h2("check isear original sentiment")
df_ori = df[["text", "ori_sentiment"]].groupby(["ori_sentiment"], as_index=False).count()
print(df_ori)

## NRC


## DEPECHEMOOD
LogController.log_h2("check dpm original sentiment")
df_dpm = df[["text", "dpm_sentiment"]].groupby(["dpm_sentiment"], as_index=False).count()
print(df_dpm)
'''

# REVIEW ORIGINAL AND NRC
NrcReview.run(df, dir_path)
DepecheMoodReview.run(df, dir_path)


'''
df_g = df[["text", "ori_sentiment", "nrc_sentiment", "dpm_sentiment",
           "esn_sentiment"]].groupby(["ori_sentiment", "nrc_sentiment", "dpm_sentiment",
                                      "esn_sentiment"], as_index=False).count()

print("------{}-----".format("ori_sentiment"))
print(df_g["ori_sentiment"].unique())

print("------{}-----".format("nrc_sentiment"))
print(df_g["nrc_sentiment"].unique())

print("------{}-----".format("dpm_sentiment"))
print(df_g["dpm_sentiment"].unique())

print("------{}-----".format("esn_sentiment"))
print(df_g["esn_sentiment"].unique())

sns.set_theme(style="whitegrid")
f, ax = plt.subplots(figsize=(15, 6))
# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="ori_sentiment", y="text", data=df_g, label="Orignal", color="b")

sns.lineplot(data=df_g, x="nrc_sentiment", y="text", palette="tab10", label="nrc_sentiment", linewidth=2.5)
sns.lineplot(data=df_g, x="dpm_sentiment", y="text", palette="tab10", label="nrc_sentiment", linewidth=2.5)
sns.lineplot(data=df_g, x="esn_sentiment", y="text", palette="tab10", label="nrc_sentiment", linewidth=2.5)

plt.savefig("{}img/_bar.png".format(dir_path))
plt.close()
'''