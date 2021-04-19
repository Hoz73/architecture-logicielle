# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.togglebutton import ToggleButton
# from kivy.uix.button import Button
# from kivy.uix.pagelayout import PageLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.widget import Widget
# from kivy.uix.screenmanager import ScreenManager, Screen

# class LoginScreen(GridLayout):

#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         btn1 = ToggleButton(text='Male', group='sex',)
#         btn2 = ToggleButton(text='Female', group='sex', state='down')
#         btn3 = ToggleButton(text='Mixed', group='sex')
#         self.add_widget(btn1)
#         self.add_widget(btn2)
#         self.add_widget(btn3)

# class Page_Layout(PageLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         self.layout1 = LoginScreen()

#         self.add_widget(self.layout1)

#         self.button2 = Button(
#             text="Page 2"
#         )

#         self.add_widget(self.button2)

#         self.button3 = Button(
#             text="Page 3"
#         )

#         self.add_widget(self.button3)

# class MyApp(App):
#     def build(self):
#         sm
#         return Page_Layout()


# if __name__ == '__main__':
#     MyApp().run()









from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from CustomModules import CustomGraphics
from kivy.uix.screenmanager import SlideTransition

# Builder.load_string("""
# <BuildingScreen>:
#     name: '_building_'

#     GridLayout:
#         cols: 1
#         padding: 5,5,5,5
#         Label:
#             id: title
#             text: "Select a building"
#             width: 40
#             size_hint_y: None
#             color: 0,0,0,1
#         GridLayout:
#             cols: 2
#             Label:
#                 id: building
#                 text: "Hi I'm The Building Screen"
#             Label:
#                 id: building
#                 text: "Hi I'm The Building Screen"
#             Label:
#                 id: building
#                 text: "Hi I'm The Building Screen"
#             Label:
#                 id: building
#                 text: "Hi I'm The Building Screen"
# <ControlPanelScreen>:
#     name: '_control_panel_'
#     Label:
#         id: control_panel
#         text: "Hi I'm The Control panel Screen"
# """)

Builder.load_file('./builder.kv')
sm = ScreenManager()

class BuildingScreen(Screen):
    def switchToControlPanel(self, widget, app):
        print(widget.name)
        print(app)
        sm.transition = SlideTransition(direction='left')
        sm.current = '_control_panel_'
    # def __init__(self, name, **kwargs):
    #     super(BuildingScreen, self).__init__(**kwargs)
    #     self.name = name
    #     layout = GridLayout(cols=2)
    #     layout.add_widget(Button(text='Hello 1'))
    #     layout.add_widget(Button(text='World 1'))
    #     layout.add_widget(Button(text='Hello 2'))
    #     layout.add_widget(Button(text='World 2'))

    #     self.do_layout(layout)


class ControlPanelScreen(Screen):
    def backToBuildings(self):
        print("go back you dumb fuck")
        sm.transition = SlideTransition(direction='right')
        sm.current = '_building_'

class MyApp(App):
    def build(self):
        # Create the screen manager
        sm.add_widget(BuildingScreen(name='_building_'))
        sm.add_widget(ControlPanelScreen(name='_control_panel_'))
        sm.current = '_building_'
        print(sm)
        print(sm.children)

        CustomGraphics.SetBG(sm, bg_color=[0.9,0.9,0.9,1])

        return sm

if __name__ == '__main__':
    MyApp().run()