import json
import os

from kivy.uix.screenmanager import ScreenManager

from Model.data_handler import DataHandler
from View.accepted_requests import AcceptedRequestsView
from View.available_requests import AvailableRequestsView
from View.create_request_view import CreateRequestView
from View.registration_successful_view import RegistrationSuccessfulView
from View.welcome_view import WelcomeView
from View.sign_up_volunteer_view import SignUpVolunteerView
from View.sign_up_in_need_view import SignUpInNeedView
from View.login_view import LoginView
from View.user_requests_view import UserRequestsView

class ViewController(ScreenManager):
    def __init__(self, **kwargs):
        super(ViewController, self).__init__(**kwargs)
        user_data = DataHandler.read_data(self)

        if not 'state' in user_data:
            self.add_widget(WelcomeView(name='welcomeView'))
        else:
            if user_data['state'] == 'in_need':
                self.add_widget(UserRequestsView(name='userRequests'))
            else:
                self.add_widget(AvailableRequestsView(name='availableRequestsView'))

        self.add_widget(WelcomeView(name='welcomeView'))

        self.add_widget(SignUpVolunteerView(name='signUpVolunteerView'))
        self.add_widget(SignUpInNeedView(name='signUpInNeedView'))
        self.add_widget(LoginView(name='loginView'))
        self.add_widget(RegistrationSuccessfulView(name='registrationSuccessfulView'))

        self.add_widget(UserRequestsView(name='userRequests'))
        self.add_widget(CreateRequestView(name='createRequestView'))

        self.add_widget(AvailableRequestsView(name='availableRequestsView'))
        self.add_widget(AcceptedRequestsView(name='acceptedRequestsView'))
