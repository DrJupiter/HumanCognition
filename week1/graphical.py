import os
from time import perf_counter
from collections import defaultdict


from libmissionaries_and_cannibals import valid_state, Move, state_transition, update_time_dict, bar_plot

import numpy as np

import pygame
from pygame.constants import RESIZABLE, QUIT, VIDEORESIZE, WINDOWFOCUSLOST, KEYDOWN

from pygame.constants import K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_LALT, K_RALT, K_LMETA, K_RMETA

MODS = [K_LSHIFT, K_RSHIFT, K_LCTRL, K_RCTRL, K_LALT, K_RALT, K_LMETA, K_RMETA] 

pygame.display.init()
pygame.display.set_mode([700,400], RESIZABLE)

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

while True:
    pygame.event.pump()
    event = pygame.event.wait()
#    print(event)
    if event.type == QUIT:
       break 
    elif event.type == VIDEORESIZE:
        w, h = pygame.display.get_surface().get_size()
        print(w, h)
        pygame.display.update()

    elif event.type == KEYDOWN:
        move = parse_move_py(event) 
        print(move)
        if move == Move.Quit:
            break



"""
def main(current_state = np.array([3,3,1]), default_dict = defaultdict(lambda: 0), move_list = np.array([0,0,1])):
    
    move_list = np.array([0,0,1])
    start_time = perf_counter()

    while True:
        generate_scene(current_state, move_list)
#        input_move = input("please input move ")
        pygame.event.pump()
        event = pygame.event.await()

        if event.type == KEYDOWN:
            move = parse_move_py(event)

            if move == Move.Boat:
                new_state = state_transition(current_state, move_list)

                if valid_state(new_state):
                    if move_list[0] > 0 or move_list[1] > 0:
                        update_time_dict(default_dict, new_state, start_time, perf_counter())
                        if sum(new_state) == 0:
                            generate_scene(new_state, np.array([0,0,0]))
                            print("GG MATE, ez game ez life")

                            bar_plot(default_dict)
                            exit(0)

                        main(new_state, default_dict)

                    else:
                        input("no people in boat (press enter to continue)")        
                else:
                    input("Cannot move boat due to too many cannibals on one side (press enter to continue)")


            elif move == Move.AddCannibal:
                if current_state[2] == 1:
                    if current_state[1] > move_list[1] and sum(move_list) != 3:
                        move_list += [0,1,0]
                    else: 
                        input("invalid movement of cannibal (press enter to continue)")
                else:
                    if 3-current_state[1] > move_list[1] and sum(move_list) != 3:
                        move_list += [0,1,0]
                    else:
                        input("invalid movement of cannibal (press enter to continue)")

            elif move == Move.RemoveCannibal:
                if move_list[1] != 0:
                    move_list += [0,-1,0]
                else:
                    input("invalid movement of cannibal (press enter to continue)")

            elif move == Move.AddMissionary:
                if current_state[2] == 1:
                    if current_state[0] > move_list[0] and sum(move_list) != 3:
                        move_list += [1,0,0]
                    else:
                        input("invalid movement of missionary  (press enter to continue)")
                else:
                    if 3-current_state[0] > move_list[0] and sum(move_list) != 3:
                        move_list += [1,0,0]
                    else: 
                        input("invalid movement of missionary  (press enter to continue)")

            elif move == Move.RemoveMissionary:
                if move_list[0] != 0:
                    move_list += [-1,0,0]
                else:
                    input("invalid movement of missionary  (press enter to continue)")

            elif move == Move.Invalid:
                input("invalid input (press enter to continue)")
            else:
                continue
"""