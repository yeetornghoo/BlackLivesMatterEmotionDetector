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


# MASTER: CONVERT TO TOKEN AND LEMMATIZE THE TEXT
def master_process_sentence(sentence, is_lemm):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma', tokenize_no_ssplit=True)
    doc = nlp(sentence)
    sentence_words = []
    for i, sentence in enumerate(doc.sentences):
        for stz_obj in sentence.words:
            if stz_obj.upos not in allowed_upos:
                if is_lemm:
                    sentence_words.append(stz_obj.lemma)
                else:
                    sentence_words.append(stz_obj.text)
    return sentence_words


# MASTER: LOAD DATASET AND PROCESS
def master_count_unique_word(master_df):
    ttl_dataset_words = []
    for index, row in master_df.iterrows():
        words = row[0]
        for word in words:
            target_word = word.lower()
            if target_word not in ttl_dataset_words:
                ttl_dataset_words.append(target_word)

    LogController.log("TOTAL UNIQUE WORDS IN DATASET IS {}".format(len(ttl_dataset_words)))


# ------------------------------------------------
# CHECK NORMAL WORD MATCH FUNCTION
# ------------------------------------------------

def normal_word_match_check(master_df, lexicon_obj):
    unique_words = []

    for index, row in master_df.iterrows():
        words = row["tweet_text"]
        for word in words:
            target_word = word.lower().strip()
            if target_word in lexicon_obj:
                if target_word not in unique_words:
                    unique_words.append(target_word)
    #print(unique_words)
    LogController.log("TOTAL UNIQUE WORDS IN STANDARD FORM IS {}".format(len(unique_words)))

# ------------------------------------------------
# CHECK LEMMATIZED WORD MATCH FUNCTION
# ------------------------------------------------


def lemma_word_match_check(master_df, lexicon_obj):
    unique_words = []

    for index, row in master_df.iterrows():
        #print(row["text"])
        words = row["lemma_tweet_text"]
        for word in words:
            target_word = word.lower().strip()
            if target_word in lexicon_obj:
                #print("FOUND MATCH " + target_word)
                if target_word not in unique_words:
                    unique_words.append(target_word)
    #print(unique_words)
    LogController.log("TOTAL UNIQUE WORDS IN LEMMAIZED FORM IS {}".format(len(unique_words)))


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