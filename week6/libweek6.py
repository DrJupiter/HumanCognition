# OBS:
# To change input, go to the bottom of the file

from random import shuffle
from copy import deepcopy

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
    """
    hop_field_net takes 3 parameters.

    The first n_patterns determines how many patterns are loaded as well as how many iterations are done during training. [1, 15]

    The second test_pattern_noise_lvl determines the frequency at which pixels are flipped at in the initial selected image [0,1]

    The third wmtrx_noise_lvl determines how much to scale the noise added to the weight matrix by. [0,1]

    The hops field network is then run, and the outputs of it are displayed.
    """
    if n_patterns > 15 or n_patterns < 1:
        print(f"ERROR: The number of patterns must be between 1 and 15, received {n_patterns}")
        return None

    if test_pattern_noise_lvl < 0 or test_pattern_noise_lvl > 1:
        print(f"ERROR: The TestPatternNoiseLvl must be between 0 and 1, received {test_pattern_noise_lvl}")
        return None

    if wmtrx_noise_lvl < 0 or wmtrx_noise_lvl > 1:
        print(f"ERROR: The WmtrxNoiseLvl must be between 0 and 1, received {wmtrx_noise_lvl}")
        return None



    train_patterns = load_patterns_rand(n_patterns, "patterns.csv")

    n_neurons = train_patterns.shape[1]

    w_mtrx = weight_matrix(n_neurons, n_patterns, train_patterns, wmtrx_noise_lvl)

    flip_mtrx = np.where(np.random.rand(n_neurons) < test_pattern_noise_lvl)

    test_pattern_idx = 0
    test_pattern = deepcopy(train_patterns[test_pattern_idx, :])
    test_pattern[flip_mtrx] = np.random.randint(0,1,size=test_pattern[flip_mtrx].shape)*2-1

    iterations = np.zeros(shape=(n_patterns, test_pattern.shape[0]))

    iterations[0] = test_pattern


    for i in range(len(iterations)-1):
        iterations[i+1] = np.sign(np.dot(w_mtrx , iterations[i, :]))

    show_patterns(train_patterns, [train_patterns[test_pattern_idx]], iterations)



def weight_matrix(n_neurons, n_patterns, train_patterns, wmtrx_noise_lvl):
    """
    Generates Weight_matrix based on [(n_neurons, n_patterns, train_patterns, wmtrx_noise_lvl]
    """
    w_mtrx = np.zeros(n_neurons)

    for i in range(0,n_patterns):
        h = np.transpose(train_patterns[i,:].reshape(1,100)) * train_patterns[i,:].reshape(1,100)
        w_mtrx = w_mtrx + h - np.identity(n_neurons)
#        print((np.transpose(train_patterns[i,:].reshape(1,100)) * train_patterns[i,:].reshape(1,100)).shape)
#        print(train_patterns[i,:].reshape(1,100))
    
    w_mtrx = w_mtrx/n_patterns
    w_mtrx = w_mtrx + (np.random.rand(n_neurons)-1/2) * wmtrx_noise_lvl

    return w_mtrx

def load_patterns(path):
    """
    Loads all patterns from csv file which is in the same directory as the rest of the code.
    """
    with open(CODE_PATH.joinpath(path), newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = []
        for row in csv_reader:
            data.append(list(map(float, row)))
        data = np.array(data)
    

    return data

def load_patterns_rand(n_patterns: int, path):
    """
    Choses "n_patterns" random patterns from the 15 patterns
    """
    patterns = load_patterns(path) 

    _pat_range = [i for i in range(0,15)]
    shuffle(_pat_range)
    train_pattern_idx = _pat_range[:n_patterns]

    train_patterns = patterns[train_pattern_idx,:]

    return train_patterns

def show_patterns(train_patterns: list, selected_pattern: list, iter_patterns: list):
    """
    Plots the patterns (Train: top, selected: middle, Iter: bot)
    """

    fig, axs = plt.subplots(3,len(iter_patterns))
    fig.subplots_adjust(hspace = .5, wspace=0.2)

    for i in range(len(train_patterns)):
        axs[0, i].imshow(np.rot90(train_patterns[i].reshape((10,10)),axes=(1,0)), 'gray')
        axs[0, i].get_xaxis().set_visible(False)
        axs[0, i].get_yaxis().set_visible(False)
        axs[0,i].set_title(f"Pattern {i+1}")

    for i in range(len(selected_pattern)):
        axs[1, i].imshow(np.rot90(selected_pattern[i].reshape((10,10)),axes=(1,0)), 'gray')
        axs[1, i].get_xaxis().set_visible(False)
        axs[1, i].get_yaxis().set_visible(False)
        axs[1,i].set_title(f"Selected Pattern {i+1}")

    for i in range(len(selected_pattern), len(train_patterns)):
        axs[1, i].axis('off')

    for i in range(len(iter_patterns)):
        axs[2, i].imshow(np.rot90(iter_patterns[i].reshape((10,10)),axes=(1,0)), 'gray')
        axs[2, i].get_xaxis().set_visible(False)
        axs[2, i].get_yaxis().set_visible(False)
        axs[2,i].set_title(f"Iteration {i+1}")

    plt.show()



if __name__ == "__main__":

    # Change here:
    hop_field_net(5, 0, 0)
    
    # Hover function to view inputs or read the function documentation at the top of the file under the function declaration.
