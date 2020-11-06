from datetime import datetime
import numpy as np

standard_date_format = "%Y-%m-%d %H:%M:%S"


# RETURN DATETIME BY DATE AND HOUR ONLY, MIN AND SEC SET TO 0
def get_date_with_hour(str_input, date_format):
    new_date = str_input[0:13]+":00:00"
    return datetime.strptime(new_date, date_format)


def get_date_with_time(str_input):
    new_date_str = "{} 00:00:00".format(str_input)
    new_date = datetime.strptime(new_date_str, "%Y-%m-%d %H:%M:%S")
    return new_date


def get_datetime64(str_date, input_format):
    new_date = datetime.strptime(str_date, input_format)
    new_date = np.datetime64(new_date)
    return new_date


# HANDLE DATETIME END WITH +00:00
def standardize_date(str_input, date_format):
    end_index = str_input.find('+')
    print(str_input[0:end_index])
    return str_input[0:end_index]
