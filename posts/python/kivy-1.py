"""
pip install kivy
python app.py
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyApp(App):

    def build(self):
        grid = GridLayout()
        grid.cols = 2
        grid.add_widget(Label(text='Hello world'))
        grid.add_widget(Button(text="click"))
        return grid

if __name__ == '__main__':
    MyApp().run()