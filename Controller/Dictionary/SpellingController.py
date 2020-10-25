import re
import emoji
import pandas as pd
from Controller import LogController
from Helper.AppConfigHelper import get_app_config_by_key


def load_dictionary():
    dir = get_app_config_by_key("app_dir")
    efc_df = pd.read_csv(dir+"lib/efc_spelling/EFC/filteredSpellingErrors.csv", sep="\t")
    efc_df.drop(['ErrorFrequency'], axis=1, inplace=True)
    return efc_df


lib_df = load_dictionary()


def fix(word):
    print(lib_df)
    return word
