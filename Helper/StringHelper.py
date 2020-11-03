

def compare_str(obja, objb):
    return obja.lower().strip() == objb.lower().strip()


def isEmpty(str_obj):
    if len(str(str_obj).lower().strip()) < 1:
        return True
    return False


def trim_word(str_obj):
    return str(str_obj).strip()
