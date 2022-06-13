import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random

def nkf_kazanc_fn(nkf_H , nkf_p_thm , R , t):
    # kk = (Pk*Ht) * ( S+R )^-1  & S = H * P * H^t
    S_parta = np.matmul(nkf_H, np.matmul(nkf_p_thm, nkf_H.transpose()))
    nkf_S = S_parta + R
    if  np.linalg.det(nkf_S + R) != 0 :
        nkf_K = np.matmul(np.matmul(nkf_p_thm, nkf_H.transpose()),  np.linalg.inv(nkf_S))
        return nkf_K, nkf_S
    else:
        print("!!!!!DET(S + R)!!!!!" )
        print("DET(S + R) =",np.linalg.det(nkf_S) )
        print("!!!!!DET(S + R)!!!!!" )
        exit