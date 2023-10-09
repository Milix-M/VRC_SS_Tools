import re
import os

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