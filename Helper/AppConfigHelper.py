import os

from configparser import ConfigParser
app_config_file_path = "C:/workspace/SocialMovementSentiment/app.config"


def get_value_by_key(line):
    start_index = line.index("=")+1
    return line[start_index:].strip()


def get_app_config_by_key(key):
    with open(app_config_file_path, 'r') as read_obj:
        for line in read_obj:
            if key in line:
                return get_value_by_key(line)
    return None
