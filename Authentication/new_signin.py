from kivy.config import Config
from kivymd.uix.boxlayout import MDBoxLayout
Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '736')

import json
from kivy.app import App

from kivymd.uix.screen import MDScreen
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from utils import Overlay, failed_response



request_completed = False

class Content(MDBoxLayout):
    pass



class NewSignin(MDScreen):
    dialog = None
    
    def show_password_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Password Reset:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Resend",
                        theme_text_color="Custom",
                        text_color=[0,0,0,1],
                    ),
                    MDFlatButton(
                        text="Reset",
                        theme_text_color="Custom",
                        text_color=[0,0,0,1],
                    ),
                ],
            )
        self.dialog.open()

    def set_validations(self):
        if self.ids.pwd.focus:
            self.ids.eye.text_color = [0,0,0,1]
        elif self.ids.mail.focus:
            pass
        else:
            self.ids.eye.text_color = [0,0,0,0.2]
            if self.ids.pwd.text.strip() and self.ids.mail.text.strip():
                self.ids.signin_btn.disabled = False
            else:
                self.ids.signin_btn.disabled = True

    def submit_request(self):
        print('YOU CALLED ME')
        self.loader = Overlay()
        self.add_widget(self.loader)
        email = self.ids.mail.text
        password = self.ids.pwd.text
        ApiCall.signin_request(email,password)


class EyeIcon(MDIconButton):
    
    def activate_password(self,pwd):
        pwd.focus = True
        if pwd.focus:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            pwd.password = False if pwd.password is True else True



class ApiCall:

    Headers = {
        "Content-Type":"application/json",
        "Accept":"text/plain"
    }
    BASE_URL = "http://localhost:5000"

    @classmethod
    def signin_request(cls,email,password):
        url = cls.BASE_URL + "/user/login"
        body = {
            "username":email,
            "password":password
        }
        req = UrlRequest(url, req_body=json.dumps(body),
                        req_headers=cls.Headers,
                        on_success=cls.signin_success,
                        on_failure=cls.signin_failure,
                        on_progress=cls.signin_progress)

    def signin_progress(self,*args):
        print('progressing')

    def signin_success(self,*args):
        print('success')

    def signin_failure(self,result):
        root = App.get_running_app().root
        overlay = App.get_running_app().root.children[0]
        root.remove_widget(overlay)
        print('failed signin')
        failed_response(result['error'])
