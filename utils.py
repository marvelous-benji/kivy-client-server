

from functools import partial
from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty
from kivy.properties import Clock
from kivymd.uix.label import MDLabel
from kivy.animation import Animation



class Overlay(MDBoxLayout):
    rad = NumericProperty(10)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.start_loader)


    def start_loader(self,*args):
        self.anim = Animation(rad=40, d=0.8)
        self.anim += Animation(rad=10, d=0.8)
        self.anim.repeat = True
        self.anim.start(self)
    '''
    def on_rad(self, instance, value):
        if self.rad == 25:
            self.anim.cancel(self)
            print('You cancelled me')
    '''

def failed_response(resp):
    print('Returning response')
    instance = App.get_running_app().root
    lab = MDLabel(text=resp,font_size="18sp",halign="center")
    outline = MDBoxLayout(size_hint=(0.9,0.05),md_bg_color=[0.8,0,0,1],
                    pos_hint={"center_x":0.5,"center_y":0.9},radius=10)
    outline.add_widget(lab)
    instance.add_widget(outline)
    Clock.schedule_once(lambda dt: instance.remove_widget(outline), 1)
