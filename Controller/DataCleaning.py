import re
import pandas as pd
from Controller import LogController

corr_df = pd.read_csv('C:/workspace/SocialMovementSentiment/dataset/_custome/correction.csv')



def run(df):
    LogController.log_h1("START DATA CLEANING")

    replace_special_char_df(df)
    remove_url_df(df)
    replace_word_is_df(df)
    replace_are_df(df)
    replace_am_df(df)
    replace_will_df(df)
    replace_have_df(df)
    replace_would_df(df)
    #replace_correction_words_df(df)

    return df


def has_unchange_tweet(reg_pattern, df):
    for index, row in df.iterrows():
        search_result = re.search(reg_pattern, row["tweet_text"])
        if search_result is not None:
            print("FOUND - {}".format(row["tweet_text"]))
            return True
    return False


# REPLACE SPECIAL CHARACTERS FROM THE SENTENCES
def replace_special_char(sentence):
    sentence = sentence.replace("“", '"')
    sentence = sentence.replace("”", '"')
    sentence = sentence.replace("’", "'")
    return sentence


def replace_special_char_df(df):
    LogController.log("Replace Special Characters From The Sentences")
    has_unchange = True
    reg_pattern = "(“|”|’)"

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_special_char(str(x)))
        has_unchange = has_unchange_tweet(reg_pattern, df)


# REMOVE URL FROM THE SENTENCES
def remove_url(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        sentence = sentence.replace(search_result[0], "")
    return sentence


def remove_url_df(df):
    LogController.log("Remove URL From The Sentences")
    has_unchange = True
    reg_pattern = "(?P<url>https?://[^\s]+)"

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: remove_url(str(x), reg_pattern))
        has_unchange = has_unchange_tweet(reg_pattern, df)


# REPLACE 'S TO IS FROM THE SENTENCES
def replace_word_is(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} is".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word.lower())
    return sentence


def replace_word_is_df(df):
    LogController.log("Replace 'S To IS From The Sentences")
    has_unchange = True
    reg_pattern = "[-A-Za-z]+'[Ss]+"

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_word_is(str(x), reg_pattern))
        has_unchange = has_unchange_tweet(reg_pattern, df)


# REPLACE 'RE TO ARE FROM THE SENTENCES
def replace_are(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} are".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def replace_are_df(df):
    LogController.log("Replace 'RE To ARE From The Sentences")
    has_unchange = True
    reg_pattern = "[-A-Za-z]+'[ERer]+"

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_are(str(x), reg_pattern))
        has_unchange = has_unchange_tweet(reg_pattern, df)


# REPLACE 'M TO AM FROM THE SENTENCES
def replace_am(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} am".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def replace_am_df(df):
    LogController.log("Replace 'M To AM From The Sentences")
    has_unchange = True
    reg_pattern = "[Ii]+'[Mm]+"

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_am(str(x), reg_pattern))
        has_unchange = has_unchange_tweet(reg_pattern, df)


# REPLACE 'LL TO WILL FROM THE SENTENCES
def replace_will(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} will".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def replace_will_df(df):
    LogController.log("Replace 'LL To WILL From The Sentences")
    has_unchange = True
    reg_pattern = "[-A-Za-z]+'(LL|ll)"

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_will(str(x), reg_pattern))
        has_unchange = has_unchange_tweet(reg_pattern, df)


# REPLACE 'VE TO HAVE FROM THE SENTENCES
def replace_have(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} ha{}".format(split_word[0], split_word[1])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def replace_have_df(df):
    LogController.log("Replace 'VE To HAVE From The Sentences")
    has_unchange = True
    reg_pattern = "[-A-Za-z]+'(VE|ve)"

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_have(str(x), reg_pattern))
        has_unchange = has_unchange_tweet(reg_pattern, df)


# REPLACE 'D TO WOULD FROM THE SENTENCES
def replace_would(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} would".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def replace_would_df(df):
    LogController.log("Replace 'D To WOULD From The Sentences")
    has_unchange = True
    reg_pattern = "[-A-Za-z]+'[Dd] "

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_would(str(x), reg_pattern))
        has_unchange = has_unchange_tweet(reg_pattern, df)


# CORRECTION > COMPARE WORD FROM CORRECTION.CSV FILE
def search_word(word):
    to_text = word.lower()
    corr_word_df = (corr_df.loc[corr_df['from_text'] == word.lower()])
    if not corr_word_df.empty:
        to_text = corr_word_df.iat[0, 1]
    return to_text


# TODO: PENDING TO ADD THE COUNT CHECK
def replace_would_df(df):
    LogController.log("Replace Correction Word")
    has_unchange = True

    while has_unchange:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: search_word(str(x)))
        #has_unchange = has_unchange_tweet(reg_pattern, df)






# CORRECTION > SEARCH WORD AND REPLACE WORDS
def replace_correction_words(sentence):
    search_result = re.search("[-A-Za-z]+'[-A-Za-z]+", sentence)
    if search_result is not None:
        from_word = search_result[0]
        to_word = search_word(from_word)
        # print("BEFORE:{} <> AFTER:{}".format(from_word, to_word))
        sentence = sentence.replace(from_word, to_word)
    return sentence
