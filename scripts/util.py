import pygame
import os

def load_image(path):
    image = pygame.image.load(f"data/images/{path}").convert()
    image.set_colorkey((0, 0, 0))
    return image
