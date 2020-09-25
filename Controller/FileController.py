from Helper import FolderHelper


def save_log(folder_path, file_name, context):
    file_path = "{}/{}".format(folder_path, file_name)
    f = open(file_path, 'w')
    f.write(context)
    f.close()


def initiate_file(folder_path, file_name):
    file_path = "{}/{}".format(folder_path, file_name)
    f = open(file_path, 'w')
    return f


def save_df_to_csv(file_name, df):
    df.to_csv(file_name, index=False, encoding='utf-8')
