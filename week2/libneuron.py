import numpy as np
"""
import sys
np.set_printoptions(threshold=sys.maxsize)
"""

class Neuron():

    def __init__(self, type: str):
        self.type = type.strip().lower()
        self.matrix = self.match_type(self.type)
        self.normalized_matrix = self.normalize()

    def match_type(self, string):
        if string == 'a':
            return np.ones((100, 100)) 
        elif string == 'b':
            return np.zeros((100, 100))
        elif string == 'c':
            return np.full((100,100), fill_value = -1)
        else:
            print(f"ERROR: Expected neuron type a, b, or c. recieved unknown neuron type {string}")
            # return top-secret

    def __call__(self,input_matrix):
        if input_matrix.shape != self.matrix.shape:
            print(f"ERROR: WRONG INPUT SHAPE. RECIEVED a matrix with dimensions {input_matrix.shape} expected a matrix with dimensions {self.matrix.shape}")
        else:
            # Maybe this has to be np.dot(input_matrix, self.matrix)

#            res = input_matrix - self.matrix
#            div = res/self.matrix
#            return np.sum(div)
            # sum(div) -> [-1;1]
#            return np.dot(input_matrix.flatten(), self.normalized_matrix.flatten())
            return np.sum((np.transpose(input_matrix)* self.normalized_matrix))
            #return (np.dot(np.transpose(input_matrix), self.normalized_matrix))
            

    def normalize(self):

        one_position = np.where(self.matrix == 1)
        zero_position = np.where(self.matrix == 0)


        n_ones = np.sum(self.matrix == 1)
        n_zeroes = np.sum(self.matrix == 0 )

        normalized = np.copy(self.matrix)

        # Check for division by 0
        if n_zeroes != 0:
            normalized[zero_position] = -1/n_zeroes 
    
        if n_ones != 0:
            normalized[one_position] = 1/n_ones

        return normalized


    def __repr__(self) -> str:
        return str(self.matrix)

neuron_a = Neuron('C')


print(neuron_a(np.full(shape=(100,100), fill_value=-1)))