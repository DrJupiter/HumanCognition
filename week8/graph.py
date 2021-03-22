from collections import defaultdict
import pygame
import numpy as np
from pygame.constants import KEYDOWN, QUIT, RESIZABLE, VIDEORESIZE

from enum import Enum, unique

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,150,0)

SCALE = 50
THICKNESS = 3

def circle(x, y, color, x_resolution, y_resolution, screen):
    pygame.draw.circle(screen,color,(x,y),np.min([x_resolution,y_resolution]),THICKNESS)

def render_help_txt_info(screen, txt_config, height, width):
    intro_info_txt = [
        txt_config.render("Press \"j\" when you see a target!", False, BLACK),
        txt_config.render("Press \"f\" when you see no target", False, BLACK),
        txt_config.render("Press any key to start the experiment", False, BLACK),
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/8,height/4+i*55))
        
@unique
class Scene(Enum):
    StartGuide   = 0,
    ControlGuide = 1,
    InfoOne      = 2,
    InfoTwo      = 3,
    Playing      = 4,
    Wrong        = 5,
    Correct      = 6,

def generate_points_learn(resolution, matrix ):
    w, h = resolution

    points = []
    for plot_vec in matrix:
        circle(plot_vec[0], plot_vec[1], RED, w, h, screen)
        circle(plot_vec[2], plot_vec[3], BLUE, w, h, screen)    
        circle(plot_vec[4], plot_vec[5], GREEN, w, h, screen)

    return points

def generate_points_play(resolution, step_size, assignment):

    w, h = resolution

    points = []


    return points

def generate_scene(screen, width, height, step_size, assignment, scene, txt_config):
    screen.fill(WHITE)

    if scene == Scene.Playing:
        place_points(generate_points((width,height), step_size, assignment), width, height, screen, step_size)

    pygame.display.update()

from pygame.constants import K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_LALT, K_RALT, K_LMETA, K_RMETA

MODS = [K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_LALT, K_RALT, K_LMETA, K_RMETA] 

@unique
class Move(Enum):
    Wrong = 0,
    Right = 1,
    Quit  = 2,
    Nothing = 3
    Invalid = 4,

def parse_move_py(event) -> Move:
    if event.key == pygame.K_q:
        return Move.Quit
    elif event.key == pygame.K_j:
        return Move.Right
    elif event.key == pygame.K_f:
        return Move.Wrong
    else:
        if event.key in MODS:
            return Move.Nothing
        return Move.Invalid

def wait():
    while True:
        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)
        elif event.type == KEYDOWN:
            break                

from time import perf_counter, sleep



def main(screen, resolution, txt_config, n_tests, config, test_types, step_size):

    if fisk == fisk:
        return None

    elif move == Move.Quit:
        print("Exiting")
        exit(0)

    elif event.type == VIDEORESIZE:
        width, height = screen.get_size()


if __name__ == "__main__":
    width = 800
    height = 800


    pygame.display.set_caption("Visual Search")

    pygame.display.init()

    pygame.font.init()
    txt_config = pygame.font.SysFont('Times New Roman', 40)

    screen = pygame.display.set_mode((width, height),RESIZABLE)


    screen.fill((255, 255, 255))
    main(screen,(width, height), txt_config, 10, [6, 20, 60], [TestType.Disjunktion, TestType.Conjunktion], 30)

    # add delay between states

