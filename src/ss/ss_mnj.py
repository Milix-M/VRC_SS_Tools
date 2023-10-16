import os
import re
import shutil
import datetime


def copy_ss(ss_paths: list, path: str, date_line: int) -> None:
    """日付分けごとのディレクトリを作成してSSをコピーします

    Args:
        ss_paths (list): 対象となるSSのパス(list)

        path (str): 日付分けされたSSを作成するディレクトリを指定

        date_line (int): 日付変更線を指定します(0-24)
    """

    extracted_text = []

    #キー:SSのパス バリュー:格納先 の辞書
    date_sspath_dict = {}

    for ss in ss_paths:
        m = re.search(r'(\d{4}-([0-1][0-9])-([0-3][0-9]))', ss)
        if m:

            #スクリーンショットの日付情報を取得
            time_m = re.search(r'(\d{4}-([0-1][0-9])-([0-3][0-9])_([0-2][0-9])-([0-5][0-9])-([0-5][0-9]))', ss)

            #datetimeに変換
            ss_dttime = datetime.datetime.strptime(time_m.group(), "%Y-%m-%d_%H-%M-%S")

            # 日付を変更する時間（6時）を設定
            change_time = ss_dttime.replace(hour=date_line, minute=0, second=0, microsecond=0)

            # SSの日時が日付を変更する時間より前の場合、前日の6時に設定
            if ss_dttime < change_time:
                change_time -= datetime.timedelta(days=1)

            #日付変更線を適用した日時をStringsに戻し日付データを格納するリストにappend
            extracted_text.append(change_time.date().strftime("%Y-%m-%d"))

            date_sspath_dict[ss] = change_time.date().strftime("%Y-%m-%d")


    sorted_days  = list(dict.fromkeys(extracted_text))

    #作成が必要なディレクトリを作成する
    for make in sorted_days:
        if not os.path.exists(os.path.join(path, make)):
            os.makedirs(os.path.join(path, make))

    # for ss in ss_paths:
    #     day = re.search(r'(\d{4}-([0-1][0-9])-([0-3][0-9]))', ss)
    #     shutil.copy(os.path.join(path, ss), os.path.join(path, day.group()))

    #date_sspath_dictを元にSSをコピー
    for ss_path, putting_dir in date_sspath_dict.items():
        shutil.copy(ss_path, os.path.join(path, putting_dir))

    print("Complete sort!")

