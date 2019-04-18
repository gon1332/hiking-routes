#!/usr/bin/env python
# -*- coding: utf-8 -*-


import networkx as nx
import matplotlib.pyplot as plt


class Point(object):

    """Docstring for Point. """

    def __init__(self, name, location_type):
        self.name = name
        self.location_type = location_type

    def __str__(self):
        return "{} ({})".format(self.name, self.location_type)


class Route(object):

    """Docstring for Route. """

    def __init__(self, point_a, point_b, distance):
        if not isinstance(point_a, Point) or not isinstance(point_b, Point):
            print("point_a and point_b should be of type Point.")
            return None
        self.point_a = point_a
        self.point_b = point_b
        self.distance = distance

    def __str__(self):
        return "({} - {}): {}km".format(self.point_a.name, self.point_b.name,
                                        self.distance)


def find_point(name, points):
    """TODO: Docstring for function:.
    :returns: TODO

    """
    for p in points:
        if name == p.name:
            return p

    return None


class HikingNetwork(object):

    """ Hiking Routes Network. """

    G = None

    def __init__(self, graph):
        """ Fill the graph. """

        print("\nLoaded {}".format(graph['label']))

        # Fill the Graph
        self.G = nx.Graph()

        for n in graph['nodes']:
            point = Point(name=n['id'], location_type=n['metadata']['type'])
            self.G.add_node(point, name=point)

        for e in graph['edges']:
            point_a = find_point(e['source'], self.get_points())
            point_b = find_point(e['target'], self.get_points())
            route = Route(point_a, point_b, e['metadata']['distance'])
            self.G.add_edge(route.point_a, route.point_b, object=route)

    def get_points(self):
        """ Get the network points.

        :returns: list of all points

        """
        return self.G.nodes

    def get_villages(self):
        """ Get the village points.

        :returns: list of all villages

        """
        return [p for p in self.G.nodes if p.location_type == "village"]

    def get_shelters(self):
        """ Get the shelter points.

        :returns: list of all shelter

        """
        return [p for p in self.G.nodes if p.location_type == "shelter"]

    def get_routes(self):
        """ Get the one hop routes.

        :returns: list of all one hop routes

        """
        return self.G.edges

    def draw(self):
        """ Draw the network.

        :returns: None

        """
        pos = nx.spring_layout(self.G)

        # Draw nodes
        options = {
            'font_size': 9,
            'node_color': 'green',
            'node_shape': 's',
            'font_family': 'san-serif',
            'node_size': 50,
        }
        nx.draw_networkx_nodes(self.G, pos, node_list=self.get_villages(),
                               **options)
        nx.draw_networkx_nodes(self.G, pos, node_list=self.get_shelters(),
                               **options)

        for p in pos:
            pos[p][1] += 0.07
        nx.draw_networkx_labels(self.G, pos)

        # Draw edges
        edge_labels = dict([((u, v,), str(d['object'].distance) + "km")
                           for u, v, d in self.G.edges(data=True)])
        nx.draw_networkx_edges(self.G, pos)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        # Show the network
        plt.show()
