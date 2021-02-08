import os
from time import perf_counter
from collections import defaultdict

from libmissionaries_and_cannibals import parse_move, valid_state, Move, state_transition, update_time_dict, bar_plot

import numpy as np

from getch import _Getch as Getch

_getch = Getch()

def generate_scene(state, boat):
    os.system('cls' if os.name == 'nt' else 'clear')


    #print("""
    #    m -> move missionary INTO boat, M -> move missionary FROM boat\n
    #    c -> move cannibal INTO boat, C -> move cannibal FROM boat\n
    #    b or B -> move boat to the other side and unload its passengers\n 
    #    """
    #    )

    print(""" m -> move missionary INTO boat, M -> move missionary FROM boat\n c -> move cannibal INTO boat, C -> move cannibal FROM boat\n b or B -> move boat to THE OTHER SIDE and unload its passengers\n""")

    ws = 10
    fill = f"{' '*ws}"

    rs = 15
    river = f"/{'~'*rs}/"

    line = f"|{fill}{river}{fill}|"
    ls = 5

    if state[2] == 1:
        lstate = state - boat + np.array([0,0,1])
        rstate = state
    else:
        rstate = state + boat - np.array([0, 0, 1])
        lstate = state

    boat = f"{boat[0]*'m'}{boat[1]*'c'}{' '*(2-sum(boat[:2]))}"    

    left_side_o = f"{lstate[0]*'m'}"
    left_side_u =  f"{lstate[1]*'c'}"

    right_side_o = f"{(3-rstate[0])*'m'}"
    right_side_u = f"{(3-rstate[1])*'c'}"
    if state[2] == 1:
        rivermidle_o = f"/{boat}{'~'*(rs-2)}/"
        rivermidle_u = f"/⎻⎻{'~'*(rs-2)}/"
        middle_o = f"|{(ws - len(left_side_o))*' '}{left_side_o}{rivermidle_o}{right_side_o}{(ws-len(right_side_o))*' '}|\n"
        middle_u = f"|{(ws - len(left_side_u))*' '}{left_side_u}{rivermidle_u}{right_side_u}{(ws-len(right_side_u))*' '}|\n"
    else:
        rivermidle_o = f"/{'~'*(rs-2)}{boat}/"
        rivermidle_u = f"/{'~'*(rs-2)}⎻⎻/"
        middle_o = f"|{(ws - len(left_side_o))*' '}{left_side_o}{rivermidle_o}{right_side_o}{(ws-len(right_side_o))*' '}|\n"
        middle_u = f"|{(ws - len(left_side_u))*' '}{left_side_u}{rivermidle_u}{right_side_u}{(ws-len(right_side_u))*' '}|\n"
    

    print(f"{line}\n"*ls, end='\b')
    print(middle_o, end='\b')
    print(middle_u, end='\b')
    print(f"{line}\n"*ls, end='\b')



def main(current_state = np.array([3,3,1]), default_dict = defaultdict(lambda: 0), move_list = np.array([0,0,1])):
    
    #print(current_state)
    move_list = np.array([0,0,1])
    start_time = perf_counter()

    while True:
        generate_scene(current_state, move_list)
#        input_move = input("please input move ")
        input_move = _getch()
        move = parse_move(input_move)

        if move == Move.Boat:
            new_state = state_transition(current_state, move_list)
    
            if valid_state(new_state):
                if move_list[0] > 0 or move_list[1] > 0:
                    update_time_dict(default_dict, current_state, start_time, perf_counter())
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

        else:
            input("invalid input (press enter to continue)")

if __name__ == "__main__":
    main()