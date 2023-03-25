from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup

from Model.request_model import RequestModel
from View.Widgets.ui_button_back import UIButtonBack
from View.Widgets.ui_button_main import UIButton
from View.Widgets.ui_text_input import UITextInput
from View.Widgets.ui_title import UITitle


class SignUpVolunteerView(Screen):
    def __init__(self, **kwargs):
        super(SignUpVolunteerView, self).__init__(**kwargs)

        self.data_filled_correctly = True

        self.scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), do_scroll_x=False)
        self.form = BoxLayout(
            orientation="vertical",
            padding=[100, 50, 100, 100],
            spacing=20,
            size_hint_y=None,
            height=1280,
        )

        self.have_account_block = BoxLayout(height=100)

        self.header = BoxLayout(height=100)
        self.entry_label = UITitle(text="Реєстрація волонтера")
        self.back_button = UIButtonBack(text="<", on_press=self.back, size_hint=[.2, 1])
        self.header.add_widget(self.back_button)
        self.header.add_widget(self.entry_label)

        self.last_name = UITextInput(hint_text='Прізвище', multiline=False, font_size=40, height=100)
        self.first_name = UITextInput(hint_text='Iм\'я', multiline=False, font_size=40, height=100)
        self.fathers_name = UITextInput(hint_text='По-батькові', multiline=False, font_size=40, height=100)
        self.date_of_birth = UITextInput(hint_text='Дата народження (Формат: 07.07.77)', multiline=False, font_size=40,
                                         height=100)
        self.phone = UITextInput(hint_text='Номер телефону', multiline=False, font_size=40, height=100)
        self.region = UITextInput(hint_text='Регіон проживання', multiline=False, font_size=40, height=100)
        self.city = UITextInput(hint_text='Населений пункт', multiline=False, font_size=40, height=100)
        self.email = UITextInput(hint_text='Електронна пошта', multiline=False, font_size=40, height=100)
        self.password = UITextInput(hint_text='Пароль', multiline=False, font_size=40, height=100, password_mask="* ",
                                    password=True)
        self.confirm_password = UITextInput(hint_text='Підтвердження паролю', multiline=False, font_size=40, height=100,
                                            password_mask=" *", password=True)

        self.next_button = UIButton(text="Зареєструватися")
        self.next_button.bind(on_press=self.switch_screen)

        self.have_account_label = UITitle(text="Маєте\nакаунт?")
        self.have_account_button = UIButton(text="Увійти", on_press=self.open_login)
        self.have_account_block.add_widget(self.have_account_label)
        self.have_account_block.add_widget(self.have_account_button)

        self.error_message = ''

        self.form.add_widget(self.header)

        self.form.add_widget(self.last_name)
        self.form.add_widget(self.first_name)
        self.form.add_widget(self.fathers_name)
        self.form.add_widget(self.date_of_birth)
        self.form.add_widget(self.phone)
        self.form.add_widget(self.region)
        self.form.add_widget(self.city)
        self.form.add_widget(self.email)
        self.form.add_widget(self.password)
        self.form.add_widget(self.confirm_password)

        self.form.add_widget(self.next_button)
        self.form.add_widget(self.have_account_block)

        self.scroll_view.add_widget(self.form)
        self.add_widget(self.scroll_view)

    def switch_screen(self, instance, *args):
        self.error_message = '\n\n\n\n'
        self.data_filled_correctly = True

        if not self.last_name.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели прізвище\n'

        if not self.first_name.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели ім\'я\n'

        if not self.fathers_name.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели по-батькові\n'

        if not self.date_of_birth.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели дату народження\n'

        self.birthday = self.date_of_birth.text
        separators = [' ', '.', '\\', ',', '/']
        is_birthday_filled_correctly = False

        try:
            for separator in separators:
                list_of_numbers = self.birthday.split(separator)
                if len(list_of_numbers) == 3:
                    if len(list_of_numbers[0]) > 0 and len(list_of_numbers[0]) < 3:
                        if len(list_of_numbers[1]) > 0 and len(list_of_numbers[1]) < 3:
                            if len(list_of_numbers[2]) > 1 and len(list_of_numbers[2]) < 5:
                                is_birthday_filled_correctly = True
                                self.birthday = '.'.join(list_of_numbers)
                                break
        except:
            is_birthday_filled_correctly = False

        if not is_birthday_filled_correctly:
            self.data_filled_correctly = False
            self.error_message += 'Формат дати народження: 07.07.77\n'

        if not self.phone.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели номер телефону\n'

        phone_number = self.phone.text
        is_phone_number_filled_correctly = True

        try:
            if phone_number[0] == '+':
                for symbol_number in range(1, len(phone_number)):
                    if not phone_number[symbol_number].isdigit():
                        is_phone_number_filled_correctly = False
            else:
                for symbol_number in range(0, len(phone_number)):
                    if not phone_number[symbol_number].isdigit():
                        is_phone_number_filled_correctly = False

            if len(phone_number) < 7 or len(phone_number) > 15:
                is_phone_number_filled_correctly = False
        except:
            is_phone_number_filled_correctly = False

        if not is_phone_number_filled_correctly:
            self.data_filled_correctly = False
            self.error_message += 'Некоректний формат номера телефону\n'

        if not self.region.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели регіон проживання\n'

        if not self.city.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели населений пункт\n'

        if not self.email.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели електронну пошту\n'

        if not self.password.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не ввели пароль\n'

        if not self.confirm_password.text:
            self.data_filled_correctly = False
            self.error_message += 'Ви не підтвердили пароль\n'

        if not self.password.text == self.confirm_password.text:
            self.data_filled_correctly = False
            self.error_message += 'Паролі не співпадають\n'

        if not self.data_filled_correctly:
            error_content = BoxLayout(orientation='vertical', padding=[200], spacing=40)
            error_text = UITitle(text=self.error_message, color=(1, 1, 1, 1), halign='center')
            error_button = UIButton(text='Закрити', size_hint_y=None, height=100)

            error_content.add_widget(error_text)
            error_content.add_widget(error_button)

            popup = Popup(title='Помилки під час заповнення даних', content=error_content, background_color=(0, 0, 0, 1))
            error_button.bind(on_press=popup.dismiss)
            popup.open()

        if self.data_filled_correctly:
            user_info = {}
            user_info['is_verified'] = 0
            user_info['last_name'] = self.last_name.text
            user_info['first_name'] = self.first_name.text
            user_info['fathers_name'] = self.fathers_name.text
            user_info['date_of_birth'] = self.date_of_birth.text
            user_info['phone'] = self.phone.text
            user_info['region'] = self.region.text
            user_info['city'] = self.city.text
            user_info['email'] = self.email.text
            user_info['password'] = self.password.text

            RequestModel.post_data_registration_volunteer(instance, user_info)

            self.parent.current = 'registrationSuccessfulView'



    def back(self, instance):
        self.parent.current = 'welcomeView'

    def open_login(self, instance):
        self.parent.current = 'loginView'
