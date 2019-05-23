import os

from file_operation.file_operation import read_corpus

__output_file__ = "../temp/"


def traverse_corpus(file_path, use_fast):
    corpus_lengths = {}
    max_length = 0
    # 获取当前目录下面的文件列表
    path_dir = os.listdir(file_path)
    for path in path_dir:
        # 将文件名补充完整
        new_dir = os.path.join(file_path, path)
        # 判断如果是txt文件
        if os.path.splitext(new_dir)[1] == ".txt":
            # 读文件
            length = read_corpus(new_dir, use_fast)
            if max_length < length:
                max_length = length
            if not use_fast:
                corpus_lengths[__output_file__ + os.path.splitext(os.path.split(new_dir)[1])[0] + '.temp'] = length
            else:
                corpus_lengths[__output_file__ + 'corpus.temp'] = max_length
            pass
        else:
            # 递归遍历文件夹
            print(new_dir)
            corpus_lengths.update(traverse_corpus(new_dir, use_fast))
    return corpus_lengths
