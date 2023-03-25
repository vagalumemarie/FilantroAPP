from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from View.Widgets.ui_button_main import UIButton

class WelcomeView(Screen):
    def __init__(self, **kwargs):
        super(WelcomeView, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", size_hint=[.7,.7], pos_hint={"center_x": 0.5, "center_y": 0.5}, spacing=30)

        self.label = Label(text="F e e l a n t r o A P P", font_name="Impact", font_size=70)
        self.volunteer_button = UIButton(text="Я волонтер", on_press=self.open_volunteer_form)
        self.in_need_button = UIButton(text="Мені потрібна допомога", on_press=self.open_in_need_form)
        self.have_account_button = UIButton(text="У мене є обліковий запис", on_press=self.open_login)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.volunteer_button)
        self.layout.add_widget(self.in_need_button)
        self.layout.add_widget(self.have_account_button)
        self.add_widget(self.layout)

    def open_volunteer_form(self, instance):
        self.parent.current = 'signUpVolunteerView'

    def open_in_need_form(self, instance):
        self.parent.current = 'signUpInNeedView'

    def open_login(self, instance):
        self.parent.current = 'loginView'
