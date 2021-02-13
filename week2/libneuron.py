import numpy as np



class Neuron():

    def __init__(type: str):
        matrix = match_type(str.strip().lower())

    def match_type(str):
        if str == 'a':
            return 
        elif ...

    def __call__(self,input_matrix):
        if input_matrix.shape != self.matrix.shape:
            print(f"ERROR: WRONG INPUT SHAPE. RECIEVED a matrix with dimensions {input_matrix.shape} expected a matrix with dimensions {self.matrix.shape}")
        else:
            # Maybe this has to be np.dot(input_matrix, self.matrix)
            return input_matrix * self.matrix