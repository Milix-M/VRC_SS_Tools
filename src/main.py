import json

#ソートターゲットディレクトリ走査用モジュール
from ss import target, ss_mnj


with open("./settings.json") as f:
    settings = json.load(f)

sort_target = target.get_target_ss(target.get_target_dir(settings["ss_path"]))

ss_mnj.make_days_dir(sort_target, settings["ss_path"])

ss_mnj.copy_ss(sort_target, settings["ss_path"])