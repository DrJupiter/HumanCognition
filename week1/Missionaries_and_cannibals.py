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

#print(state_transition(np.array([3,3,1]),np.array([0,2,1])))

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


def test_parse_move() -> bool:
    inputs = [' m ', '   M ', 'c', 'C', 'b', '123123123123']
    expected_moves = [Move.AddMissionary, Move.RemoveMissionary, Move.AddCannibal, Move.RemoveCannibal, Move.Boat, Move.Invalid]
    for move, e_move in zip(inputs, expected_moves):
        if parse_move(move) == e_move:
            continue
        else:
            return False
    return True
    

print(test_parse_move())

    
