import re
import os
import xlrd

__output_file__ = "../temp/"


def read_corpus(file_path, use_fast):
    file_name = os.path.split(file_path)[1]
    (file_name, file_type) = os.path.splitext(file_name)
    if file_type == '.xls':
        return read_xls_file_path(file_path, use_fast)
    if not use_fast:
        file_output_path = __output_file__ + file_name + ".temp"
    else:
        file_output_path = __output_file__ + "corpus.temp"
    # 判断是否已经对语料库进行处理，如果处理则不用做重复操作
    if os.access(file_output_path, os.F_OK) and not use_fast:
        file_output = open(file_output_path, 'r', encoding='UTF-8')
        max_length = int(file_output.readline())
        return max_length
    else:
        # 打开语料库文件
        file = open(file_path, 'r', encoding='UTF-8')
        if use_fast:
            file_output = open(file_output_path, 'a', encoding='UTF-8')
        else:
            file_output = open(file_output_path, 'w', encoding='UTF-8')
        lines = file.readlines()
        max_length = 0
        for index in range(len(lines)):
            lines[index] = re.sub("[0-9\[\]\,\。\t ]", "", lines[index])
            length = len(lines[index])
            if max_length < length:
                max_length = length
        if not use_fast:
            file_output.write(str(max_length) + '\n')
        file_output.writelines(lines)
        file_output.close()
        file.close()
    return max_length


def read_xls_file_path(file_path, use_fast):
    file_name = os.path.split(file_path)[1]
    file_name = os.path.splitext(file_name)[0]
    if not use_fast:
        file_output_path = __output_file__ + file_name + ".temp"
    else:
        file_output_path = __output_file__ + "corpus.temp"
    # 判断是否已经对语料库进行处理，如果处理则不用做重复操作
    if os.access(file_output_path, os.F_OK) and not use_fast:
        file_output = open(file_output_path, 'r', encoding='UTF-8')
        max_length = int(file_output.readline())
        return max_length
    else:
        # 现获取Excel表格中的语料库内容
        workbook = xlrd.open_workbook(file_path)
        worksheet = workbook.sheet_by_index(0)
        lines = worksheet.col_values(1)
        if use_fast:
            file_output = open(file_output_path, 'a', encoding='UTF-8')
        else:
            file_output = open(file_output_path, 'w', encoding='UTF-8')
        max_length = 0
        for line in lines:
            length = len(line)
            if max_length < length:
                max_length = length
        if not use_fast:
            file_output.write(str(max_length) + '\n')
        for line in lines:
            if len(line) > 1:
                file_output.write(line+"\n")
        file_output.close()
    return max_length

