import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random

#################################### 
####  KALMAN DUZELTME MODULU   #####
####################################

#EKF  : Extended Kalman Filtre icin
def ekf_x_duz_fn(zk , ekf_x_thm , ekf_K , x_orj , t):
    zkk = np.zeros((2, 1))
    zkk[0, 0] = math.sqrt(ekf_x_thm[0, 0]**2 + ekf_x_thm[2, 0]**2)
    zkk[1, 0] = math.atan2(ekf_x_thm[0, 0], ekf_x_thm[2, 0])    
    nu = zk -  zkk  # NU inovasyon   
    ekf_x_duz = ekf_x_thm + np.matmul(ekf_K, nu)
    return ekf_x_duz


# NKF & EKF icin ortak kullanım
def ekf_p_duz_fn(ekf_p_thm , ekf_K , ekf_S , t):
    ekf_p_duz = ekf_p_thm - np.matmul(np.matmul(ekf_K, ekf_S), ekf_K.transpose())
    return ekf_p_duz