from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from Model.data_handler import DataHandler
from Model.request_model import RequestModel
from View.Widgets.ui_button_main import UIButton
from View.Widgets.ui_title import UITitle

class UserRequestsView(Screen):
    def __init__(self, **kwargs):
        super(UserRequestsView, self).__init__(**kwargs)
        self.container = BoxLayout(orientation='vertical', padding=[50], spacing=30)
        self.header = BoxLayout(orientation='horizontal', size_hint_y=None, height=100)
        self.scroll_view = ScrollView()
        self.scroll_view_content = BoxLayout(orientation='vertical', padding=[70], spacing=30)

        self.update_request_button = UIButton(text='Оновити', size_hint=[.7, 1], on_press=self.update_request_status)
        self.exit_button = UIButton(text='Вийти', size_hint=[.7, 1], on_press=self.exit)
        self.header.add_widget(self.update_request_button)
        self.header.add_widget(Widget())
        self.header.add_widget(self.exit_button)

        request_button_text = 'Створити запит'
        category_text = 'Тут будуть відображатися'
        describing_text = 'Ваші запити про допомогу.'
        location_text = 'Для створення запиту'
        deadline_text = 'натисніть на кнопку нижче.'
        extra_info_text = ''
        status_text = ''

        self.category_label = UITitle(text=category_text, halign='center')
        self.describing_label = UITitle(text=describing_text, halign='center')
        self.location_label = UITitle(text=location_text, halign='center')
        self.deadline_label = UITitle(text=deadline_text, halign='center')
        self.extra_info_label = UITitle(text=extra_info_text, halign='center')
        self.status_label = UITitle(text=status_text, halign='center')

        self.scroll_view_content.add_widget(self.category_label)
        self.scroll_view_content.add_widget(self.describing_label)
        self.scroll_view_content.add_widget(self.location_label)
        self.scroll_view_content.add_widget(self.deadline_label)
        self.scroll_view_content.add_widget(self.extra_info_label)
        self.scroll_view_content.add_widget(self.status_label)

        self.request_button = UIButton(text=request_button_text, size_hint_y=None, height=100, on_press=self.create_request)

        self.update_request_status(self)

        self.scroll_view_content.add_widget(self.request_button)
        self.scroll_view_content.add_widget(Widget())
        self.scroll_view.add_widget(self.scroll_view_content)

        self.container.add_widget(self.header)
        self.container.add_widget(self.scroll_view)
        self.add_widget(self.container)


    def exit(self, instance):
        user_info_empty = {}
        DataHandler.write_data(self, data=user_info_empty)
        self.parent.current = 'welcomeView'

    def create_request(self, instance):
        self.parent.current = 'createRequestView'

    def update_request_status(self, instance):
        user_data = DataHandler.read_data(self)
        if 'email' in user_data:
            cloud_data = RequestModel.get_own_request(self, user_data['email'])
        else:
            cloud_data = None

        if cloud_data == None:
            request_button_text = 'Створити запит'
            category_text = 'Тут будуть відображатися'
            describing_text = 'Ваші запити про допомогу.'
            location_text = 'Для створення запиту'
            deadline_text = 'натисніть на кнопку нижче.'
            extra_info_text = ''
            status_text = ''
        else:
            request_button_text = 'Редагувати'
            category_text = 'Категорія:\n' + cloud_data['assistance_category']
            describing_text = 'Опис проблеми:\n' + cloud_data['problem_description']
            location_text = 'Місцезнаходження:\n' + cloud_data['location']
            deadline_text = 'Термін виконання:\n' + cloud_data['term_of_execution']
            extra_info_text = 'Додаткова інформація:\n' + cloud_data['additional_contact_information']
            status_text = 'Статус виконання:\n' + cloud_data['status']

        self.request_button.text = request_button_text
        self.category_label.text = category_text
        self.describing_label.text = describing_text
        self.location_label.text = location_text
        self.deadline_label.text = deadline_text
        self.extra_info_label.text = extra_info_text
        self.status_label.text = status_text


