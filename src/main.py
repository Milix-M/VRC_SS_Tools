import json
import time

#ソートターゲットディレクトリ走査用モジュール
from ss import target, ss_mnj


with open("./settings.json") as f:
    settings = json.load(f)

while True:
    time.sleep(10)
    sort_target = target.get_target_ss(target.get_target_dir(settings["ss_path"]))
    ss_mnj.copy_ss(sort_target, settings["ss_path"], settings["date_line"])