import csv
import numpy as np
import matplotlib.pyplot as plt

# For code path
import sys
import os
from pathlib import Path

CODE_PATH = Path(*Path(os.path.realpath(sys.argv[0])).parts[:-1])




with open(CODE_PATH.joinpath("patterns.csv"), newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = []
    for row in csv_reader:
        data.append(list(map(float, row)))

    data = np.array(data)
        
print(np.shape(data))


data[data == -1.0] = 0

#print(data)

fig = plt.figure(figsize= (10,10))
plt.title('XD')
plt.imshow(data[0].reshape((10,10)), 'gray')

print(data[0].reshape((10,10)))

plt.show()