import re
import os

def get_target_dir(path: str) -> list:
    """ソート対象のディレクトリを取得
    YYYY-MM形式のディレクトリを取得します

    Args:
        path (str): ソート対象を走査するディレクトリを指定

    Returns:
        list: ソート対象のディレクトリ
    """
    pattern = r'\d{4}-\d{2}$'

    target_dir = []

    # ディレクトリ内のフォルダを検索
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            if re.match(pattern, dir_name):
                target_dir.append(os.path.join(root, dir_name))

    return target_dir