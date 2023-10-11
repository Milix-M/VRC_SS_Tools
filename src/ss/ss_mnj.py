import os
import re
import shutil


def copy_ss(ss_paths: list, path: str) -> None:
    """日付分けごとのディレクトリを作成してSSをコピーします

    Args:
        ss_paths (list): 対象となるSSのパス(list)
        path (str): 日付分けされたSSを作成するディレクトリを指定
    """

    extracted_text = []

    for ss in ss_paths:
        m = re.search(r'(\d{4}-([0-1][0-9])-([0-3][0-9]))', ss)
        if m:
            extracted_text.append(m.group())

    sorted_days  = list(dict.fromkeys(extracted_text))

    #作成が必要なディレクトリを作成する
    for make in list(dict.fromkeys(sorted_days)):
        if not os.path.exists(os.path.join(path, make)):
            os.makedirs(os.path.join(path, make))

    for ss in ss_paths:
        day = re.search(r'(\d{4}-([0-1][0-9])-([0-3][0-9]))', ss)
        shutil.copy(os.path.join(path, ss), os.path.join(path, day.group()))

    print("Complete sort!")

