import json

#ソートターゲットディレクトリ走査用モジュール
from ss import target, ss_mnj


with open("./settings.json") as f:
    settings = json.load(f)

print("スクリーンショットを日付分けしますか？: y/n")
choice = input("")

if choice == "y":
    sort_target = target.get_target_ss(target.get_target_dir(settings["ss_path"]))

    ss_mnj.copy_ss(sort_target, settings["ss_path"])
else:
    print("処理を中止します")