import os
import re
import shutil

def make_days_dir(sss: list, path: str) -> None:
    """日付ごとにフォルダを作成します
    SSの名前から日付を検出し日付ごとに作成

    Args:
        sss (list): 日付ごとのフォルダを作成するスクリーンショットのパスを指定
        path (str): 日付ごとのフォルダを作成するディレクトリを指定
    """
    extracted_text = []
    for ss in sss:
        m = re.search(r'(\d{4}-([0-1][0-9])-([0-3][0-9]))', ss)
        if m:
            extracted_text.append(m.group())

    sorted_days  = list(dict.fromkeys(extracted_text))

    #作成が必要なディレクトリを作成する
    for make in list(dict.fromkeys(sorted_days)):
        if not os.path.exists(os.path.join(path, make)):
            os.makedirs(os.path.join(path, make))

def copy_ss(ss_paths: list, path: str) -> None:
    """スクリーンショットをコピーします

    Args:
        ss_path (list): スクリーンショットのパスを指定
        path (str): 日付ごとのフォルダが存在するディレクトリのパスを指定
    """
    for ss in ss_paths:
        day = re.search(r'(\d{4}-([0-1][0-9])-([0-3][0-9]))', ss)
        shutil.copy(os.path.join(path, ss), os.path.join(path, day.group()))
        print("Complete Copy!")

