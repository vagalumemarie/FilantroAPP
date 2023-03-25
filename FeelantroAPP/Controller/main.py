from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from Controller.view_controller import ViewController

class FeelantroAPPApp(App):
    def build(self):
        self.view_controller = ViewController()

        layout = BoxLayout()
        layout.add_widget(self.view_controller)

        return layout


if __name__ == '__main__':
    FeelantroAPPApp().run()
