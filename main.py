import os
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout

# constants
MAIN_WINDOW: str = os.path.abspath('main.kv')

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class MainApp(MDApp):
    def build(self):
        return Builder.load_file(MAIN_WINDOW)

    def on_start(self):
        self.fps_monitor_start()


MainApp().run()