# For code path
import sys
import os
from pathlib import Path
CODE_PATH = Path(*Path(os.path.realpath(sys.argv[0])).parts[:-1])

import numpy as np
from numpy import matlib

def get_f_h() -> (str, int):
    """
    -> filename: str, filehash: int

    filename = input() if filename is an integer, then filehash = filename
    else filehash = hash(filename)
    """

    filename = input()
    try:
        filehash = int(filename)
    except ValueError:
        filehash = hash(filename)
    
    return filename, filehash


def gen_prototype(n_dots: int):
    return 2 * (np.random.rand(1, n_dots*2) - 1/2)
    
import pickle

def store_protoype(path: Path, prototype: np.array ):
    f = open(f"{path}", "wb")
    pickle.dump(prototype, f)
    f.close()


def load_prototype(path: Path) -> np.array:
    f = open(f"{path}", "rb")
    prototype = pickle.load(f)
    f.close()
    return prototype



def gen_sample(n_dots, lrn_dist, p_type, n_v_lrn_plots, n_h_lrn_plots):
    n_samples = n_v_lrn_plots*n_h_lrn_plots

    samples = np.random.rand(n_samples, n_dots*2)-1/2
    samples = np.divide(samples*lrn_dist , np.transpose(matlib.repmat(np.sqrt(np.sum(samples**2,axis=1)), n_dots*2, 1))  )
    samples += matlib.repmat(p_type, n_samples, 1)
    return samples

def gen_test_sample(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots):
    n_samples = n_v_lrn_plots*n_h_lrn_plots

    samples = np.random.rand(len(lrn_dists), n_samples, n_dots*2)-1/2
    

    d = []
    for i in range(len(lrn_dists)):
        d.append(samples[i]*lrn_dists[i])
    d = np.array(d)

    samples = np.divide(d, np.transpose(matlib.tile(np.sqrt(np.sum(samples**2,axis=2)), (n_dots*2, 1, 1)),(1,2,0)))
    samples += matlib.repmat(p_type, n_samples, 1)
    return samples

def gen_samples(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots):
    """
    returns alle the learn samples
    """ 

    learn_samples = gen_sample(n_dots, lrn_dists[1], p_type, n_v_lrn_plots, n_h_lrn_plots)
    non_lepton_samples = gen_sample(n_dots, lrn_dists[-1], p_type, n_v_lrn_plots, n_h_lrn_plots)
    test_samples = gen_test_sample(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots)
    
    
    return learn_samples, non_lepton_samples, test_samples

from random import shuffle
def gen_test_indices(n_dist_types,plot_resolution):

    outer = [x for x in range(n_dist_types)] * plot_resolution[0]*plot_resolution[1]
    shuffle(outer)
    inner = [[x for x in range(plot_resolution[0]*plot_resolution[1])] for i in range(n_dist_types)]  
    for i in inner:
        shuffle(i)

    return outer, inner 

import matplotlib.pyplot as plt
def plots(dict_learn, dict_tests, l_dists, t_dists, plot_resolution): 
    plt.rcdefaults()
    N = plot_resolution[0]*plot_resolution[1]
    plot_names = ["Tests", "Learns"]

    x_kords_t = []
    y_kords_t = []
    y_err_t = []
    for i, n_correct in enumerate(dict_tests):
        x_kords_t.append(t_dists[i])
        p=n_correct/N*100
        y_kords_t.append(p)
        y_err_t.append(np.sqrt((p*(100-p))/(N)))

    x_kords_l = []
    y_kords_l = []
    y_err_l = []
    for i, n_correct in enumerate(dict_learn):
        x_kords_l.append(l_dists[i])
        p=n_correct/N*100
        y_kords_l.append(p)
        y_err_l.append(np.sqrt((p*(100-p))/(N)))
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.bar(x_kords_t, y_kords_t, width = 0.4, yerr = y_err_t, ecolor = 'red', capsize=10, tick_label = [str(x_kords_t[0]), str(x_kords_t[1]),str(x_kords_t[2]), str(x_kords_t[3])])
    plt.title(f"{plot_names[0]}")
    plt.xlabel('distance to prototype')
    plt.ylabel('% lepton responses')
    plt.ylim((0,100))

    plt.subplot(2,1,2)
    plt.bar(x_kords_l, y_kords_l, width = 0.5, yerr = y_err_l, ecolor = 'red', capsize=10, tick_label = [str(x_kords_l[0]), str(x_kords_l[1])])
    plt.title(f"{plot_names[1]}")
    plt.xlabel('distance to prototype')
    plt.ylabel('% lepton responses')
    plt.ylim((0,100))


    
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    conf = [1.,1.5,2.,2.5]
    plot_resolution = (3,5)
    l, n, t = gen_samples(3, conf, gen_prototype(3), *plot_resolution)
    print(l.shape, n.shape,t.shape)

    

    