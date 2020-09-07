import pandas as pd
import nltk
nltk.download('wordnet')
from Controller import DataAssess, FileController, LogController
from Lexicon import NrcController, DepecheMoodController
from ast import literal_eval
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

# LOAD DATASET
df = pd.read_csv("03-post-nlp-dataset.csv", sep=",")

def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]


df['tweet_text_lemmatized'] = df.tweet_text.apply(lemmatize_text)
df.drop(['text', 'tweet_langague'], axis=1, inplace=True)

print(df.head(10))

ttl_raw_words = []


def count_raw_words(df):
    ttl_raw_words = []

    for index, row in df.iterrows():
        words = literal_eval(row[0])

        for target_word in words:
            if target_word not in ttl_raw_words:
                ttl_raw_words.append(target_word)

    return ttl_raw_words

# NOT LEMMA
def check_nrc(df):

    lexicon_df = pd.read_csv("C:/workspace/SocialMovementSentiment/Lexicon/nrc/NRC-Emotion-Intensity-Lexicon-v1/NRC-Emotion-Intensity-Lexicon-v1.txt", sep="\t")
    lexicon_list = lexicon_df.values.tolist()

    for index, row in df.iterrows():
        words = literal_eval(row[0])
        for target_word in words:
            if target_word not in lexicon_list:
                print("FOUND:" + target_word)



#ttl_raw_words = count_raw_words(df)
#print(len(ttl_raw_words))

check_nrc(df)
