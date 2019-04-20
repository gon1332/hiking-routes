#!/usr/bin/env python
# -*- coding: utf-8 -*-


import networkx as nx
import matplotlib.pyplot as plt


class HikingNetwork(object):

    """ Hiking Routes Network. """

    def __init__(self, graph):
        """ Fill the graph. """

        print("\nLoaded {}".format(graph['label']))

        # Fill the Graph
        self.G = nx.Graph()

        for n in graph['nodes']:
            options = {
                'type': n['metadata']['type'],
            }
            self.G.add_node(n['id'], **options)

        for e in graph['edges']:
            options = {
                'distance': e['metadata']['distance'],
            }
            self.G.add_edge(e['source'], e['target'], **options)

    def get_points(self):
        """ Get the network points.

        :returns: list of all points

        """
        return self.G.nodes

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
        nx.draw_networkx_nodes(self.G, pos, node_list=self.get_points(),
                               **options)

        for p in pos:
            pos[p][1] += 0.07
        nx.draw_networkx_labels(self.G, pos)

        # Draw edges
        edge_labels = dict([((u, v,), str(d['distance']) + "km")
                           for u, v, d in self.G.edges(data=True)])
        nx.draw_networkx_edges(self.G, pos)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        # Show the network
        plt.show()
