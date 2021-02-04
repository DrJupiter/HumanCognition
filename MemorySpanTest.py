# Copy right Andreas Holme og Klaus Jupiter Bentzen

import random
import time
from math import sqrt

alphabet = 'bcdfghjklmnpqrstvxz'
len_alphabet = len(alphabet)

number_of_tests = int(input("HOW MANY TESTS DO YOU WANT OF EACH KIND?: "))

cases = [5,6,7,8]*number_of_tests
random.shuffle(cases)

def generate_test(n, list):
    tmp = []
    for i in range(n):
        tmp.append(alphabet[random.randint(0,len_alphabet-1)])
    list.append(tmp)

comb = []

for i in cases:
    generate_test(i, comb)

correct_dict = {'5': 0, '6': 0, '7': 0, '8': 0}

for _ in range(number_of_tests):

    print("Get ready!")
    time.sleep(1)

    for index, case in enumerate(comb):
        for c in case:

            print(c.upper(), flush=True, end='\r')
            time.sleep(1)

        usr_answer = input("Input the Sequence observed: ").strip()

        correct = 0

        for key, c in enumerate(usr_answer):
            if key < len(comb[index]):
                if c.upper() == comb[index][key].upper():
                    correct += 1
            else:
                break

        correct_dict[str(len(case))] += correct

        print(correct)

print("CORRECTNESS:")
print(correct_dict)

std_dict = {'5': 0, '6': 0, '7': 0, '8': 0} 

for key, val in correct_dict.items():
    ikey = int(key)
    p = val/(ikey*number_of_tests)
    std_dict[key] = sqrt(number_of_tests*(p)*(1-p))

print("Standard deviation:")
print(std_dict)