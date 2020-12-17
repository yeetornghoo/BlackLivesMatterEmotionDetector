import os
import pandas as pd
from Controller import FileController
from Controller.Baseline import BaselineViz
from Controller.Visualization import BarPlotViz

dir_path = "C:/workspace/SocialMovementSentiment/dataset/labeled/"
label_dataset_folder = ["emotioncause", "ISEAR", "SemEval2018_Task1", "SemEval2019_Task3"]

'''
# GENERATE BASELINE DATASET
for folder_name in label_dataset_folder:
    folder_path = "{}{}/".format(dir_path, folder_name)
    os.chdir(folder_path)
    exec(open('script_0_init.py').read())
'''

# COMBINE FINAL BASELINE DATASET
df = pd.DataFrame()
for folder_name in label_dataset_folder:
    baseline_ds_path = "{}{}/baseline-dataset.csv".format(dir_path, folder_name)
    df_tmp = pd.read_csv(baseline_ds_path, sep=",")
    df = df.append(df_tmp, ignore_index=True)

FileController.save_df_to_csv(dir_path+"master/baseline-dataset.csv", df)

# GENERATE VISUAL FOR THE LATEST BASELINE DATASET
out_path = dir_path+"master/img/baseline/"
#BaselineViz.run(df, out_path)

# TWEET COUNT
img_path = out_path+"../final_tweet_count.png"
df_count = df.loc[:, ['sentiment', 'tweet_text']]
df_count = df_count.groupby("sentiment").count()
BarPlotViz.generate_barplot(df_count, "Prelabelled Dataset", "Emotion", "# of Tweets", img_path)
