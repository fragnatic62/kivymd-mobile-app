import os
from kivymd.app import MDApp
from kivy.lang import Builder

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file(os.path.abspath('main.kv'))
    
    def login(self):
        self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'


    def clear(self):
        self.root.ids.welcome_label.text = 'WELCOME'
        self.root.ids.password.text = ''
        self.root.ids.user.text = ''


MainApp().run()