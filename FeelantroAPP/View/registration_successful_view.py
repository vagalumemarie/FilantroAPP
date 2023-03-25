from kivy.uix.screenmanager import Screen

from kivy.uix.boxlayout import BoxLayout

from View.Widgets.ui_button_main import UIButton
from View.Widgets.ui_title import UITitle


class RegistrationSuccessfulView(Screen):
    def __init__(self, **kwargs):
        super(RegistrationSuccessfulView, self).__init__(**kwargs)

        self.container = BoxLayout(orientation='vertical', padding=[200])

        self.entry_label = UITitle(text="Вітаємо! Реєстрація пройшла успішно.")
        self.button = UIButton(text="Увійти", size_hint_y=None, height=100, on_press=self.login)

        self.container.add_widget(self.entry_label)
        self.container.add_widget(self.button)

        self.add_widget(self.container)

    def login(self, instance):
        self.parent.current = 'loginView'