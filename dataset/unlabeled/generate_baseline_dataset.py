import pandas as pd
import os
from Controller import FileController, LogController
from Controller.Baseline import BaselineViz

# SETTING
from Controller.Visualization import BarPlotViz

unlabeled_path = "C:/workspace/SocialMovementSentiment/dataset/unlabeled/"
label_dataset_folder = ["blm_baltimore", "blm_davideantonio", "blm_minnesota", "blm_washington"]
#label_dataset_folder = ["blm_washington"]
mood_perc = [["fear", 0.78], ["anger", 1], ["sadness", 1], ["trust", 0.68], ["joy", 0.90], ["surprise", 0.0], ["anticipation", 0.0], ["disgust", 0.0]]


# FILTER DATA BY PERCENTAGE
def filter_data_by_perc(df_input, out_path):
    df_out = pd.DataFrame()
    for mood, perc in mood_perc:
        df_tmp = BaselineViz.df_summary(df_input, mood, perc, out_path)
        df_out = df_out.append(df_tmp)
    return df_out


# LOOP DATASET
df = pd.DataFrame()
for folder_name in label_dataset_folder:

    folder_path = "{}{}/".format(unlabeled_path, folder_name)
    print("folder_path: {}".format(folder_path))
    os.chdir(folder_path)
    #exec(open('script_0_init.py').read())

    # PROCESS INVIDIUAL DATASET
    dataset_file_path = "{}/baseline-dataset.csv".format(folder_path)
    ds_tmp = pd.read_csv(dataset_file_path, sep=",")
    ds_tmp = ds_tmp[["sentiment", "sentiment_score", "tweet_text"]]

    LogController.log("Added {} with {} rows".format(folder_name, len(ds_tmp.index)))
    df = df.append(ds_tmp, ignore_index=True)

out_path = unlabeled_path + "master/img/baseline/"
df = filter_data_by_perc(df, out_path)


FileController.save_df_to_csv(unlabeled_path + "master/baseline-dataset.csv", df)

# TWEET COUNT
img_path = out_path+"../final_tweet_count.png"
df_count = df.loc[:, ['sentiment', 'tweet_text']]
df_count = df_count.groupby("sentiment").count()
BarPlotViz.generate_barplot(df_count, "EmoLex Labelled Dataset", "Emotion", "# of Tweets", img_path)
