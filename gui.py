from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from CustomModules import CustomGraphics
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.graphics import Ellipse
from kivy.graphics import Triangle
from kivy.graphics import Color

import time

Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Builder.load_file('./builder.kv')




class MainScreen(BoxLayout):
    card = 0
    bat = 0
    nb_person = 0

    WHITE = [1,1,1,1]
    RED = [1,0,0,1]
    GREEN = [0,1,0,1]
    FIRE = [1,0,0,1]

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

    def redraw(self, green, red, fire):
        c = self.ids.floatlayout.canvas
        with c:
            c.get_group('a').clear()
            Color(green[0], green[1], green[2], green[3])
            c.add(Ellipse(pos=(112, 418), size=(80, 80)))
        
            Color(red[0], red[1], red[2], red[3])
            c.add(Ellipse(pos=(112, 320), size=(80, 80)))

            Color(fire[0], fire[1], fire[2], fire[3])
            c.add(Triangle(points=(112,218,152,298,192,218)))

        

    def change_to_green(self):
        self.redraw(self.GREEN, self.WHITE, self.WHITE)

    def change_to_red(self):
        self.redraw(self.WHITE, self.RED, self.WHITE)

    def change_to_fire(self):
        self.redraw(self.WHITE, self.WHITE, self.FIRE)

    def change_to_white(self):
        self.redraw(self.WHITE, self.WHITE, self.WHITE)
    
class app(App):

    def build(self):
        return MainScreen()
