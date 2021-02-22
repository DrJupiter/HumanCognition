

from collections import defaultdict 
from enum import Enum, unique


import random

from math import floor

@unique
class Shape(Enum):
    RedCross   = 0,
    BlueCross  = 1,
    RedCircle  = 2,
    BlueCircle = 3,


def generate_pairs(n_pairs, low, high):
    pairs = []
    
    for _ in range(n_pairs):
        pairs.append((random.randint(low, high), random.randint(low, high)))
    
    return pairs

def assignment(offsets, n_tiles, type_dict, fill_type):
    miss_counter = 0
    for o in offsets:
        if type_dict[o] == 0:
            type_dict[o] = fill_type # where 3 is a red cross
        else:
            miss_counter += 1
    if miss_counter == 0:
        return None
    else:
        return assignment(generate_pairs(miss_counter, low=1,high=n_tiles), n_tiles, type_dict, fill_type)

# make this take a distribution of types and how many we want
# distribution = [number_of_type, type]
def generate_assignments(n_tiles, n_targets, distribution):

#    w, h = resolution

    if n_tiles*n_tiles < n_targets:
        print(f"Number of targets may not exceed n_tiles*n_tiles {n_tiles**2}. Recieved {n_targets} targets.")

    d_total = 0
    for p in distribution:
        d_total += p[0]
    
    if d_total != n_targets:
        print(f"The number of targets {n_targets} doesn't correspond with the number of targets in the distribution {d_total}")
         

    
    type_dict = defaultdict(lambda: 0)

    for n_shape, shape in distribution:
        offsets = generate_pairs(n_shape, 1, n_tiles)
        assignment(offsets, n_tiles, type_dict, shape)

    return type_dict


def generate_points(resolution, step_size, assignment):

    w, h = resolution

    w_step = floor(w/(step_size+1))

    h_step = floor(h/(step_size+1))

    points = []

    for k, v in assignment.items():
        points.append((w_step*k[0],h_step*k[1], v))

    return points

if __name__ == "__main__":

    assignment = generate_assignments(10, 21, [(20, Shape.RedCross), (1, Shape.BlueCross)])

    print(generate_points((100,100), 10, assignment))

