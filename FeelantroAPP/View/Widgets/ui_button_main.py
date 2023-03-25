from kivy.uix.button import Button
from kivy.graphics import Color, Line

class UIButton(Button):
    def __init__(self, **kwargs):
        super(UIButton, self).__init__(**kwargs)

        self.background_color = (0, 0, 0, 0)
        self.font_name = 'Helvetica.ttc'
        self.font_size = 30


        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.line = Line(rectangle=(self.x, self.y, self.width, self.height), width=3)

        self.bind(pos=self.update_line, size=self.update_line)

    def update_line(self, *args):
        self.line.rectangle = (
        self.x, self.y, self.width, self.height)










