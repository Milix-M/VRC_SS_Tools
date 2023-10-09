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

def get_target_ss(path: str) -> list:
    """SSを全て取得します
    VRChat_YYYY-MM-DD_hh-mm-ssから始まる.pngファイルを全て取得します

    Args:
        dir (str): 走査対象のディレクトリを指定

    Returns:
        list: 対象のSS
    """
    # example: VRChat_2022-11-14_21-35-14.256_1920x1080.png
    pattern = r'VRChat_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.\d{3}_\d{4}x\d{4}.png'

    ss = []

    # ディレクトリ内のファイルを検索
    for dir in path:
        for root, dirs, files in os.walk(dir):
            for file_name in files:
                if re.match(pattern, file_name):
                    ss.append(os.path.join(root, file_name))

    return ss