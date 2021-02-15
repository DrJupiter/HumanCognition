import numpy as np


# For code path
import sys
import os
from pathlib import Path

from numpy.core.fromnumeric import shape

# This is used to read files in the module properly when the Main.py script is run from an external location.
CODE_PATH = Path(*Path(os.path.realpath(sys.argv[0])).parts[:-1])

import pickle
np.set_printoptions(threshold=sys.maxsize)

class Neuron():
    """
    Neuron(INPUT_MATRIX) -> [-1;1], which depicts how close the INPUT_MATRIX was to the Neuron.
    """
    def __init__(self, type: str):
        self.type = type.strip().lower()
        self.matrix = self.match_type(self.type)
        self.normalized_matrix = self.normalize()

    def match_type(self, string):
        if string == 'a':
            with open(CODE_PATH.joinpath("NeuronA"), 'rb') as f:
                a = pickle.load(f)
                f.close()
            return a

        elif string == 'b':
            with open(CODE_PATH.joinpath("NeuronB"), 'rb') as f:
                b = pickle.load(f)
                f.close()
            return b

        elif string == 'c':
            with open(CODE_PATH.joinpath("NeuronC"), 'rb') as f:
                c = pickle.load(f)
                f.close()
            return c
        else:
            print(f"ERROR: Expected neuron type a, b, or c. recieved unknown neuron type {string}")
            return np.random.randint(0,2, size=(100,100))

    def __call__(self,input_matrix):
        if input_matrix.shape != self.matrix.shape:
            print(f"ERROR: WRONG INPUT SHAPE. RECIEVED a matrix with dimensions {input_matrix.shape} expected a matrix with dimensions {self.matrix.shape}")
        else:
            return np.sum(input_matrix*self.normalized_matrix)
            

    def normalize(self):

        one_position = np.where(self.matrix == 1)
        zero_position = np.where(self.matrix == 0)


        n_ones = np.sum(self.matrix == 1)
        n_zeroes = np.sum(self.matrix == 0)

        normalized = np.copy(self.matrix).astype('float64')

#        print(normalized[one_position])

        # Check for division by 0
        if n_zeroes != 0:
            normalized[zero_position] = -1/n_zeroes 
    
        if n_ones != 0:
            normalized[one_position] = 1/n_ones
        
#        print(np.sum(normalized))
#        print(np.sum(normalized[zero_position]*(0)) + np.sum(normalized[one_position] * 1))

        return normalized



def test_neuron():

    a, b, c = Neuron('A'), Neuron('B'), Neuron('C')

    print(a.matrix.shape,b.matrix.shape,c.matrix.shape)
    print(a(a.matrix), b(b.matrix), c(c.matrix))

    #d = Neuron('Y')
    #print(d(d.matrix))

#b = Neuron('B')

#print(b(b.matrix))

#test_neuron()


#print(neuron_a(np.full(shape=(100,100), fill_value=-1)))
