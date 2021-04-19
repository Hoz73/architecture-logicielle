from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from CustomModules import CustomGraphics
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Builder.load_file('./test_builder.kv')

class MainScreen(BoxLayout):
    pass
    
class app(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    app().run()