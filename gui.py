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
Builder.load_file('./builder.kv')

class MainScreen(BoxLayout):
    bat_8a = 0
    bat_8b = 0
    bat_8c = 0
    nb_person = 0

    def check_card(self):
        print("_________________________________")
        print("bat 8A door : " + str(self.bat_8a))
        print("bat 8B door : " + str(self.bat_8b))
        print("bat 8C door : " + str(self.bat_8c))
        print("nb person : " + str(self.nb_person))
    
class app(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    app().run()