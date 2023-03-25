from kivy.uix.textinput import TextInput

class UITextInput(TextInput):
    def __init__(self, **kwargs):
        super(UITextInput, self).__init__(**kwargs)

        self.background_normal = ''
        self.background_color = (1, 1, 1, 0.2)

        self.font_name = 'Helvetica.ttc'
        self.font_size = 30

        self.foreground_color = (1, 1, 1, 0.8)
        self.hint_text_color = (1, 1, 1, 0.3)
        self.cursor_color = ((1, 1, 1, 0.8))




