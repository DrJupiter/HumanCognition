from random import shuffle

import csv
from typing import Pattern
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
    _pat_range = [i for i in range(0,15)]
    shuffle(_pat_range)
    train_pattern_idx = _pat_range[:n_patterns]

    patterns = load_patterns(n_patterns) 

    train_patterns = patterns[train_pattern_idx,:]

    print(train_patterns)

    # each pattern object contains 100 px



def load_patterns(n_patterns: int):

    with open(CODE_PATH.joinpath("patterns.csv"), newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = []
        for row in csv_reader:
            data.append(list(map(float, row)))
        data = np.array(data)
    
    #print(np.shape(data))

    return data

def show_patterns(patterns: list):

    fig, axs = plt.subplots(1,len(patterns))
    fig.subplots_adjust(hspace = .5, wspace=0.2)

    axs = axs.ravel()

    for i in range(len(patterns)):
        axs[i].imshow(np.rot90(patterns[i].reshape((10,10)),axes=(1,0)), 'gray')
        axs[i].get_xaxis().set_visible(False)
        axs[i].get_yaxis().set_visible(False)

    plt.show()

"""
patts = load_patterns(15)
r_patts = []
for i in range(len(patts)):
    r_patts.append(patts[i])

show_patterns(r_patts)
"""


hop_field_net()
