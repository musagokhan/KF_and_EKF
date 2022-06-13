import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random

import baslangic_grafik


def prf_fn(x_orj,nkf_x_thm,ekf_x_thm,t):
    nkf_perf_array = []
    ekf_perf_array = []

    pyd = math.hypot(x_orj[0, 0] - 0,x_orj[2, 0] - 0)

    nkf_pay = math.hypot( x_orj[0, 0] - nkf_x_thm[0, 0] , x_orj[2, 0] - nkf_x_thm[2, 0] ) 
    nkf_perf_array.append(100*(nkf_pay/pyd))

    ekf_pay = math.hypot( x_orj[0, 0] - ekf_x_thm[0, 0] , x_orj[2, 0] - ekf_x_thm[2, 0] )
    ekf_perf_array.append(100*(ekf_pay/pyd))


    adim_sayisi = baslangic_grafik.orneklem_adedi_fn()

    if t == adim_sayisi-1:
        nkf_perf = sum(nkf_perf_array)/adim_sayisi
        ekf_perf = sum(ekf_perf_array)/adim_sayisi
        print( "% nkf_hata :", nkf_perf)
        print( "% ekf_hata :", ekf_perf)

    return 