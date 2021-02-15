import numpy as np

from libneuron import Neuron

# Neurons
neuron_a = Neuron('A') #<- INSERT NEURON LETTER HERE 
neuron_b = Neuron('B') #<- INSERT NEURON LETTER HERE 
neuron_c = Neuron('C') #<- INSERT NEURON LETTER HERE 

for _ in range(10):

    print(neuron_a(np.zeros((100,100)))) # <- INPUT MATRIX HERE
                                 # Outputs scaler indicating how active the neruon is with respect to its baseline activity
                                 # A value of -1 means that the neuron is maximally inhibited. 
                                 # A value of 0 means that the neuron is active at its baseline level. 
                                 # A value of 1 means that the neuron is maximally active.

    # INSTERT CODE HERE / change code



