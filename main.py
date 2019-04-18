#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pyjsongraph.jsongraph import (validate_schema,
                                   validate_jsongraph,
                                   load_graphs)
import hikingnetwork


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


def main():
    graphs = load_json("pelion_routes.json")
    hiking_net = hikingnetwork.HikingNetwork(next(graphs))

    print("\nPoints:")
    for n in hiking_net.get_points():
        print(" *", n)

    print("\nRoutes:")
    for e in hiking_net.get_routes():
        print(" *", e)

    hiking_net.draw()


if __name__ == '__main__':
    main()
