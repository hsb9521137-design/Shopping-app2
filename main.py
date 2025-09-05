from kivy.app import App
from kivy.uix.label import Label

class ShoppingApp(App):
    def build(self):
        return Label(text="Welcome to Shopping App!")

if __name__ == "__main__":
    ShoppingApp().run()
