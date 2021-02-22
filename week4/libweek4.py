

from collections import defaultdict

import random

from math import floor

def generate_pairs(n_pairs, low, high):
    pairs = []
    
    for _ in range(n_pairs):
        pairs.append((random.randint(low, high), random.randint(low, high)))
    
    return pairs


def assignment(offsets, n_tiles, type_dict, fill_type):
    print(offsets)
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
def generate_assignments(n_tiles, n_targets):

#    w, h = resolution

    if n_tiles*n_tiles < n_targets:
        print(f"Number of targets may not exceed n_tiles*n_tiles {n_tiles**2}. Recieved {n_targets} targets.")

    offsets = generate_pairs(n_targets, 1, n_tiles)
    
    type_dict = defaultdict(lambda: 0)

    assignment(offsets, n_tiles, type_dict, 1)

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

    assignment = generate_assignments(10, 20)
    
    print(generate_points((100,100), 10, assignment))

