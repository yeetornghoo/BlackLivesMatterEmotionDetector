from ast import literal_eval

import pandas as pd
import stanza

from Controller import LogController

# DOWNLOAD LIBRARY
stanza.download('en')

# CONFIGURATION
allowed_upos = ['PUNCT', 'SYM']

# ------------------------------------------------
# MASTER FUNCTION
# ------------------------------------------------


# MASTER: LOAD DATASET AND PROCESS
def master_count_unique_word(master_df):
    ttl_dataset_words = []
    for index, row in master_df.iterrows():
        words = literal_eval(row["tweet_text"])
        for word in words:
            target_word = word.lower()
            if target_word not in ttl_dataset_words:
                ttl_dataset_words.append(target_word)

    LogController.log("TOTAL UNIQUE WORDS IN DATASET IS {}".format(len(ttl_dataset_words)))


# ------------------------------------------------
# CHECK NORMAL WORD MATCH FUNCTION
# ------------------------------------------------

def normal_word_match_check(master_df, lexicon_obj):
    unique_n_words = []
    for index, row in master_df.iterrows():
        words = literal_eval(row["tweet_text"])
        for word in words:
            target_word = word.lower().strip()
            if target_word in lexicon_obj:
                if target_word not in unique_n_words:
                    unique_n_words.append(target_word)
    LogController.log("TOTAL UNIQUE WORDS IN STANDARD FORM IS {}".format(len(unique_n_words)))

# ------------------------------------------------
# CHECK LEMMATIZED WORD MATCH FUNCTION
# ------------------------------------------------


def lemma_word_match_check(master_df, lexicon_obj):
    unique_l_words = []
    for index, row in master_df.iterrows():
        words = literal_eval(row["lemma_tweet_text"])
        for word in words:
            target_word = word.lower().strip()
            if target_word in lexicon_obj:
                if target_word not in unique_l_words:
                    unique_l_words.append(target_word)
    LogController.log("TOTAL UNIQUE WORDS IN LEMMAIZED FORM IS {}".format(len(unique_l_words)))


# RUN MASTER ------------------------------------------
LogController.log_h1("CHECK DATASET SIZE")
df = pd.read_csv("03-post-nlp-dataset.csv", sep=",")
master_count_unique_word(df)


# RUN NORMAL WORDS DISTINCT COUNT ---------------------

# --- load lexicon library
dir_path = "C:/workspace/SocialMovementSentiment/Lexicon/"
nrc_folder = "nrc/NRC-Emotion-Intensity-Lexicon-v1/"
lexicon_df = pd.read_csv(dir_path + nrc_folder + "NRC-Emotion-Intensity-Lexicon-v1.txt", sep="\t")
lexicon_df['word'] = lexicon_df['word'].apply(lambda x: str(x).lower())
lexicon_df.drop(['emotion', 'emotion-intensity-score'], axis=1, inplace=True)
lexicon_list = lexicon_df.values.flatten()

normal_word_match_check(df, lexicon_list)
lemma_word_match_check(df, lexicon_list)
