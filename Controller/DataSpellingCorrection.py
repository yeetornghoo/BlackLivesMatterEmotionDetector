import re
import emoji
from Controller import LogController
import pandas as pd
from ast import literal_eval
from Helper import StringHelper
from Helper.AppConfigHelper import get_app_config_by_key

dir = get_app_config_by_key("app_dir")
corr_df = pd.read_csv(dir+'lib/manual_correction/correction.csv')


'''
def load_dictionary():
    efc_df = pd.read_csv(dir+"lib/efc_spelling/EFC/filteredSpellingErrors.csv", sep="\t")
    efc_df.drop(['ErrorFrequency'], axis=1, inplace=True)
    return efc_df



lib_df = load_dictionary()

# SPELLING CORRECTION
def efc_spelling_correction(df):
    for index, row in lib_df.iterrows():

        # GET CORRECT WORD
        correction_str = StringHelper.trim_word(row["Correction"])

        # GET ERROR WORDS
        errors_str = StringHelper.trim_word(row["Errors"].replace('[', "").replace(']', ""))
        errors = errors_str[1:-1].split(',')

        # REPLACE
        for error in errors:
            error_str = StringHelper.trim_word(error)
            df["tweet_text"] = df["tweet_text"].str.replace(" {} ".format(error_str), " {} ".format(correction_str))
            #df["tweet_text"] = df["tweet_text"].str.replace(error_str, correction_str)

    return df
'''

# SPELLING CORRECTION
def spelling_correction(df):
    for index, row in corr_df.iterrows():
        df["tweet_text"] = df["tweet_text"].str.replace(" {} ".format(row["from_text"]), " {} ".format(row["to_text"]))
    return df


# REPLACE SPECIAL CHARACTERS FROM THE SENTENCES
def remove_extra_whitespace_char(sentence):
    sentence = sentence.replace("    ", " ")
    sentence = sentence.replace("   ", " ")
    sentence = sentence.replace("  ", " ")
    return sentence.strip()


def remove_extra_whitespace_df(df):
    LogController.log("Replace extra white space From The Sentences")
    df['tweet_text'] = df['tweet_text'].apply(lambda x: remove_extra_whitespace_char(str(x)))
    return df


def run(df):
    LogController.log_h1("START DATA SPELLING CORRECTION")

    LogController.log("Custome Spelling Correction")
    df = spelling_correction(df)

    LogController.log("Remove Extra Whitespace")
    df = remove_extra_whitespace_df(df)

    return df
