from kivy.uix.screenmanager import Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox

from Model.data_handler import DataHandler
from Model.request_model import RequestModel
from View.Widgets.ui_button_back import UIButtonBack
from View.Widgets.ui_button_main import UIButton
from View.Widgets.ui_text_input import UITextInput
from View.Widgets.ui_title import UITitle


class LoginView(Screen):
    def __init__(self, **kwargs):
        super(LoginView, self).__init__(**kwargs)

        self.form = BoxLayout(
            orientation="vertical",
            size_hint=[.6, .6],
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            padding=[0, 200, 0, 0],
            spacing=40,
        )

        self.header = BoxLayout(size_hint_y=None, height=100)
        self.entry_label = UITitle(text="Увійти")
        self.back_button = UIButtonBack(text="<", on_press=self.back, size_hint=[.2, 1])
        self.header.add_widget(self.back_button)
        self.header.add_widget(self.entry_label)

        self.login_field = UITextInput(hint_text='Електронна пошта', multiline=False, font_size=40, size_hint_y=None, height=100)
        self.password_field = UITextInput(hint_text='Пароль', multiline=False, font_size=40, size_hint_y=None, height=100, password_mask="* ", password=True)

        self.button = UIButton(text="Далi", size_hint_y=None, height=100, on_press=self.login)
        self.error_label = UITitle(text='', color=(1, 0, 0, 1), halign='center')

        self.is_volunteer_field = BoxLayout(size_hint_y=None, height=100)
        self.checkbox = CheckBox(active=True, size_hint=[.05, 1])
        self.is_volunteer_label = UITitle(text="Я волонтер", halign='left', size_hint=[.95, 1])
        self.is_volunteer_field.add_widget(self.checkbox)
        self.is_volunteer_field.add_widget(self.is_volunteer_label)

        self.form.add_widget(self.header)
        self.form.add_widget(self.login_field)
        self.form.add_widget(self.password_field)
        self.form.add_widget(self.is_volunteer_field)
        self.form.add_widget(self.button)
        self.form.add_widget(self.error_label)

        self.add_widget(self.form)

    def back(self, instance):
        self.parent.current = 'welcomeView'

    def login(self, instance):
        self.error_label.text = '\n\n'
        self.email = self.login_field.text
        self.password = self.password_field.text

        if not self.login_field.text:
            self.error_label.text += 'Ви не ввели електронну пошту\n'
        if not self.password_field.text:
            self.error_label.text += 'Ви не ввели пароль\n'

        if self.login_field.text and self.password_field.text:
            self.is_user_volunteer = False
            if self.checkbox.active:
                self.is_user_volunteer = True

            try:
                if self.is_user_volunteer:
                    cloud_data = RequestModel.get_data_registration_volunteer(instance, self.email)
                    cloud_data['state'] = 'volunteer'
                else:
                    cloud_data = RequestModel.get_data_registration_users(instance, self.email)
                    cloud_data['state'] = 'in_need'

                if self.login_field.text == cloud_data['email'] and self.password_field.text == cloud_data['password']:

                    DataHandler.write_data(instance, 'user_data', cloud_data)
                    if cloud_data['state'] == 'in_need':
                        self.parent.current = 'userRequests'
                    else:
                        self.parent.current = 'availableRequestsView'

                else:
                    self.error_label.text += 'Комбінація електронної пошти\nта пароля не співпадають\n'
            except:
                self.error_label.text += 'Комбінація електронної пошти\nта пароля не співпадають\n'
