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

print(state_transition(np.array([3,3,1]),np.array([0,2,1])))