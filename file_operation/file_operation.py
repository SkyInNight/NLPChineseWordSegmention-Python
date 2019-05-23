import re
import os

__output_file__ = "../temp/"


def read_corpus(file_path):
    file_name = os.path.split(file_path)[1]
    file_name = os.path.splitext(file_name)[0]
    file_output_path = __output_file__ + file_name + ".temp"
    # 判断是否已经对语料库进行处理，如果处理则不用做重复操作
    if os.access(file_output_path, os.F_OK):
        file_output = open(file_output_path, 'r', encoding='UTF-8')
        max_length = int(file_output.readline())
    else:
        # 打开语料库文件
        file = open(file_path, 'r', encoding='UTF-8')
        file_output = open(file_output_path, 'w', encoding='UTF-8')
        lines = file.readlines()
        max_length = 0
        for index in range(len(lines)):
            lines[index] = re.sub("[A-Za-z0-9\!\%\[\]\,\。\t ]", "", lines[index])
            length = len(lines[index])
            if max_length < length:
                max_length = length
        file_output.write(str(max_length) + '\n')
        file_output.writelines(lines)
    return max_length
