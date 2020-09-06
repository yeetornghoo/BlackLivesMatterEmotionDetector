import re
import pandas as pd
from Controller import LogController
corr_df = pd.read_csv('C:/workspace/BlackLiveMetters/lexicon/_custome/correction.csv')


def run(df):
    LogController.log_h1("START DATA CLEANING")

    LogController.log("Replace Special Characters From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_special_char(str(x)))

    LogController.log("Remove URL From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: remove_url(str(x)))

    LogController.log("Replace 'S To IS From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_word_is(str(x)))

    LogController.log("Replace 'RE To ARE From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_are(str(x)))

    LogController.log("Replace 'M To AM From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_am(str(x)))

    LogController.log("Replace 'LL To WILL From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_will(str(x)))

    LogController.log("Replace 'VE To HAVE From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_have(str(x)))

    LogController.log("Replace 'D To WOULD From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_would(str(x)))

    LogController.log("Replace Correction Word")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_correction_words(str(x)))

    return df

# REPLACE SPECIAL CHARACTERS FROM THE SENTENCES
def replace_special_char(sentence):
    sentence = sentence.replace("“", '"')
    sentence = sentence.replace("”", '"')
    sentence = sentence.replace("’", "'")
    return sentence


# REMOVE URL FROM THE SENTENCES
def remove_url(sentence):
    search_result = re.search("(?P<url>https?://[^\s]+)", sentence)
    if search_result is not None:
        sentence = sentence.replace(search_result[0], "")
    return sentence


# REPLACE 'S TO IS FROM THE SENTENCES
def replace_word_is(sentence):
    search_result = re.search("[-A-Za-z]+'[Ss]+", sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} is".format(split_word[0])).lower()
        # print("BEFORE:{} <> AFTER:{}".format(word, replace_word))
        sentence = sentence.replace(word, replace_word.lower())
    return sentence


# REPLACE 'RE TO ARE FROM THE SENTENCES
def replace_are(sentence):
    search_result = re.search("[-A-Za-z]+'[ERer]+", sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} are".format(split_word[0])).lower()
        # print("BEFORE:{} <> AFTER:{}".format(word, replace_word))
        sentence = sentence.replace(word, replace_word)
    return sentence


# REPLACE 'M TO AM FROM THE SENTENCES
def replace_am(sentence):
    search_result = re.search("[Ii]+'[Mm]+", sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} am".format(split_word[0])).lower()
        # print("BEFORE:{} <> AFTER:{}".format(word, replace_word))
        sentence = sentence.replace(word, replace_word)
    return sentence


# REPLACE 'LL TO WILL FROM THE SENTENCES
def replace_will(sentence):
    search_result = re.search("[-A-Za-z]+'(LL|ll)", sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} will".format(split_word[0])).lower()
        # print("BEFORE:{} <> AFTER:{}".format(word, replace_word))
        sentence = sentence.replace(word, replace_word)
    return sentence


# REPLACE 'VE TO HAVE FROM THE SENTENCES
def replace_have(sentence):
    search_result = re.search("[-A-Za-z]+'(VE|ve)", sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} ha{}".format(split_word[0], split_word[1])).lower()
        # print("BEFORE:{} <> AFTER:{}".format(word, replace_word))
        sentence = sentence.replace(word, replace_word)
    return sentence


# REPLACE 'D TO WOULD FROM THE SENTENCES
def replace_would(sentence):
    search_result = re.search("[-A-Za-z]+'[Dd] ", sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} would".format(split_word[0])).lower()
        # print("BEFORE:{} <> AFTER:{}".format(word, replace_word))
        sentence = sentence.replace(word, replace_word)
    return sentence


# CORRECTION > COMPARE WORD FROM CORRECTION.CSV FILE
def search_word(word):
    to_text = word.lower()
    corr_word_df = (corr_df.loc[corr_df['from_text']==word.lower()])
    if not corr_word_df.empty:
        to_text = corr_word_df.iat[0,1]
    return to_text


# CORRECTION > SEARCH WORD AND REPLACE WORDS
def replace_correction_words(sentence):
    search_result = re.search("[-A-Za-z]+'[-A-Za-z]+", sentence)
    if search_result is not None:
        from_word = search_result[0]
        to_word = search_word(from_word)
        # print("BEFORE:{} <> AFTER:{}".format(from_word, to_word))
        sentence = sentence.replace(from_word, to_word)
    return sentence
