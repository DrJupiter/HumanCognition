from random import shuffle

import csv
import numpy as np
import matplotlib.pyplot as plt

# For code path
import sys
import os
from pathlib import Path
CODE_PATH = Path(*Path(os.path.realpath(sys.argv[0])).parts[:-1])



def hop_field_net(n_patterns: int = 5,
 test_pattern_noise_lvl: float = 0., wmtrx_noise_lvl: float = 0.):

    if n_patterns > 15 or n_patterns < 1:
        print(f"The number of patterns must be between 1 and 15, received {n_patterns}")

    if test_pattern_noise_lvl < 0 or test_pattern_noise_lvl > 1:
        print(f"The TestPatternNoiseLvl must be between 0 and 1, received {test_pattern_noise_lvl}")

    if wmtrx_noise_lvl < 0 or wmtrx_noise_lvl > 1:
        print(f"The WmtrxNoiseLvl must be between 0 and 1, received {wmtrx_noise_lvl}")


    test_pattern_idx = 1

    train_patterns = load_patterns_rand(n_patterns)

    n_neurons = train_patterns.shape[1]

    w_mtrx = weight_matrix(n_neurons, n_patterns, train_patterns, wmtrx_noise_lvl)

    # a boolean matrix
    flip_mtrx = np.where(np.random.rand(n_neurons) < test_pattern_noise_lvl, True, False)


def weight_matrix(n_neurons, n_patterns, train_patterns, wmtrx_noise_lvl):
    w_mtrx = np.zeros(n_neurons)

    for i in range(0,n_patterns):
        w_mtrx = w_mtrx + np.transpose(train_patterns[i,:]) * train_patterns[i,:] - np.identity(n_neurons)

    w_mtrx = w_mtrx/n_patterns
    w_mtrx = w_mtrx + (np.random.rand(n_neurons)-1/2) * wmtrx_noise_lvl

    return w_mtrx

def load_patterns():

    with open(CODE_PATH.joinpath("patterns.csv"), newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = []
        for row in csv_reader:
            data.append(list(map(float, row)))

        data = np.array(data)
    


    return data

def load_patterns_rand(n_patterns: int):

    patterns = load_patterns() 

    _pat_range = [i for i in range(0,15)]
    shuffle(_pat_range)
    train_pattern_idx = _pat_range[:n_patterns]

    train_patterns = patterns[train_pattern_idx,:]

    return train_patterns

def show_patterns(patterns: list):

    fig = plt.figure(figsize= (10,10))
    plt.title('XD')
    plt.imshow(patterns[0].reshape((10,10)), 'gray')

    plt.show()


if __name__ == "__main__":
    hop_field_net()