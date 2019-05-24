# Built-in modules
import pygame
from typing import Dict, List


def get_screen_res():
    pygame.init()
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h
    return width, height


def create_routes_from_nodes(node_list: Dict) -> List:
    route_edges = []

    for edge in node_list:
        route_edges.append(edge["source"] + '-' + edge["target"])
    return tuple(route_edges)
