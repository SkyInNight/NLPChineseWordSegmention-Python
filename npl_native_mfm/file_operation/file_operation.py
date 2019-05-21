import re


def read_corpus(file_path):
    file = open(file_path, 'r', encoding='UTF-8')
    lines = file.readlines()
    max_length = 0
    for line in lines:
        line = re.sub("[A-Za-z0-9\!\%\[\]\,\。\t\n ]", "", line)
        length = len(line)
        if max_length < length:
            max_length = length
    return max_length
