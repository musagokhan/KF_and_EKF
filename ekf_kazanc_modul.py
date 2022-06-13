import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random

def ekf_kazanc_fn(ekf_H , ekf_p_thm , R , t):
    # kk = (Pk*Ht) * ( S+R )^-1  & S = H * P * H^t
    S_parta = np.matmul(ekf_H, np.matmul(ekf_p_thm, ekf_H.transpose()))
    ekf_S = S_parta + R
    if  np.linalg.det(ekf_S + R) != 0 :
        ekf_K = np.matmul(np.matmul(ekf_p_thm, ekf_H.transpose()),  np.linalg.inv(ekf_S))
        return ekf_K, ekf_S
    else:
        print("!!!!!DET(S + R)!!!!!" )
        print("DET(S + R) =",np.linalg.det(ekf_S) )
        print("!!!!!DET(S + R)!!!!!" )
        exit