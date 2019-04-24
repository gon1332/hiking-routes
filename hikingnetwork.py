#!/usr/bin/env python
# -*- coding: utf-8 -*-


import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import utils


class HikingNetwork(object):

    """ Hiking Routes Network. """

    def __init__(self, graph):
        """ Fill the graph. """

        print("\nLoaded {}".format(graph['label']))

        self.G = nx.Graph()

        # Fill the Graph with points
        for n in graph['nodes']:
            options = {
                'type': n['metadata']['type'],
            }
            self.G.add_node(n['id'], **options)

        # Villages subgraph
        self.G_villages = self.G.subgraph([n[0] for n in self.G.nodes.data() if
                                           n[1]['type'] == "village"])
        # Shelters subgraph
        self.G_shelters = self.G.subgraph([n[0] for n in self.G.nodes.data() if
                                           n[1]['type'] == "shelter"])

        # Fill the Graph with edges
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

    def get_shortest_route(self, point_a, point_b):
        """ Get the shortest route between two points.

        :returns: list of one hop routes for the shortest route

        """
        return shortest_path(self.G, point_a, point_b, "distance")

    def _draw_villages(self, pos, options):
        nx.draw_networkx_nodes(self.G_villages, pos,
                               node_list=self.G_villages,
                               **options)

    def _draw_shelters(self, pos, options):
        nx.draw_networkx_nodes(self.G_shelters, pos,
                               node_list=self.G_shelters,
                               **options)

    def _draw_legend(self, config):
        village_point = mlines.Line2D([], [],
                                      color=config.village_conf['node_color'],
                                      marker=config.village_conf['node_shape'],
                                      markersize=10, linestyle='',
                                      label='village')

        shelter_point = mlines.Line2D([], [],
                                      color=config.shelter_conf['node_color'],
                                      marker=config.shelter_conf['node_shape'],
                                      markersize=10, linestyle='',
                                      label='shelter')
        plt.legend(loc="lower left", handles=[village_point, shelter_point])

    def draw(self, config):
        """ Draw the network.

        :returns: None

        """
        dpi = 180
        w, h = utils.get_screen_res()
        plt.figure(1, figsize=(w/dpi, w/dpi))
        pos = nx.spring_layout(self.G)

        # Draw nodes
        self._draw_villages(pos, config.village_conf)
        self._draw_shelters(pos, config.shelter_conf)

        # Draw edges
        edge_labels = dict([((u, v,), str(d['distance']) + "km")
                           for u, v, d in self.G.edges(data=True)])
        nx.draw_networkx_edges(self.G, pos)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        for p in pos:
            pos[p][1] += 0.07
        nx.draw_networkx_labels(self.G, pos)

        self._draw_legend(config)

        # Subplot settings
        plt.subplots_adjust(
            left=0.0,
            right=0.95,
            bottom=0.0,
            top=0.95,
            wspace=0.2,
            hspace=0.2)

        # Show the network
        plt.axis('off')
        plt.suptitle('Pelion routes')
        plt.show()
