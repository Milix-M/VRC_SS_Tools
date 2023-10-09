import json

#ソートターゲットディレクトリ走査用モジュール
from get_target import get_dir


with open("./settings.json") as f:
    settings = json.load(f)

print(get_dir.get_target_dir(settings["ss_path"]))