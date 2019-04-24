import pygame


def get_screen_res():
    pygame.init()
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h
    return width, height
