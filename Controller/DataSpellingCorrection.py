import re
import emoji
from Controller import LogController

def load_dictionary():
    dir = get_app_config_by_key("app_dir")
    efc_df = pd.read_csv(dir+"lib/efc_spelling/EFC/filteredSpellingErrors.csv", sep="\t")
    efc_df.drop(['ErrorFrequency'], axis=1, inplace=True)
    return efc_df


lib_df = load_dictionary()


def fix(word):
    print(lib_df)
    return word


def run(df):
    LogController.log_h1("START DATA SPELLING CORRECTION")