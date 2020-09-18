from datetime import datetime


# RETURN DATETIME BY DATE AND HOUR ONLY, MIN AND SEC SET TO 0
def get_date_with_hour(str_input, date_format):
    new_date = str_input[0:13]+":00:00"
    return datetime.strptime(new_date, date_format)
