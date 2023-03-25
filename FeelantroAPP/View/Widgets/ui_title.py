from kivy.uix.label import Label

class UITitle(Label):
    def __init__(self, **kwargs):
        super(UITitle, self).__init__(**kwargs)

        self.font_name = 'Helvetica.ttc'
        self.font_size = 30