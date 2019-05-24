# Built-in modules
from math import sin, cos
import json

# Our third party modules
from build_routes import run_plot
from utils import create_routes_from_nodes

# Kivy modules
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.spinner import Spinner
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.clock import Clock


class MainApp(App):

    def on_spinner_select(self, spinner, text):
        print("You have chosen: " + text)
        if self.spinner.text != "Makrinitsa-Portaria":
            self.spinnerSelection.text = "We have not " + text + " route yet!"
        else:
            self.carousel.load_next()
            self.spinnerSelection.text = self.spinner.text
            Clock.schedule_once(run_plot, 0.5)

    def build(self):
        self.carousel = Carousel(direction='right')
        first_page = GridLayout(cols=1, padding=20)
        second_page = GridLayout(cols=1, padding=20)
        self.carousel.add_widget(first_page)
        self.carousel.add_widget(second_page)

        # Configure first page
        anchor_north = AnchorLayout(anchor_x='center', anchor_y='top')
        anchor_center = AnchorLayout(anchor_x='center', anchor_y='center')
        first_page.add_widget(anchor_north)
        first_page.add_widget(anchor_center)

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

        # Configure second page
        anchor_center_second_page = AnchorLayout(anchor_x='center', anchor_y='center')
        second_page.add_widget(anchor_center_second_page)

        return_home = Button(text="Return home", on_press=lambda a: self.carousel.load_previous(),
                             size=(400, 100), pos=[100, 100], size_hint=(None, None))
        anchor_center_second_page.add_widget(return_home)

        return self.carousel

if __name__ == '__main__':
    MainApp().run()
