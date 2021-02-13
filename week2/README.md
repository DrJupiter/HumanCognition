# Implement

 - [1] A neuron class
 - - [1.1] The neuron class should have three neuron options - A, B, C. The options generate a neuron with a different pattern each.
 - > We find the patterns detailed in the matlab files
 - [2] An instructional file


# Implementation

## [1] Neuron Class

- Be initialized as one of the three neurons
- Callable where: `neuron(input) -> input*inner_matrix` 

```python
class Neuron():

    def __init__(type: str):
        matrix = match_type(str.strip().lower())

    def match_type(str):
        if str == 'a':
            return matrix_a
        elif ...

    def __call__(self,input_matrix):
        if input_matrix.shape != self.matrix.shape:
            print(f"ERROR: WRONG INPUT SHAPE. RECIEVED a matrix with dimensions {input_matrix.shape} expected a matrix with dimensions {self.matrix.shape}")
        else:
            # Maybe this has to be np.dot(input_matrix, self.matrix)
            return input_matrix * self.matrix
```

## [2] Instructional file

- describe the api
- put in some boiler plate code
- let the user figure out how to determine the neurons structure as per instruction

# Extra Tid: 

- billede ind selv, så skal vi printe, hvordan det ser ud

- Giv os et input, som vi så tager som vores shape af billede for at teste om perception er anderledes for fx højerer resolution.

- can we encrypt the files? - spend no more than 30 min
- > Perhaps load matrixes with pickle, since they would be semi obscured as they would be in a binary format.

- find ud af hvordan vi konvertere sort hvid svg’er til matricer

- convert neuron to a black and white image.

## The meme branch???

- print() -> Don’t cheat / matrix hvor det ligner Xd lol pepe, der griner troll 

### How would we solve it

sum of scalar times input matricies.