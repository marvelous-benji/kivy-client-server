from kivy.config import Config
Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '736')
from kivy.properties import ObjectProperty


from kivymd.uix.screen import MDScreen




class OldSignin(MDScreen):
    email_field = ObjectProperty(None)
    fingerprint_field = ObjectProperty(None)

    def on_touch_down(self, touch):
        if (not self.email_field.on_touch_down(touch) and
        not self.fingerprint_field.on_touch_down(touch)):
            touch.ud['initial_x_touch'] = touch.x
        return super().on_touch_down(touch)
    
    def on_touch_move(self, touch):
        if touch.ud.get('initial_x_touch',None) and touch.ud['initial_x_touch'] < touch.x:
            self.manager.transition.direction = 'right'
            self.manager.current ='new_signin'
        return super().on_touch_move(touch)