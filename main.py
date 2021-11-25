
from kivy.config import Config
Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '736')

from kivy.properties import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp


Builder.load_file('Authentication/new_signin.kv')
Builder.load_file('Authentication/old_signin.kv')
Builder.load_file('Profile/profile.kv')
Builder.load_file('Settings/setting.kv')
Builder.load_file('utils.kv')

from Profile.profile import Profile, UserProfile
from Settings.setting import UserSetting
from Authentication.old_signin import OldSignin
from Authentication.new_signin import NewSignin
from utils import Overlay


class Controller(MDScreen):
    pass


class MainApp(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(NewSignin(name='new_signin'))
        sm.add_widget(OldSignin(name='old_signin'))
        sm.add_widget(UserProfile(name='user_profile'))
        sm.add_widget(UserSetting(name='user_setting'))
        return sm


if __name__ == '__main__':
    MainApp().run()
