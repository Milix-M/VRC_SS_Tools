import json

#ソートターゲットディレクトリ走査用モジュール
from ss import target
from filemnj import dirs

with open("./settings.json") as f:
    settings = json.load(f)

sort_target = target.get_target_ss(target.get_target_dir(settings["ss_path"]))

dirs.make_days_dir(sort_target, settings["ss_path"])