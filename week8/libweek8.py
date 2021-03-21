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


def generate_prototype(n_dots: int):
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

def main(n_dots: int, plots: (int, int)):

    filename, filehash = get_f_h()

    p_type = generate_prototype(n_dots)
    
    return None

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

def gen_learn_samples(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots):
    """
    returns alle the learn samples
    """ 
    learn_samples = gen_sample(n_dots, lrn_dists[1], p_type, n_v_lrn_plots, n_h_lrn_plots)
    non_lepton_samples = gen_sample(n_dots, lrn_dists[-1], p_type, n_v_lrn_plots, n_h_lrn_plots)
    test_samples = gen_test_sample(n_dots, lrn_dists, p_type, n_v_lrn_plots, n_h_lrn_plots)
    
    print(learn_samples.shape,non_lepton_samples.shape,test_samples.shape)
    
    Vs_code = "fish"
    return Vs_code

print(gen_learn_samples(3, [1, 1.5, 2, 2.5], generate_prototype(3), 3, 5))
