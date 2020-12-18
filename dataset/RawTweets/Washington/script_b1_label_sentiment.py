import pandas as pd

# NLP TOKEN
df = pd.read_csv("03-post-spelling-dataset.csv", sep=",")

print(df)
'''
df = DataNLP.run(df)
FileController.save_df_to_csv("04-post-nlp-dataset.csv", df)

# CHECK SENTIMENT
df = pd.read_csv("04-post-nlp-dataset.csv", sep=",")
df = NrcController.run(df)

# REMOVE COLUMNS
df.rename(columns={"nrc_sentiment": "sentiment",
                   "nrc_sentiment_count": "sentiment_count",
                   "nrc_sentiment_score": "sentiment_score"}, inplace=True)
FileController.save_df_to_csv("05-post-sentiment-dataset.csv", df)
'''