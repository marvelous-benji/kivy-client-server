from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import Clock



class Profile(MDBoxLayout):
    pass

class UserProfile(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.set_font)

    def set_font(self, *args):
        self.ids.topbar.ids.label_title.font_name = "/home/benji/Kivymd/Frontend/Ubuntu-Regular.ttf"

    def show_settings(self):
        self.manager.current = 'user_setting'