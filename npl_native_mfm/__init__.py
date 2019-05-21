"""
正向最大匹配，中文分词代码
语料库使用清华提供的源，文本类型为txt，路径为：../chinese_corpus/tsinghua/*
"""
from file_operation.traverse_corpus import traverse_corpus
from npl_native_mfm.maximum_string_matching import  maximum_string_matching

__preprocessing_file_path__ = "../input_file/input.txt"
__corpus_path__ = "../chinese_corpus/"


# 1. 先获取输入数据的文件
def open_input_file():
    file = open(__preprocessing_file_path__, "r", encoding='UTF-8')
    lines = file.readlines()
    for line in lines:
        subscript = line.find(' ')
        if subscript > -1:
            line = line[0:subscript]
        # 调试输出line
        # print(len(line))
    return lines


# 2. 遍历所有的语料库文件并获取每一个语料库中最长的字符数组
def get_max_length():
    max_length = traverse_corpus(__corpus_path__)
    return max_length


# 3. 通过用户输入的字符串在每一个语料库中进行正向最大匹配
def match_words():
    # 最终输出的分词列表
    output_list = []
    # 获取输入列表
    input_lines = open_input_file()
    # 获取字典库中的最大长度子串
    corpus_max_length = get_max_length()
    # 3.1 一个字符串在一个语料库中进行匹配
    output_list = maximum_string_matching(input_lines, corpus_max_length)
    return output_list


# main函数
def main():
    output = match_words()
    for str_output in output:
        print(str_output + "|", end="")


if __name__ == '__main__':
    main()
