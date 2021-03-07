# Copyright Andreas Holme og Klaus Jupiter Bentzen

import random
import time
from math import sqrt
from collections import defaultdict

alphabet = 'bcdfghjklmnpqrstvxz'
len_alphabet = len(alphabet)



def generate_cases(config, number_of_tests):
    return config*number_of_tests

#cases = [5,6,7,8]*number_of_tests
#random.shuffle(cases)

def generate_test(n, list):
    tmp = []
    for i in range(n):
        tmp.append(alphabet[random.randint(0,len_alphabet-1)])
    list.append(tmp)


def generate_comb(cases):
    comb = []

    for i in cases:
        generate_test(i, comb)
    return comb

#correct_dict = {'5': 0, '6': 0, '7': 0, '8': 0}

def get_index(array, val):
    for key, item in enumerate(array):
        if item == val:
            return key
    return None

# Checks the number of correct answers regardless of their position
def check_correctness(position_dict, sequence, usr_answer):
    print(sequence)
    usr_answer = [c for c in usr_answer]
    print(usr_answer)
    for pos, c in enumerate(sequence):
        answer_pos = get_index(usr_answer, c)
        if answer_pos is not None:
            print(usr_answer)
            position_dict[pos] += 1
            print(answer_pos)
            usr_answer.pop(answer_pos)
        #else:
        #    # We do this inorder to avoid uninitialized entries
        #    position_dict[pos]
    
def calculate_means(position_dict, number_of_tests):
    mean_dict = defaultdict(lambda: 0)

    for key, val in position_dict.items():
        mean = val/(number_of_tests)
        mean_dict[key] = mean 
    return mean_dict

import matplotlib.pyplot as plt

def bar_plot(mean_dict): 
    plt.rcdefaults()
    positions = []
    means = []
    for key, val in mean_dict.items():
        print(type(key))
        positions.append(key+1)
        means.append(val)
    print(positions)

    plt.title('Serial Position Task')
    plt.xlabel('Position in Letter Sequence')
    plt.ylabel('Average Accuracy')
    plt.bar(positions, means, color='red')
    plt.xticks([i for i in range(1,11)])
    plt.show()

if __name__ == "__main__":
    number_of_tests = int(input("HOW MANY TESTS DO YOU WANT OF EACH KIND?: "))

    cases = generate_cases([10], number_of_tests)
    print(cases)

    comb = generate_comb(cases)
    print(comb)

    position_dict = defaultdict(lambda: 0)

    print("Get ready!")
    time.sleep(1)

    for index, case in enumerate(comb):
        for c in case:

            print(c.upper(), flush=True, end='\r')
            time.sleep(0)

        usr_answer = input("Input the Sequence observed: ").strip()

        check_correctness(position_dict, case, usr_answer)


    print("CORRECTNESS:")
    print(position_dict)

    print("Means")
    print(calculate_means(position_dict, number_of_tests))
