import os

from file_operation.file_operation import read_corpus

__output_file__ = "../temp/"


def traverse_corpus(file_path):
    corpus_lengths = {}
    # 获取当前目录下面的文件列表
    path_dir = os.listdir(file_path)
    for path in path_dir:
        # 将文件名补充完整
        new_dir = os.path.join(file_path, path)
        # 判断如果是txt文件
        if os.path.splitext(new_dir)[1] == ".txt":
            # 读文件
            corpus_lengths[__output_file__ + os.path.splitext(os.path.split(new_dir)[1])[0] + '.temp'] = read_corpus(new_dir)
            pass
        else:
            # 递归遍历文件夹
            print(new_dir)
            corpus_lengths.update(traverse_corpus(new_dir))
    return corpus_lengths
