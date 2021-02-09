# Copyright Klaus Jupiter Bentzen og Andreas Holme
from collections import defaultdict
from enum import Enum, unique, auto

# !!!! External modules required !!!!
# pip install numpy matplotlib
# to fetch the modules
import matplotlib.pyplot as plt
import numpy as np


# INSERT TIMED CODE HERE
def update_time_dict(default_dict, state, start_time, end_time):
    string_state = f'{state}'
    default_dict[string_state] += end_time - start_time

# Calculates new state
def state_transition(state, move):
    
    if state[2] == 0:
        return state + move
    elif state[2] == 1:
        return state - move
    else:
        print("Error, boat state not True or False")

@unique
class Move(Enum):
    AddCannibal = auto(),
    RemoveCannibal = auto(),
    AddMissionary = auto(),
    RemoveMissionary = auto(),
    Boat = auto(),
    Quit = auto(),
    Nothing = auto(),
    Invalid = auto(),

def parse_move(string: str) -> Move:
    string = string.strip()
    if string == "c":
       return Move.AddCannibal
    elif string == "C":
        return Move.RemoveCannibal
    elif string == "m":
       return Move.AddMissionary
    elif string == "M":
        return Move.RemoveMissionary
    elif string == "b" or string == "B":
        return Move.Boat
    elif string == "q" or string == "Q":
        return Move.Quit
    else:
        # Add a help message for this in the main loop
        return Move.Invalid

def valid_state(state: [int, int, bool]) -> bool:
    if state[0] == 3 or state[0] == 0:
        return True
    elif state[0] >= state[1] and (3-state[0]) >= (3-state[1]):
        return True
    else:
        return False


def state_to_title(state):
    return f"{state[0]*'m'} {state[1]*'c'} {state[2]*'b /~/'} {(1-state[2])*'/~/ b'} {(3-state[0])*'m'} {(3-state[1])*'c'}"

def bar_plot(time_dict): 
    plt.rcdefaults()
    states = []
    times = []
    for key, val in time_dict.items():
        state = list(map(int, key[1:len(key)-1].split()))
        states.append(state_to_title(state))
        times.append(val)
    

    plt.title('c = cannibal, m = missionary, /~/ = river, b = boat')
    plt.suptitle('Missionary and Cannibals', fontsize = 14, fontweight='bold')
    plt.xlabel('State')
    plt.ylabel('Time Spent in a State in Seconds')
    plt.bar(states, times, color='red')
    print(f"Total time spent = {sum(times)} s")
    print("items =", time_dict.items())
    print(len(time_dict))
    plt.show()

import csv    
def to_csv(default_dict):
    
    lines = []
    lines.append(["[Missionay, Cannibals, boat] on left","time_spent"])
    for key, val in default_dict.items():
        state_line = []
        state = list(map(int, key[1:len(key)-1].split()))
        state_line.append(state)
        state_line.append(val)
        lines.append(state_line)

    with open('Miss_and_cann_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    
    #print(f"lines = {lines}")


### Test functions:

def test_time_dict() -> bool:
    input_state = [np.array([3,3,1]),np.array([0,0,0]),np.array([3,3,1])]
    input_start_time = [2,17,4]
    input_end_time = [4,7,5]
    default_dict = defaultdict(lambda:0)
    for i in range(len(input_state)):
        update_time_dict(default_dict, input_state[i],input_start_time[i],input_end_time[i])
    
    #print(default_dict)
    #print(default_dict[f'{np.array([3,3,1])}'])
    
    if default_dict[f'{np.array([3,3,1])}'] == 3 and default_dict[f'{np.array([0,0,0])}'] == -10:
        return True
    else:
        return False

def test_state_transition() -> bool:
    input1 = [np.array([3,3,1]),np.array([0,2,0])]
    input2 = [np.array([0,2,1]),np.array([1,1,1])]
    expected = [np.array([3,1,0]), np.array([1,3,1])]

    for i in range(len(input1)):
        comparison = state_transition(input1[i], input2[i]) == expected[i]
        if comparison.all() == True:
            return True
        else:
            return False

def test_parse_move() -> bool:
    inputs = [' m ', '   M ', 'c', 'C', 'b', '123123123123']
    expected_moves = [Move.AddMissionary, Move.RemoveMissionary, Move.AddCannibal, Move.RemoveCannibal, Move.Boat, Move.Invalid]
    for move, e_move in zip(inputs, expected_moves):
        if parse_move(move) == e_move:
            continue
        else:
            return False
    return True

def test_valid_state() -> bool:
    states = [[3,3,0], [1,2,0], [2,2,0], [2,1,0]]
    e = [True, False, True, False]
    for state, e_bool in zip(states, e):
        if valid_state(state) == e_bool:
            continue
        else:
            return False
    return True

#print(test_time_dict())
#print(test_state_transition())
#print(test_parse_move())
#print(test_valid_state())