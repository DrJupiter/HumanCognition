import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def circle(radius, size=None):
    if size == None:
        size = radius*2

    center = size / 2
    xx, yy = np.mgrid[:size, :size]
    circle = (xx - center) ** 2 + (yy - center) ** 2

    circle[circle<=(radius/2)**2*2] = 1
    circle[circle>(radius/2)**2*2] = 0
    
    return circle

print(circle(10))