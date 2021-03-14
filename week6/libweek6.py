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

    patterns = load_patterns(n_patterns) 

    test_pattern_idx = 1
    train_pattern_idx = shuffle([i for i in range(1,n_patterns+1)])

    # each pattern object contains 100 px



def load_patterns(n_patterns: int):

    with open(CODE_PATH.joinpath("patterns.csv"), newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = []
        for row in csv_reader:
            data.append(list(map(float, row)))

        data = np.array(data)
    
    print(np.shape(data))


    return data

def show_patterns(patterns: list):

    fig = plt.figure(figsize= (10,10))
    plt.title('XD')
    plt.imshow(patterns[0].reshape((10,10)), 'gray')

    plt.show()
