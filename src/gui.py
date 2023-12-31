# フル画面を解除して画面の幅と高さを設定
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', 0)

import japanize_kivy
import json
import os

from kivy.clock import Clock
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty

from ss import target, ss_mnj

class TextWidget(Widget):
    text = StringProperty()
    input = ObjectProperty()
    input2 = ObjectProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)

        with open("./settings.json") as f:
            settings = json.load(f)

        self.input.text = settings["ss_path"]
        self.input2.text = str(settings["date_line"])

        Clock.schedule_interval(self.update, 10)

    def update(self, dt):
        with open("./settings.json") as f:
            settings = json.load(f)

        sort_target = target.get_target_ss(target.get_target_dir(settings["ss_path"]))
        ss_mnj.move_ss(sort_target, settings["ss_path"], settings["date_line"])

        #不要になったYYYY-MMディレクトリを削除
        for i in target.get_target_dir(settings["ss_path"]):
            try:
                os.rmdir(i)
            except OSError:
                pass

    def buttonClicked(self):
        with open("./settings.json") as f:
            settings = json.load(f)

        settings["ss_path"] = self.input.text
        settings["date_line"] = int(self.input2.text)

        with open("./settings.json", "w") as f:
            json.dump(settings, f, indent=2)



class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'VRC SS Tools'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    TestApp().run()