import re
from npl_native_mfm.compare_str import compare_str

__use__hash__ = True


def maximum_string_matching(input_lines, corpus_max_length, use_fast):
    output_list = []
    hash_table = {}
    if use_fast:
        # 将语料库全部加载到内存中
        current_corpus = open("../temp/corpus.temp", 'r', encoding='UTF-8')
        lines = current_corpus.readlines()
        for index in range(len(lines)):
            lines[index] = re.sub("[0-9\n ]", "", lines[index])
            hash_table[lines[index]] = lines[index]
        current_corpus.close()
    # 存在多行输入值时，需要进行逐行进行分词
    for input_line in input_lines:
        # 当前输入文件的开始匹配位置
        current_input_subscript = 0
        # 检测是否已经匹配成功
        flag_compare = False
        # 当前语料库分词控制的最大长度
        current_max_length = 0
        # 获取当前输入行数的长度，防止判断时数组溢出
        input_length = len(input_line)
        # 1. 实现对整个字符串从左到右的遍历，一直到文件末尾停止
        while input_length > current_input_subscript:
            if not use_fast:
                # 2. 每一个语料库中最长子串的长度大小不一，因此在和不同语料库的比较中需要用不断变换最长比较长度
                for key in corpus_max_length:
                    # 得到当前语料库中最大词句的长度
                    current_max_length = corpus_max_length[key]
                    # 为了防止判断溢出，所以这里进行了保护
                    if current_input_subscript + current_max_length > input_length:
                        current_max_length = input_length - current_input_subscript
                    # 将语料库全部加载到内存中
                    current_corpus = open(key, 'r', encoding='UTF-8')
                    lines = current_corpus.readlines()
                    for index in range(len(lines)):
                        lines[index] = re.sub("[0-9\n ]", "", lines[index])
                        hash_table[lines[index]] = lines[index]
                    current_corpus.close()
                    current_compare_str = input_line[current_input_subscript:current_input_subscript + current_max_length]
                    # 3. 实现当前匹配串在当前语料库中进行比较，如果匹配成功则结束此串的比较，如果匹配失败，则去除匹配串末尾进行下一轮比较
                    while current_max_length > 0:
                        # 突然意识到，因为python中的字典就是hash表构建的，所以这里可以直接借用字典进行查找
                        # 4. 遍历语料库中的词语，和当前匹配文本进行比较
                        if not __use__hash__:
                            for line in lines:
                                # 将匹配文本和语料库中的词语进行比较
                                flag_compare = compare_str(current_compare_str, line)
                                # 如果匹配成功
                                if flag_compare:
                                    # 将读写下标向右移动当前判断字符串长度
                                    current_input_subscript += current_max_length
                                    # 将当前分词加入输出列表中
                                    output_list.append(current_compare_str)
                                    # 结束当前循环
                                    break
                        if __use__hash__:
                            flag_compare = hash_table.__contains__(current_compare_str)
                        # 如果在当前语料库中成功找到匹配项则可以退出当前匹配
                        if flag_compare:
                            if __use__hash__:
                                # 将读写下标向右移动当前判断字符串长度
                                current_input_subscript += current_max_length
                                # 将当前分词加入输出列表中
                                output_list.append(current_compare_str)
                            break
                        else:
                            # 将匹配字符串右侧减少一个字符位
                            current_max_length -= 1
                        current_compare_str = current_compare_str[:-1]
                    if flag_compare:
                        flag_compare = False
                        break
            else:
                # 得到当前语料库中最大词句的长度
                current_max_length = corpus_max_length['../temp/corpus.temp']
                # 为了防止判断溢出，所以这里进行了保护
                if current_input_subscript + current_max_length > input_length:
                    current_max_length = input_length - current_input_subscript
                current_compare_str = input_line[current_input_subscript:current_input_subscript + current_max_length]
                # 3. 实现当前匹配串在当前语料库中进行比较，如果匹配成功则结束此串的比较，如果匹配失败，则去除匹配串末尾进行下一轮比较
                while current_max_length > 0:
                    # 4. 遍历语料库中的词语，和当前匹配文本进行比较
                    flag_compare = hash_table.__contains__(current_compare_str)
                    # 如果在当前语料库中成功找到匹配项则可以退出当前匹配
                    if flag_compare:
                        # 将读写下标向右移动当前判断字符串长度
                        current_input_subscript += current_max_length
                        # 将当前分词加入输出列表中
                        output_list.append(current_compare_str)
                        break
                    else:
                        # 将匹配字符串右侧减少一个字符位
                        current_max_length -= 1
                    current_compare_str = current_compare_str[:-1]
                    flag_compare = False
            # 如果匹配到只有一个字符，那这个字符一定是孤立的
            if current_max_length == 0:
                output_list.append(input_line[current_input_subscript])
                current_input_subscript += 1
    return output_list

