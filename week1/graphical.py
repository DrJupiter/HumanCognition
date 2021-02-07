import os
from render_py import generate_scene
from time import perf_counter
from collections import defaultdict


from libmissionaries_and_cannibals import valid_state, Move, state_transition, update_time_dict, bar_plot

import numpy as np

import pygame
from pygame.constants import RESIZABLE, QUIT, VIDEORESIZE, WINDOWFOCUSLOST, KEYDOWN

from pygame.constants import K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_LALT, K_RALT, K_LMETA, K_RMETA

MODS = [K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_LALT, K_RALT, K_LMETA, K_RMETA] 



def parse_move_py(event) -> Move:
    mods = pygame.key.get_mods()
    print(mods, event.key)
    if event.key == pygame.K_q:
        return Move.Quit
    elif event.key == pygame.K_c:
        if mods & pygame.KMOD_RSHIFT or mods & pygame.KMOD_LSHIFT:
            return Move.RemoveCannibal
        else:
            return Move.AddCannibal
    elif event.key == pygame.K_m:
        if mods & pygame.KMOD_RSHIFT or mods & pygame.KMOD_LSHIFT:
            return Move.RemoveMissionary
        else:
            return Move.AddMissionary
    elif event.key == pygame.K_b:
        return Move.Boat
    else:
        if event.key in MODS:
            return Move.Nothing

        return Move.Invalid

#while True:
#    pygame.event.pump()
#    event = pygame.event.wait()
##    print(event)
#    if event.type == QUIT:
#       break 
#    elif event.type == VIDEORESIZE:
#        w, h = pygame.display.get_surface().get_size()
#        print(w, h)
#        pygame.display.update()
#
#    elif event.type == KEYDOWN:
#        move = parse_move_py(event) 
#        print(move)
#        if move == Move.Quit:
#            break

def main(current_state = np.array([3,3,1]), default_dict = defaultdict(lambda: 0), move_list = np.array([0,0,1]), err=""):

    generate_scene(current_state, move_list, screen, width, height, txt_config, err) 
    move_list = np.array([0,0,1])
    start_time = perf_counter()

    while True:

        generate_scene(current_state, move_list, screen, width, height, txt_config, err) 


        pygame.event.pump()
        event = pygame.event.wait()

        if event.type == QUIT:
            exit(0)

        elif event.type == KEYDOWN:
            move = parse_move_py(event)

            if move == Move.Boat:
                new_state = state_transition(current_state, move_list)

                if valid_state(new_state):
                    if move_list[0] > 0 or move_list[1] > 0:
                        update_time_dict(default_dict, new_state, start_time, perf_counter())
                        if sum(new_state) == 0:
                            generate_scene(new_state, np.array([0,0,1]), screen, width, height, txt_config, err) 
                            print("GG MATE, ez game ez life")

                            bar_plot(default_dict)
                            exit(0)

                        main(new_state, default_dict, err=err)

                    else:
                        err = "No people in boat"        
                else:
                    err = "This movement results in too many cannibals on one side"


            elif move == Move.AddCannibal:
                if current_state[2] == 1:
                    if current_state[1] > move_list[1] and sum(move_list) != 3:
                        move_list += [0,1,0]
                    else: 
                        err = "Invalid movement of cannibal"
                else:
                    if 3-current_state[1] > move_list[1] and sum(move_list) != 3:
                        move_list += [0,1,0]
                    else:
                        err = "Invalid movement of cannibal"

            elif move == Move.RemoveCannibal:
                if move_list[1] != 0:
                    move_list += [0,-1,0]
                else:
                    err = "Invalid movement of cannibal"

            elif move == Move.AddMissionary:
                if current_state[2] == 1:
                    if current_state[0] > move_list[0] and sum(move_list) != 3:
                        move_list += [1,0,0]
                    else:
                        err = "Invalid movement of missionary "
                else:
                    if 3-current_state[0] > move_list[0] and sum(move_list) != 3:
                        move_list += [1,0,0]
                    else: 
                        err = "Invalid movement of missionary "

            elif move == Move.RemoveMissionary:
                if move_list[0] != 0:
                    move_list += [-1,0,0]
                else:
                    err = "Invalid movement of missionary "

            elif move == Move.Invalid:
                err = "Invalid input"

            elif move == Move.Quit:
                exit(0)
            else:
                continue

pygame.display.init()
width, height = 500, 500
screen = pygame.display.set_mode([width,height])
pygame.font.init()
txt_config = pygame.font.SysFont('Times New Roman', 20)

main()