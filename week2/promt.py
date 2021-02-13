import numpy as np

def gen_random_matrix(dimensions):
#    return np.random.randint(0, 2, size=dimensions)
    return np.random.rand(*dimensions)


from libneuron import Neuron

# Neurons
neuron_a = Neuron('A') #<- INSERT NEURON LETTER HERE 
neuron_b = Neuron('B') #<- INSERT NEURON LETTER HERE 
neuron_c = Neuron('C') #<- INSERT NEURON LETTER HERE 

for _ in range(1000):

    print(neuron_a(gen_random_matrix((100,100))))  # Outputs scaler indicating how active the neruon is with respect to its baseline activity
                                 # A value of -1 means that the neuron is maximally inhibited. 
                                 # A value of 0 means that the neuron is active at its baseline level. 
                                 # A value of 1 means that the neuron is maximally active.

    # INSTERT CODE HERE / change code



