# Built-in modules
from math import sin, cos
import os

# Our third party modules
from build_routes import run_plot

# Kivy modules
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner


class MainApp(App):

    def build(self):
        scroll_view = ScrollView()
        layout = GridLayout(cols=1, padding=20)

        anchor_north = AnchorLayout(anchor_x='center', anchor_y='top')
        anchor_center = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_south = AnchorLayout(anchor_x='center', anchor_y='bottom')
        layout.add_widget(anchor_north)
        layout.add_widget(anchor_center)
        layout.add_widget(anchor_south)

        # Configure spinner object
        # TODO: read routes from json
        self.spinner = Spinner(
            text='Select Route',
            values=('Makrinitsa-Portaria',
                    'Makrinitsa-Stagiates',
                    'Stagiates-Portaria',
                    'Makrinitsa-West shelter'),
            size=(400, 100), pos=[100, 100], size_hint=(None, None))

        anchor_center.add_widget(self.spinner)
        self.spinner.bind(text=self.on_spinner_select)

        self.spinnerSelection = Label(text="Selected value in spinner is: %s" % self.spinner.text)
        anchor_north.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint = {'x': .1, 'y': .3}

        scroll_view.add_widget(layout)
        return scroll_view

    def on_spinner_select(self, spinner, text):
        print("You chose: " + text)
        if self.spinner.text != "Makrinitsa-Portaria":
            self.spinnerSelection.text = "You chose " + text + ". We have not this route yet!"
        else:
            self.spinnerSelection.text = self.spinner.text
            run_plot()


if __name__ == '__main__':
    MainApp().run()
