import numpy as np

from libneuron import Neuron

# Neurons
neuron_a = Neuron('A')  # \
neuron_b = Neuron('B')  #  | The character/letter in Neuron(character) indicates which type of neuron is instantiated.
neuron_c = Neuron('C')  # /

for _ in range(10):

    print(neuron_a(np.ones((100, 100))))  # \
    print(neuron_b(np.ones((100, 100))))  #  | Outputs scalar indicating how active the neuron is with respect to its baseline activity
    print(neuron_c(np.ones((100, 100))))  # /
                                          #    A value of -1 means that the neuron is maximally inhibited.
                                          #    A value of 0 means that the neuron is active at its baseline level.
                                          #    A value of 1 means that the neuron is maximally active.

    # INSTERT CODE HERE / CHANGE CODE
