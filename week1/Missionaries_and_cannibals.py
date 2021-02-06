import numpy as np
from time import perf_counter
from collections import defaultdict

""" 
default_dict = defaultdict(lambda: 0)

# returns time snippet bewteen start end append
start = perf_counter()

# INSERT TIMED CODE HERE

default_dict(state, default_dict[state] + perf_counter()-start)
"""

# Calculates new state
def state_transition(state, move):
    
    if state[2] == 0:
        return state + move
    elif state[2] == 1:
        return state - move
    else:
        print("Error, boat state not True or False")

from enum import Enum, unique, auto

@unique
class Move(Enum):
    AddCannibal = auto(),
    RemoveCannibal = auto(),
    AddMissionary = auto(),
    RemoveMissionary = auto(),
    Boat = auto(),
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

print(test_parse_move())
print(test_valid_state())

    
