import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random
import baslangic_grafik # baslangic ve grafik verileri vardir.


#################################### 
####   KALMAN TAHMIN  MODULU   #####
####################################

def nkf_x_thm_fn(A,nkf_x_duz,t): 
    ivme_durumu = baslangic_grafik.ivme_durum_fn(t)[0]
    nkf_x_thm =  np.matmul(A, nkf_x_duz) #ivmesiz
    #ivmeli
    if ivme_durumu !=0:
        ivme_vektor = baslangic_grafik.ivme_durum_fn(t)[1]
        nkf_x_thm = nkf_x_thm + ivme_vektor
    return nkf_x_thm

def nkf_p_thm_fn(A,nkf_p_duz,q_p_matris,delta_t,t):
    #part-1 :  A * Pk * A_tr        (4x4) * (4x4) * (4x4) 
    # # r * Q * r^t       (4x4) * (4x4) * (4x4)
    # ro=np.array([[0.5*t*t,0],[t,0],[0,0.5*t*t],[0,t]])
    ro = np.zeros((4, 2))
    ro[0, 0] = 0.5 * delta_t ** 2
    ro[1, 0] = delta_t
    ro[2, 1] = 0.5 * delta_t ** 2
    ro[3, 1] = delta_t 
    # q_p_mqtris FOR dan once tanimlandi
    nkf_p_thm = np.matmul(np.matmul(A, nkf_p_duz), A.transpose())
    nkf_p_thm = nkf_p_thm + np.matmul(np.matmul(ro, q_p_matris), ro.transpose())    
    #print("2.Denklem ekf_p_thm :",'\n',ekf_p_thm)
    return nkf_p_thm