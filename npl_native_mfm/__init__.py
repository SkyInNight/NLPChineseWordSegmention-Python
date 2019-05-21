"""
正向最大匹配，中文分词代码
语料库使用清华提供的源，文本类型为txt，路径为：../chinese_corpus/tsinghua/*
"""
from npl_native_mfm.file_operation.traverse_corpus import traverse_corpus
from npl_native_mfm.compare_str import compare_str
import re
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
    output_list = []
    input_lines = open_input_file()
    corpus_max_length = get_max_length()
    # 3.1 一个字符串在一个语料库中进行匹配，如果匹配得当则结束匹配，否则在下一个语料库中继续匹配
    for input_line in input_lines:
        # 当前输入文件的匹配位置
        current_input_subscript = 0
        # 检测是否已经匹配成功
        flag_compare = False
        # 当前语料库最大长度
        current_max_length = 0
        input_length = len(input_line)
        while input_length > current_input_subscript:
            # 先确定最大匹配字符长度
            for key in corpus_max_length:
                # 得到当前语料库中最大词句的长度
                current_max_length = corpus_max_length[key]
                if current_input_subscript + current_max_length > input_length:
                    current_max_length = input_length - current_input_subscript
                # 将语料库全部加载到内存中
                current_corpus = open(key, 'r', encoding='UTF-8')
                lines = current_corpus.readlines()
                for index in range(len(lines)):
                    lines[index] = re.sub("[A-Za-z0-9\!\%\[\]\,\。\t\n ]", "", lines[index])
                # 逐行进行匹配
                while current_max_length > 0:
                    current_compare_str = input_line[current_input_subscript:current_input_subscript + current_max_length]
                    for line in lines:
                        flag_compare = compare_str(current_compare_str, line)
                        # 如果匹配成功
                        if flag_compare:
                            # 将读写下标向右移动当前判断字符串长度
                            current_input_subscript += current_max_length
                            # 将当前分词加入输出列表中
                            output_list.append(current_compare_str)
                            # 结束当前循环
                            break
                    # 如果在当前语料库中成功找到匹配项则可以退出当前匹配
                    if flag_compare:
                        break
                    else:
                        # 将匹配字符串右侧减少一个字符位
                        current_max_length -= 1
                if flag_compare:
                    flag_compare = False
                    break
            # 如果匹配到只有一个字符，那这个字符一定是孤立的
            if current_max_length == 0:
                output_list.append(input_line[current_input_subscript])
                current_input_subscript += 1
    return output_list


# main函数
def main():
    output = match_words()
    for str_output in output:
        print(str_output + "|", end="")


if __name__ == '__main__':
    main()
