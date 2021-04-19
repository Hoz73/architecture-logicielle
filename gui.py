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
    card = 0
    bat = 0
    nb_person = 0

    def check_card(self):
        print("_________________________________")
        print("card number : " + str(self.card))
        print("bat 8A door : " + str(self.bat))
    
    def add_person(self):
        self.nb_person += 1
        print("nb person : " + str(self.nb_person))

    def remove_person(self):
        if self.nb_person > 0 :
            self.nb_person -= 1
            print("nb person : " + str(self.nb_person))
        else:
            print("nb person already at 0")


class app(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    app().run()