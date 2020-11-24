import re
import string
from Controller import LogController
from emot.emo_unicode import UNICODE_EMO, EMOTICONS


def convert_single_line_str(ste):
    return ste.replace('\n', '')


def convert_single_line_df(df):
    LogController.log("Replace extra white space From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: convert_single_line_str(str(x)))
    return df


def run(df):
    LogController.log_h1("START DATA CLEANING")

    df = convert_single_line_df(df)
    df = remove_url_df(df)
    df = remove_atusername_df(df)
    df = handle_emoji_df(df)
    df = handle_emoticon_df(df)
    # df = process_hasgtag_df(df)
    # df = remove_punctuation_df(df)
    df = replace_word_is_df(df)
    df = replace_are_df(df)
    df = replace_am_df(df)
    df = replace_will_df(df)
    df = replace_have_df(df)
    df = replace_would_df(df)
    df = replace_special_char_df(df)
    df = remove_extra_whitespace_df(df)
    return df


def has_unchanged_tweet(reg_pattern, df):
    for index, row in df.iterrows():
        search_result = re.search(reg_pattern, row["tweet_text"])
        if search_result is not None:
            print("FOUND - {}".format(row["tweet_text"]))
            return True
    return False


# REPLACE SPECIAL CHARACTERS FROM THE SENTENCES
def remove_extra_whitespace_char(sentence):
    sentence = sentence.replace("    ", " ")
    sentence = sentence.replace("   ", " ")
    sentence = sentence.replace("  ", " ")
    sentence = sentence.replace('\n', ' ').replace('\r', '')
    return sentence


def remove_extra_whitespace_df(df):
    LogController.log("Replace extra white space From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: remove_extra_whitespace_char(str(x)))
    return df


# REPLACE SPECIAL CHARACTERS FROM THE SENTENCES
def replace_special_char(sentence):
    sentence = sentence.replace("“", '')
    sentence = sentence.replace("”", '')
    sentence = sentence.replace(":", '')
    sentence = sentence.replace("’", "'")
    sentence = sentence.replace("(", "")
    sentence = sentence.replace(")", "")
    sentence = sentence.replace("]", "")
    sentence = sentence.replace("[", "")
    return sentence


def replace_special_char_df(df):
    LogController.log("Replace Special Characters From The Sentences")
    has_unchanged = True
    reg_pattern = "(“|”|’)"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_special_char(str(x)))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


# REMOVE URL FROM THE SENTENCES
def remove_url(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        sentence = sentence.replace(search_result[0], "")
    return sentence


def remove_url_df(df):
    LogController.log("Remove URL From The Sentences")
    has_unchanged = True
    reg_pattern = "(?P<url>https?://[^\s]+)"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: remove_url(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


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
    has_unchanged = True
    reg_pattern = "[-A-Za-z]+'[Ss]+"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_word_is(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


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
    has_unchanged = True
    reg_pattern = "[-A-Za-z]+'[ERer]+"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_are(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


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
    has_unchanged = True
    reg_pattern = "[Ii]+'[Mm]+"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_am(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


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
    has_unchanged = True
    reg_pattern = "[-A-Za-z]+'(LL|ll)"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_will(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


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
    has_unchanged = True
    reg_pattern = "[-A-Za-z]+'(VE|ve)"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_have(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


# REPLACE 'D TO WOULD FROM THE SENTENCES
def replace_would(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        split_word = word.split("\'", 1)
        replace_word = ("{} would ".format(split_word[0])).lower()
        sentence = sentence.replace(word, replace_word)
    return sentence


def replace_would_df(df):
    LogController.log("Replace 'D To WOULD From The Sentences")
    has_unchanged = True
    reg_pattern = "[-A-Za-z]+'[Dd] "

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: replace_would(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


# REMOVE TWITTER USERNAME
def remove_atusername(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        sentence = sentence.replace(word, "")
    return sentence


def remove_atusername_df(df):
    LogController.log("Remove @USERNAME")
    has_unchanged = True
    reg_pattern = "@[^\s]+"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: remove_atusername(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


def split_hashtag(word):
    split_reg_pattern = "[A-Z][^A-Z]*"
    if word != word.upper():
        split_word = re.findall(split_reg_pattern, word)
        if len(split_word) > 1:
            word = ' '.join(map(str, split_word))
    return word


def process_hasgtag(sentence, reg_pattern):
    search_result = re.search(reg_pattern, sentence)
    if search_result is not None:
        word = search_result[0]
        to_word = split_hashtag(word.replace("#", ""))
        sentence = sentence.replace(word, to_word)

    return sentence


def process_hasgtag_df(df):
    LogController.log("Process Hasgtag")
    has_unchanged = True
    reg_pattern = "#[^\s]+"

    while has_unchanged:
        df['tweet_text'] = df['tweet_text'].apply(lambda x: process_hasgtag(str(x), reg_pattern))
        has_unchanged = has_unchanged_tweet(reg_pattern, df)

    return df


# HANDLE EMOCON
def handle_emoticon_df(df):
    LogController.log("Process Emocon")
    for emot in EMOTICONS:
        try:
            #print(emot)
            to_str = EMOTICONS[emot].replace(",", "").replace(":", "")
            df["tweet_text"] = df["tweet_text"].str.replace(emot,  " " + to_str + " ")
        except:
            print("error")
    return df


# HANDLE EMOJI
def handle_emoji_df(df):
    LogController.log("Process Emoji")
    for emot in UNICODE_EMO:
        try:
            #print(emot)
            to_str = UNICODE_EMO[emot].replace(",", "").replace(":", "")
            df["tweet_text"] = df["tweet_text"].str.replace(emot,  " " + to_str + " ")
        except:
            print("error")
    return df


def remove_punctuation_df(df):
    LogController.log("Remove Punctuation")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: remove_punctuation(str(x)))
    return df


def remove_punctuation(text):
    PUNCT_TO_REMOVE = string.punctuation
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))
