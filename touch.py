from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Mouse(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        print("Mouse Up", touch)
        self.btn.opacity = 1

class TouchApp(App):
    def build(self):
        return Mouse()


if __name__ == "__main__":
    TouchApp().run()