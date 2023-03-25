from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from Model.data_handler import DataHandler
from Model.request_model import RequestModel
from View.Widgets.ui_button_main import UIButton
from View.Widgets.ui_cell import UICell
from View.Widgets.ui_title import UITitle

class AvailableRequestsView(Screen):
    def __init__(self, **kwargs):
        super(AvailableRequestsView, self).__init__(**kwargs)
        self.scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), do_scroll_x=False)
        self.form = BoxLayout(
            orientation="vertical",
            padding=[100, 50, 100, 100],
            spacing=50,
            size_hint_y=None,
            height=1280
        )
        self.header = BoxLayout(size_hint_y=None, height=100)
        self.switch_request_type = BoxLayout(size_hint_y=None, height=100)
        self.scroll_view_content = BoxLayout(orientation="vertical", spacing=50)


        self.update_request_button = UIButton(text='Оновити', size_hint=[1, 1], on_press=self.update_requests)
        self.exit_button = UIButton(text='Вийти', size_hint=[1, 1], on_press=self.exit)
        self.header.add_widget(self.update_request_button)
        self.header.add_widget(Widget())
        self.header.add_widget(self.exit_button)

        self.request_type_label = UITitle(text='Доступні запити')
        self.request_type_button = UIButton(text='Мої запити', size_hint=[1, 1], on_press=self.switch_screen)
        self.switch_request_type.add_widget(self.request_type_label)
        self.switch_request_type.add_widget(self.request_type_button)

        cloud_data = RequestModel.get_requests_volunteer(self)

        for request in cloud_data:
            self.scroll_view_content.add_widget(UICell(
                text=str(request['location']) + ' - ' + str(request['assistance_category']) + '\n' + str(request['problem_description']) ,
                size_hint=[1, None],
                height=100,
                on_press=self.accept_request
            ))

        self.form.add_widget(self.header)
        self.form.add_widget(self.switch_request_type)
        self.form.add_widget(self.scroll_view_content)
        self.form.add_widget(Widget())
        self.scroll_view.add_widget(self.form)
        self.add_widget(self.scroll_view)


    def exit(self, instance):
        user_info_empty = {}
        DataHandler.write_data(self, data=user_info_empty)
        self.parent.current = 'welcomeView'

    def update_requests(self, instance):
        print()
        #self.parent.current.reload()

    def accept_request(self, instance):
        user_data = DataHandler.read_data(self)
        RequestModel.take_request(user_data['phone'])

        self.update_requests(instance)

    def switch_screen(self, instance):
        self.parent.current = 'acceptedRequestsView'

