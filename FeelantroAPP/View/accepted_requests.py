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

class AcceptedRequestsView(Screen):
    def __init__(self, **kwargs):
        super(AcceptedRequestsView, self).__init__(**kwargs)
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
        self.exit_button = UIButton(text='Вийти', size_hint=[1, 1], on_press=self.switch_screen)
        self.header.add_widget(self.update_request_button)
        self.header.add_widget(Widget())
        self.header.add_widget(self.exit_button)

        self.request_type_label = UITitle(text='Мої запити')
        self.request_type_button = UIButton(text='Доступні запити', size_hint=[1, 1], on_press=self.switch_screen)
        self.switch_request_type.add_widget(self.request_type_label)
        self.switch_request_type.add_widget(self.request_type_button)

        self.form.add_widget(self.header)
        self.form.add_widget(self.switch_request_type)


        user_data = DataHandler.read_data(self)

        self.user_data = DataHandler.read_data(self)
        if 'email' in self.user_data:
            cloud_data = RequestModel.get_own_request_volunteer(self, user_data['phone'])

            #in_need_info = RequestModel.get_data_registration_users(self, cloud_data['email'])
            for request in cloud_data:
                self.scroll_view_content.add_widget(UICell(
                    text=str(request['location']) + ' - ' + str(request['assistance_category']) + '\n' +
                         str(request['problem_description']) + ' - ' + str(request['user_phone']) + ' ', #+in_need_info['phone'],
                        size_hint=[1, None],
                        height=100))
        else:
            cloud_data = None


        self.form.add_widget(self.scroll_view_content)
        #self.form.add_widget(Widget())
        self.scroll_view.add_widget(self.form)
        self.add_widget(self.scroll_view)


    def exit(self, instance):
        user_info_empty = {}
        DataHandler.write_data(self, data=user_info_empty)
        self.parent.current = 'welcomeView'

    def update_requests(self, instance):
        print()
        #self.parent.current.reload(instance)

    def switch_screen(self, instance):
        self.parent.current = 'availableRequestsView'


