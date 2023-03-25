from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.widget import Widget

from Model.data_handler import DataHandler
from Model.request_model import RequestModel
from View.Widgets.ui_button_back import UIButtonBack
from View.Widgets.ui_button_main import UIButton
from View.Widgets.ui_text_input import UITextInput
from View.Widgets.ui_title import UITitle


class CreateRequestView(Screen):
    def __init__(self, **kwargs):
        super(CreateRequestView, self).__init__(**kwargs)
        self.scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), do_scroll_x=False)
        self.form = BoxLayout(
            orientation="vertical",
            padding=[100, 50, 100, 100],
            spacing=20,
            size_hint_y=None,
            height=1280,
        )

        self.header = BoxLayout(size_hint_y=None, height=100)
        self.entry_label = UITitle(text="Створення запиту")
        self.back_button = UIButtonBack(text="<", on_press=self.back, size_hint=[.2, 1])
        self.header.add_widget(self.back_button)
        self.header.add_widget(self.entry_label)

        self.category = UITextInput(hint_text='Категорія допомоги*', multiline=False, font_size=40, size_hint_y=None, height=100)
        self.describing = UITextInput(hint_text='Опис проблеми*', multiline=False, font_size=40, size_hint_y=None, height=100)
        self.location = UITextInput(hint_text='Місцезнаходження*', multiline=False, font_size=40, size_hint_y=None, height=100)
        self.deadline = UITextInput(hint_text='Термін виконання (днiв)', multiline=False, font_size=40, size_hint_y=None, height=100)
        self.extra_info = UITextInput(hint_text='Додаткова контактна інформація', multiline=False, font_size=40, size_hint_y=None, height=100)
        self.submit_button = UIButton(text='Створити запит', size_hint_y=None, height=100, on_press=self.create_request)
        self.delete_button = UIButton(text='Видалити запит', size_hint_y=None, height=100, on_press=self.delete_request, opacity=0)

        self.user_data = DataHandler.read_data(self)
        if 'email' in self.user_data:
            self.cloud_data = RequestModel.get_own_request(self, self.user_data['email'])
        else:
            self.cloud_data = None

        if not self.cloud_data == None:
            self.category.text = self.cloud_data['assistance_category']
            self.describing.text = self.cloud_data['problem_description']
            self.location.text = self.cloud_data['location']
            self.deadline.text = self.cloud_data['term_of_execution']
            self.extra_info.text = self.cloud_data['additional_contact_information']
            self.delete_button.opacity = 1
            self.submit_button.text = 'Редагувати запит'

        self.form.add_widget(self.header)

        self.form.add_widget(self.category)
        self.form.add_widget(self.describing)
        self.form.add_widget(self.location)
        self.form.add_widget(self.deadline)
        self.form.add_widget(self.extra_info)
        self.form.add_widget(self.submit_button)
        self.form.add_widget(self.delete_button)
        self.form.add_widget(Widget())

        self.scroll_view.add_widget(self.form)
        self.add_widget(self.scroll_view)

    def back(self, instance):
        self.parent.current = 'userRequests'


    def create_request(self, instance):
        data_filled_correctly = True
        request_data = {}

        if not self.category.text:
            self.data_filled_correctly = False
        if not self.describing.text:
            self.data_filled_correctly = False
        if not self.location.text:
            self.data_filled_correctly = False

        if data_filled_correctly:
            request_data['assistance_category'] = self.category.text
            request_data['problem_description'] = self.describing.text
            request_data['location'] = self.location.text
            request_data['term_of_execution'] = self.deadline.text
            request_data['additional_contact_information'] = self.extra_info.text
            request_data['email'] = self.user_data['email']
            request_data['user_phone'] = self.user_data['phone']

            if self.cloud_data == None:
                request_data['volunteer_phone'] = '0'
                request_data['status'] = '0'

                RequestModel.post_data_request(self, request_data)
            else:
                RequestModel.edit_data_request(self, request_data)

            self.parent.current = 'userRequests'

    def delete_request(self, instance):
        user_data = DataHandler.read_data()
        if not self.cloud_data == None:
            RequestModel.delete_data_request(self, user_data['email'])