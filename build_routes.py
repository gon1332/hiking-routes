#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pyjsongraph.jsongraph import (validate_schema,
                                   validate_jsongraph,
                                   load_graphs)
import hikingnetwork


class Configuration(object):

    """ Application Configuration """

    def __init__(self, config_json):
        with open(config_json) as f:
            config = json.load(f)

        self.village_conf = config['points']['village']
        self.shelter_conf = config['points']['shelter']


def load_json(routes_json):
    """ Load and validate the json file

    :routes_json: JSON filename containing the routes
    :returns: generator object with the graphs

    """
    with open(routes_json) as f:
        routes = json.load(f)

    print("Does JSON Graph Schema validate?")
    validate_schema(schema='', verbose=True)

    print("\nDoes {} Graph validate?".format(routes_json))
    validate_jsongraph(routes, schema='', verbose=True)

    return load_graphs(routes, validate=False, schema='', verbose=False)


def run_plot(dt):
    config = Configuration("config.json")
    graphs = load_json("pelion_routes.json")
    hiking_net = hikingnetwork.HikingNetwork(next(graphs))

    print("\nPoints:")
    for n in hiking_net.get_points():
        print(" *", n)

    print("\nRoutes:")
    for e in hiking_net.get_routes():
        print(" *", e)

    print(hiking_net.get_shortest_route("Makrinitsa", "Pouri"))

    hiking_net.draw(config)
