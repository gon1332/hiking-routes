# Built-in modules
import pytest

# Our third party modules
from utils import create_routes_from_nodes


def test_create_routes_from_nodes():
    route_list = [{"source": "Makrinitsa", "target": "Portaria"},
                  {"source": "Pouri", "target": "Portaria"}]

    route_tuple = create_routes_from_nodes(route_list)
    assert route_tuple == ("Makrinitsa-Portaria", "Pouri-Portaria")
