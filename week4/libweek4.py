import matplotlib.pyplot as plt
from collections import defaultdict 
from enum import Enum, unique
import numpy as np


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
    print(default_dict[string_state])
    default_dict[string_state].append(end_time - start_time)
    #default_dict[string_state].append([1])


def plots(time_dict,config):
    #print("################## TEST ############################") 
    plt.rcdefaults()

    #print(time_dict)

    disjunk_present = []

    disjunk_present.append(np.array(time_dict['(<TestType.Disjunktion: (0,)>, 6, True)']))
    disjunk_present.append(np.array(time_dict['(<TestType.Disjunktion: (0,)>, 20, True)']))
    disjunk_present.append(np.array(time_dict['(<TestType.Disjunktion: (0,)>, 60, True)']))
    
    disjunk_absent = []
    disjunk_absent.append(np.array(time_dict['(<TestType.Disjunktion: (0,)>, 6, False)']))
    disjunk_absent.append(np.array(time_dict['(<TestType.Disjunktion: (0,)>, 20, False)']))
    disjunk_absent.append(np.array(time_dict['(<TestType.Disjunktion: (0,)>, 60, False)']))

    conjunk_present = []
    conjunk_present.append(np.array(time_dict['(<TestType.Conjunktion: (1,)>, 6, True)']))
    conjunk_present.append(np.array(time_dict['(<TestType.Conjunktion: (1,)>, 20, True)']))
    conjunk_present.append(np.array(time_dict['(<TestType.Conjunktion: (1,)>, 60, True)']))
    
    conjunk_absent = []
    conjunk_absent.append(np.array(time_dict['(<TestType.Conjunktion: (1,)>, 6, False)']))
    conjunk_absent.append(np.array(time_dict['(<TestType.Conjunktion: (1,)>, 20, False)']))
    conjunk_absent.append(np.array(time_dict['(<TestType.Conjunktion: (1,)>, 60, False)']))
    
    plot_times = [disjunk_present, disjunk_absent, conjunk_present, conjunk_absent]
    plot_names = ["disjunk_present", "disjunk_absent", "conjunk_present", "conjunk_absent"]

    x_kords = []
    y_kords = []
    y_err = []
    for j in range(len((plot_times))):
        x_temp = []
        y_temp = []
        err_temp = []
        for i in range(len(config)):
            x_temp.append(config[i])
            y_temp.append(np.mean(plot_times[j][i]))
            err_temp.append(np.std(plot_times[j][i]))
        x_kords.append(x_temp)
        y_kords.append(y_temp)
        y_err.append(err_temp)

    #print(x_kords)
    #print(y_kords)
    #print(y_err)

    plt.figure()
    for i in range(len(plot_times)):
        plt.subplot(2,2,i+1)
        plt.errorbar(x_kords[i], y_kords[i], y_err[i], ecolor = 'red')
        plt.title(f"{plot_names[i]}")
        plt.xlabel('number of distractors')
        plt.ylabel('Time Spent in a State in Seconds')
    
    plt.tight_layout()
    plt.show()








if __name__ == "__main__":


    step_size = 10
    disjunktion_test = generate_tests(1, [6, 20, 60], TestType.Disjunktion, step_size)
    conjunkiton_test = generate_tests(1, [6, 20, 60], TestType.Conjunktion, step_size)



