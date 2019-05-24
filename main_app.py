# Built-in modules
from math import sin, cos
import os
import json

# Our third party modules
from build_routes import run_plot
from utils import create_routes_from_nodes

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

    def on_spinner_select(self, spinner, text):
        print("You chose: " + text)
        if self.spinner.text != "Makrinitsa-Portaria":
            self.spinnerSelection.text = "We have not " + text + " route yet!"
        else:
            self.spinnerSelection.text = self.spinner.text
            run_plot()

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
        with open('./pelion_routes.json') as route_file:
            route_nodes = json.load(route_file)
        routes = create_routes_from_nodes(route_nodes['graph']['edges'])

        self.spinner = Spinner(
            text='Select Route',
            values=routes,
            size=(400, 100), pos=[100, 100], size_hint=(None, None))

        anchor_center.add_widget(self.spinner)
        self.spinner.bind(text=self.on_spinner_select)

        self.spinnerSelection = Label(text="Selected value is: %s" % self.spinner.text)
        anchor_north.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint = {'x': .1, 'y': .3}

        scroll_view.add_widget(layout)
        return scroll_view

if __name__ == '__main__':
    MainApp().run()
