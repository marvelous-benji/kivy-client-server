from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDTextButton
from kivy.properties import Clock



class UserSetting(MDScreen):
    
    def update_email(self):
        icon_btn,email_obj = self.ids.email_container.children
        self.text_field = MDTextField(size_hint_x=0.5,text=self.ids.email.text)
        self.btn = MDTextButton(text="Update",pos_hint={"top":0.5})
        self.ids.email_container.remove_widget(email_obj)
        self.ids.email_container.remove_widget(icon_btn)
        self.ids.email_container.add_widget(self.text_field)
        self.ids.email_container.add_widget(self.btn)
        self.ids.email_container.spacing = 20
        Clock.schedule_once(self.set_focus)
    
    def update_name(self):
        icon_btn,name_obj = self.ids.name_container.children
        self.text_field = MDTextField(text=self.ids.name.text)
        self.btn = MDTextButton(text="Update",pos_hint={"top":0.5})
        self.ids.name_container.remove_widget(name_obj)
        self.ids.name_container.remove_widget(icon_btn)
        self.ids.name_container.add_widget(self.text_field,index=0)
        self.ids.name_container.add_widget(self.btn)
        self.ids.name_container.spacing = 20
        Clock.schedule_once(self.set_focus)

    def set_focus(self,*args):
        self.text_field.focus = True