from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class UICell(Button):
    def __init__(self, **kwargs):
        super(UICell, self).__init__(**kwargs)

        self.background_color = (1, 1, 1, 1)
        self.background_normal = ''
        self.font_name = 'Helvetica.ttc'
        self.font_size = 30
        self.color = (0, 0, 0, 1)




