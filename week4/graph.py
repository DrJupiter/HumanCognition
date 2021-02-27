from collections import defaultdict
import pygame
import numpy as np
from pygame.constants import KEYDOWN, QUIT, RESIZABLE, VIDEORESIZE
from libweek4 import TestType, generate_tests, generate_points, Shape, update_time_dict

from enum import Enum, unique

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)

SCALE = 50
THICKNESS = 4

#screen = pygame.display.set_mode([width,height])

def circle(x, y, color, x_resolution, y_resolution, screen):
    pygame.draw.circle(screen,color,(x,y),np.min([x_resolution,y_resolution])/SCALE,THICKNESS)

def cross(x, y, color, x_resolution, y_resolution, screen):
    min_val = np.min([x_resolution,y_resolution])
    scaled_x = min_val/SCALE
    scaled_y = min_val/SCALE
    pygame.draw.line(screen,color,(x-scaled_x, y-scaled_y),(x+scaled_x, y+scaled_y),THICKNESS)
    pygame.draw.line(screen,color,(x+scaled_x, y-scaled_y),(x-scaled_x, y+scaled_y),THICKNESS)

def render_help_txt_info(screen, txt_config, height, width):
    intro_info_txt = [
        txt_config.render("Press \"j\" when you see a target!", False, BLACK),
        txt_config.render("Press \"f\" when you see no target", False, BLACK),
        txt_config.render("Press any key to start the experiment", False, BLACK),
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/8,height/4+i*55))

def render_help_txt_1(screen, txt_config, height, width):
    intro_info_txt = [
        txt_config.render("Welcome to visual search!", False, BLACK),
        txt_config.render("Your reaction time is measured", False, BLACK),
        txt_config.render("So be fast", False, BLACK),
        txt_config.render("But also be precise", False, BLACK),
        txt_config.render("Press any key to continue", False, BLACK)
    ]

    for i in range(len(intro_info_txt)):
        screen.blit(intro_info_txt[i],(width/8,height/4+i*55))

def render_help_txt_2(screen, txt_config, height, width):
    trail_1_info_txt = [
        txt_config.render("Target:", False, BLACK),
        txt_config.render("  X", False, BLUE),
        txt_config.render("or", False, BLACK),
        txt_config.render("  O", False, RED),
        txt_config.render(" ", False, BLACK),
        txt_config.render("Distractor:", False, BLACK),
        txt_config.render("  X", False, RED)
    ]

    for i in range(len(trail_1_info_txt)):
        screen.blit(trail_1_info_txt[i],(width/8,height/4+i*55))

def render_help_txt_3(screen, txt_config, height, width):
    trail_1_info_txt = [
        txt_config.render("Target:", False, BLACK),
        txt_config.render("X", False, BLUE),
        txt_config.render(" ", False, BLACK),
        txt_config.render("Distractors:", False, BLACK),
        txt_config.render("O", False, BLUE),
        txt_config.render("Or:", False, BLACK),
        txt_config.render("X", False, RED)
    ]

    for i in range(len(trail_1_info_txt)):
        screen.blit(trail_1_info_txt[i],(width/8,height/4+i*55))

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

@unique
class Scene(Enum):
    StartGuide   = 0,
    ControlGuide = 1,
    InfoOne      = 2,
    InfoTwo      = 3,
    Playing      = 4,


def generate_scene(screen, width, height, assignment, scene, txt_config):
    screen.fill(WHITE)

    if scene == Scene.Playing:
        place_points(generate_points((width,height), 10, assignment), width, height, screen)

    elif scene == Scene.StartGuide:
        render_help_txt_1(screen, txt_config, height, width)
        
    elif scene == Scene.InfoOne:
        render_help_txt_2(screen, txt_config, height, width)

    elif scene == Scene.InfoTwo:
        render_help_txt_3(screen, txt_config, height, width)

    elif scene == Scene.ControlGuide:
        render_help_txt_info(screen, txt_config, height, width)

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

from time import perf_counter

def main(screen, resolution, txt_config, n_tests, config, test_types, step_size):

    time_dict = defaultdict(lambda: 0)

    width, height = resolution

    generate_scene(screen, width, height, None, Scene.StartGuide, txt_config)

    wait()

    generate_scene(screen, width, height, None, Scene.ControlGuide, txt_config)

    wait()

    for test_type in test_types:
        tests = generate_tests(n_tests, config, test_type, step_size)

        if test_type == TestType.Disjunktion:
            generate_scene(screen, width, height, None, Scene.InfoOne, txt_config)
        elif test_type == TestType.Conjunktion:
            generate_scene(screen, width, height, None, Scene.InfoTwo, txt_config)

        wait()

        for test, target_bool in tests:

            start_time = perf_counter()

            while True:

                generate_scene(screen, width, height, test, Scene.Playing, txt_config) 

                pygame.event.pump()
                event = pygame.event.wait()

                if event.type == QUIT:
                    exit(0)

                elif event.type == KEYDOWN:
                    move = parse_move_py(event)
                    print(move, target_bool)

                    if move == Move.Right:
                        update_time_dict(time_dict, (test_type,len(test)-target_bool, target_bool), start_time, perf_counter())

                        if target_bool:
                            print("Correct")
                        else:
                            print("Incorrect")
                        break

                    elif move == Move.Wrong:

                        update_time_dict(time_dict, (len(test)-target_bool, target_bool), start_time, perf_counter())

                        if not target_bool:
                            print("Correct")
                        else:
                            print("Incorrect")
                        break

                    elif move == Move.Nothing or move == Move.Invalid:
                        continue

                    elif move == Move.Quit:
                        print("Exiting")
                        exit(0)
                elif event.type == VIDEORESIZE:
                    width, height = screen.get_size()
    print(time_dict)


 




if __name__ == "__main__":
    width = 800
    height = 800


    pygame.display.set_caption("Visual Search")

    pygame.display.init()

    pygame.font.init()
    txt_config = pygame.font.SysFont('Times New Roman', 40)

    screen = pygame.display.set_mode((width, height),RESIZABLE)


    screen.fill((255, 255, 255))
    main(screen,(width, height), txt_config, 2, [6, 20, 60], [TestType.Disjunktion, TestType.Conjunktion], 10)