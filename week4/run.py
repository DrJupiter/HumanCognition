import pygame
import numpy as np
from pygame.constants import QUIT, RESIZABLE, VIDEORESIZE

from libweek4 import generate_assignments, generate_points
from graph import circle, cross, render_help_txt_info, render_help_txt_1, render_help_txt_2, render_help_txt_3, generate_scene


width = 800
height = 800



assignment = generate_assignments(10, 20)

print(generate_points((width,height), 10, assignment))



pygame.display.set_caption("Missionaries and Cannibals Problem")

pygame.display.init()
screen = pygame.display.set_mode((width, height),RESIZABLE)
clock = pygame.time.Clock()

pygame.font.init()
txt_config = pygame.font.SysFont('Times New Roman', 40)

# initial display -> generate_scene(state, boat)
screen.fill((255, 255, 255))

generate_scene(screen, width, height)


pygame.display.update()

pygame.display.update()
while True:
    pygame.event.pump()
    event = pygame.event.wait()

    if event.type == QUIT:
        break
    
    elif event.type == VIDEORESIZE:
        width, height = pygame.display.get_surface().get_size()
        # resize
        # get width and height
        screen.fill((255, 255, 255))
        generate_scene(screen, width, height)
        pygame.display.update()