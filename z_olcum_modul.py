import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random
import numpy

import baslangic_grafik 


# NOT : OLCUM NKF & EKF icin aynidir. 
#EKF & NKF icin aynidir.  OLCUM R ve teta'dir.
def zk_fn(x_orj,t):   

    if t==0: # sadece ilk seferde girip olusturulan veriler ceklir. yoksa Gauss gürültüsü her seferinde değişir.
        orneklem_adedi = baslangic_grafik.orneklem_adedi_fn()
        ol_mu, ol_sigma_r, ol_sigma_teta = 0, 5, 1  # on tanimlamalar
        ol_sigma_teta = math.radians(ol_sigma_teta) # on tanimlama
        global ol_normal_dagilim_r
        global ol_normal_dagilim_teta
        #Gauss Dagilimi
        ol_normal_dagilim_r = np.random.normal(ol_mu, ol_sigma_r, orneklem_adedi)
        ol_normal_dagilim_teta = np.random.normal(ol_mu, ol_sigma_teta, orneklem_adedi)
        #Uniform DDagilim
        #ol_normal_dagilim_r = numpy.random.uniform(0, ol_sigma_r, orneklem_adedi) 
        #ol_normal_dagilim_teta = numpy.random.uniform(0, ol_sigma_teta, orneklem_adedi)    


    q_z = np.eye(2,1) # NKF & EKF icin ortak kullanım
    q_z[0, 0] = ol_normal_dagilim_r[t] # NKF & EKF icin ortak kullanım
    q_z[1, 0] = ol_normal_dagilim_teta[t] # NKF & EKF icin ortak kullanım

    # esas bolum
    zk = np.zeros((2, 1))
    zk[0,0] = math.sqrt(x_orj [0,0]**2 + x_orj [2,0]**2) + q_z[0,0]
    zk[1,0] = math.atan2 (x_orj [0,0] , x_orj [2,0]) + q_z[1,0]
    #zk = zk + ekf_q_z
    return zk
