import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random



# EKF  : Extended Kalman Filtre icin H matrisi uretimi
def ekf_h_fn(x_orj):
    
    x = x_orj [0,0]
    y = x_orj [2,0]
    r = math.sqrt(x*x + y*y)
    r_kare = x*x + y*y

    h1_x = x/r
    h1_vx = 0
    h1_y = y/r
    h1_vy = 0
    
    h2_x = y/r  
    h2_vx = 0
    h2_y = -x/r
    h2_vy = 0

    ekf_H = np.zeros((2, 4))
    ekf_H[0,0] = h1_x
    ekf_H[0,1] = h1_vx
    ekf_H[0,2] = h1_y
    ekf_H[0,3] = h1_vy

    ekf_H[1,0] = h2_x
    ekf_H[1,1] = h2_vx
    ekf_H[1,2] = h2_y
    ekf_H[1,3] = h2_vy

    return ekf_H