import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random

#################################### 
####  KALMAN DUZELTME MODULU   #####
####################################

#NKF  : Normal Kalman Filtre icin
def nkf_x_duz_fn(zk , nkf_H , nkf_x_thm , nkf_K , x_orj , t):
    # r ve teta dan x ve y elde edilecek.
    zk_x_ve_y = np.zeros((2, 1)) 

    cos = math.cos(zk[1])
    sin = math.sin(zk[1])
    zk_x_ve_y[0, 0] = zk[0] * math.cos(zk[1])
    zk_x_ve_y[1, 0] = zk[0] * math.sin(zk[1])

    nu = zk_x_ve_y -  np.matmul(nkf_H, nkf_x_thm)  # NU inovasyon
    nkf_x_duz = nkf_x_thm + np.matmul(nkf_K, nu)
    

    return nkf_x_duz


# NKF & EKF icin ortak kullanım
def nkf_p_duz_fn(nkf_p_thm , nkf_K , nkf_S , t):
    nkf_p_duz = nkf_p_thm - np.matmul(np.matmul(nkf_K, nkf_S), nkf_K.transpose())
    return nkf_p_duz