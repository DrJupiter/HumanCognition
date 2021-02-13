import numpy as np
import sys
import pickle
np.set_printoptions(threshold=sys.maxsize)

def line(size):
    M = np.zeros((size, size))

    for x in range(1,size):
        for y in range(1,size):
            if x == y:
                M[x,y-1] = 1
    
    for x in range(1,size):
        for y in range(1,size):
            if x == y:
                M[x-1,y] = 1

    return M

#print(line(24))

NeruonC = open(f"NeruonC", "wb")
pickle.dump(line(100),NeruonC)
NeruonC.close()

"""
NeruonC = open(f"NeruonC", "wb")
print(NeruonC)
NeruonC.close()
"""