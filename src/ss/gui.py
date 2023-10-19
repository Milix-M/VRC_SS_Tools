# フル画面を解除して画面の幅と高さを設定
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', 0)

import japanize_kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


class TextWidget(Widget):
    text = StringProperty()


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'VRC SS Tools'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    TestApp().run()