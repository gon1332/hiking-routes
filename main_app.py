from math import sin, cos
import os

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.lang import Builder


class Plot(RelativeLayout):
    def __init__(self, **kwargs):
        super(Plot, self).__init__(**kwargs)
        self.graph = Graph(xlabel="x", ylabel="y", x_ticks_minor=5,
                           x_ticks_major=25, y_ticks_major=1,
                           y_grid_label=True, x_grid_label=True,
                           x_grid=True, y_grid=True,
                           xmin=-0, xmax=100, ymin=-1,
                           ymax=1, draw_border=False)

        self.plot = MeshLinePlot(color=[1, 1, 1, 1])
        self.plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        self.plot2 = MeshLinePlot(color=[1, 0, 0, 1])
        self.plot2.points = [(x, cos(x / 10.)) for x in range(0, 101)]
        self.add_widget(self.graph)

        self.graph.add_plot(self.plot)
        self.graph.add_plot(self.plot2)

    def exit_app(self, obj):
        App.get_running_app().stop()


class MainApp(App):

    def build(self):
        scroll_view = ScrollView()
        grid_layout = GridLayout(cols=1, padding=20, spacing=20)
        grid_layout.bind(minimum_size=grid_layout.setter('size'))
        label = Label(text="Pelion Routes!", size_hint_y=None)

        graph = Plot(size_hint_y=None, height=500)

        spinner = Spinner(
            text='Select Route',
            values=('Makrinitsa-Portaria',
                    'Makrinitsa-Stagiates',
                    'Stagiates-Portaria',
                    'Makrinitsa-West shelter'),
            size_hint=(None, None), size=(400, 100),
            pos=[200, 200])

        def show_selected_value(spinner, text):
            print('The spinner', spinner, 'has text', text)

        spinner.bind(text=show_selected_value)
        grid_layout.add_widget(label)
        grid_layout.add_widget(graph)
        grid_layout.add_widget(spinner)
        scroll_view.add_widget(grid_layout)

        return scroll_view

if __name__ == '__main__':
    MainApp().run()
