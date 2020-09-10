
def get_distinct_list(obj):
    list_obj = []
    for word in obj:
        if word.lower() not in list_obj:
            list_obj.append(word.lower())
    return list_obj