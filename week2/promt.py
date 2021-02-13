import numpy as np
from libneuron import Neuron

def gen_random_matrix(size):
    return np.random.rand(size,size)


"""
for _ in range(1000):
    neuron_a = Neuron('A') #<- INSERT NEURON LETTER HERE 

    neuron_a(gen_random_matrix)  # Outputs scaler indicating how active teh neruon is with respect to its baseline activity
                                 # A value of -1 means that the neuron is maximally inhibited. 
                                 # A value of 0 means that the neuron is active at its baseline level. 
                                 # A value of 1 means that the neuron is maximally active.

    # INSTERT CODE HERE / change code



"""
