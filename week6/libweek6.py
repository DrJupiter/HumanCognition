import csv
import numpy as np

# For code path
import sys
import os
from pathlib import Path

CODE_PATH = Path(*Path(os.path.realpath(sys.argv[0])).parts[:-1])




with open(CODE_PATH.joinpath("patterns.csv"), newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = []
    for row in csv_reader:
        data.append(row)
        
    data = np.array(data)
        

print(data)
print(np.shape(data))
        
print(data[1][1])