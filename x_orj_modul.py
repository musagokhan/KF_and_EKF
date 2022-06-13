import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random
import baslangic_grafik # baslangic ve grafik verileri vardir.

#################################### 
###### x_orj :  ground truth   #####
####################################

def x_orj_fn(A,x_orj,t):
    ivme_durumu = baslangic_grafik.ivme_durum_fn(t)[0]
    x_orj = np.matmul(A, x_orj) #ivmesiz
    #ivmeli
    if ivme_durumu !=0:
        ivme_vektor = baslangic_grafik.ivme_durum_fn(t)[1]
        x_orj = x_orj + ivme_vektor

    return x_orj