

from collections import defaultdict 
from enum import Enum, unique


import random

from math import floor
from typing import List

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

@unique
class TestType(Enum):
    Disjunktion = 0,
    Conjunktion = 1,


def generate_tests(n_tests, config, test_type, step_size=10):
    cases = config*n_tests
    random.shuffle(cases)


    # Make the elements in this also have a boolean variable
    # which displays wether or not a target is there
    tests = []

    if test_type == TestType.Disjunktion:

        for case in cases:

            if random.random() >= 0.5:
                if random.random() >= 0.5:
                    target = (1, Shape.BlueCross)
                else:
                    target = (1, Shape.RedCircle)
                
                tests.append((generate_assignments(step_size, case+1, [(case, Shape.RedCross), target]), True))
            else:
                tests.append((generate_assignments(step_size, case, [(case, Shape.RedCross)]), False))

        
    
    elif test_type == TestType.Conjunktion:

        for case in cases:
            if random.random() >= 0.5:
                target = (1, Shape.BlueCross)

                tests.append((generate_assignments(step_size, case+1, [(case//2, Shape.RedCross), (case//2, Shape.BlueCircle), target]),True))
            else:
                tests.append((generate_assignments(step_size, case, [(case//2, Shape.RedCross), (case//2, Shape.BlueCircle)]),False))
    
    return tests

def update_time_dict(default_dict, state, start_time, end_time):
    string_state = f'{state}'
    default_dict[string_state] += end_time - start_time

if __name__ == "__main__":


    step_size = 10
    disjunktion_test = generate_tests(1, [6, 20, 60], TestType.Disjunktion, step_size)
    conjunkiton_test = generate_tests(1, [6, 20, 60], TestType.Conjunktion, step_size)



