import pygame
import numpy as np
from pygame.constants import QUIT, RESIZABLE, VIDEORESIZE


from libweek4 import generate_assignments, generate_points, Shape
from graph import circle, cross, render_help_txt_info, render_help_txt_1, render_help_txt_2, render_help_txt_3, generate_scene


width = 800
height = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)

do = 0

assignment = generate_assignments(10, 20)

#print(generate_points((width,height), 10, assignment))

def place_points(point_list, width, height, screen):
    for set in point_list:
        if set[2] == Shape.RedCross:
            cross(set[0], set[1], RED, height, width, screen)

        elif set[2] == Shape.BlueCross:
            cross(set[0], set[1], BLUE, height, width, screen)
        
        elif set[2] == Shape.RedCircle:
            circle(set[0], set[1], RED, height, width, screen)

        elif set[2] == Shape.BlueCircle:
            circle(set[0], set[1], BLUE, height, width, screen)


def generate_scene(screen, width, height, assignment):
    screen.fill(WHITE)

    if do == 0:
        place_points(generate_points((width,height), 10, assignment), width, height, screen)

    elif do == 1:
        render_help_txt_1(screen, txt_config, height, width)
        
    elif do == 2:
        render_help_txt_2(screen, txt_config, height, width)

    elif do == 3:
        render_help_txt_3(screen, txt_config, height, width)

    elif do == 4:
        render_help_txt_info(screen, txt_config, height, width)

    pygame.display.update()


pygame.display.set_caption("Missionaries and Cannibals Problem")

pygame.display.init()
screen = pygame.display.set_mode((width, height),RESIZABLE)
clock = pygame.time.Clock()

pygame.font.init()
txt_config = pygame.font.SysFont('Times New Roman', 40)

# initial display -> generate_scene(state, boat)
screen.fill((255, 255, 255))

generate_scene(screen, width, height, assignment)


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
        generate_scene(screen, width, height, assignment)
        pygame.display.update()