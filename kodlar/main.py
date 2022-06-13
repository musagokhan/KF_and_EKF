import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random

import baslangic_grafik # baslangic ve grafik verileri vardir.
import x_orj_modul  # Groundtruth üretimi
import ekf_h_modul  # EKF H matrisini olusturur
import nkf_h_modul  # NKF H matrisini olusturur
import z_olcum_modul  # olcum uretir
import kalman


delta_t = 1
# baslangic verileri tanimlanir.
baslangic_verileri = baslangic_grafik.ilk_veriler(delta_t)
A = baslangic_verileri[0]
x_orj = baslangic_verileri[1]
ekf_x_duz = baslangic_verileri[2]
ekf_p_duz = baslangic_verileri[3]
nkf_x_duz = ekf_x_duz # baslangicta EKF  = NKF icin
nkf_p_duz = ekf_p_duz # baslangicta EKF  = NKF icin
q_p_matris = baslangic_verileri[4]
R = baslangic_verileri[5]
orneklem_adedi = baslangic_grafik.orneklem_adedi_fn()


for t in range(orneklem_adedi): 
    ###### x_orj :  ground truth   #####
    x_orj = x_orj_modul.x_orj_fn(A,x_orj,t)
    
    ###### H matrisi tanimalamasi  #####
    nkf_H = nkf_h_modul.nkf_h_fn() #NKF : Normal Kalman Filtre
    ekf_H = ekf_h_modul.ekf_h_fn(x_orj)  # EKF  : Extended Kalman Filtre

    ###  olcum modeli  NOT : OLCUM NKF & EKF icin aynidir. 
    zk = z_olcum_modul.zk_fn(x_orj,t) # NKF & EKF icin ortak kullanım
    
    # Kalman Blok
    kalman_verileri = kalman.kalman_fn(A , ekf_x_duz , ekf_p_duz , q_p_matris, delta_t, nkf_x_duz, nkf_p_duz, ekf_H,  R , nkf_H ,  zk, x_orj, t)
    ekf_x_duz, ekf_p_duz, nkf_x_duz, nkf_p_duz = kalman_verileri[0] , kalman_verileri[1] , kalman_verileri[2] , kalman_verileri[3]


plt.show()