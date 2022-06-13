import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random



# NKF  :  Kalman Filtre icin H matrisi uretimi
def nkf_h_fn():
    
    nkf_H = np.zeros((2, 4))
    nkf_H[0, 0] = 1
    nkf_H[1, 2] = 1

    return nkf_H