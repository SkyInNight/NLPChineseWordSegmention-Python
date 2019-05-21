def compare_str(str_1, str_2):
    is_match = False
    # 优先比较两个字符串的大小
    is_match = len(str_1) == len(str_2)
    if is_match:
        # 如果两个字符串长度相同则继续判断
        is_match = str_1 == str_2

    return is_match
