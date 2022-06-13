import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random


import ekf_thm_modul  # EKF tahmin yapar
import nkf_thm_modul  # NKF tahmin yapar
import ekf_kazanc_modul  # EKF kazanc hesaplar
import nkf_kazanc_modul  # NKF kazanc hesaplar
import ekf_duz_modul  # EKF icin duzeltme (updt) yapar
import nkf_duz_modul  # NKF icin duzeltme (updt) yapar
import grafik_cizim #grafik icin
import performans

def kalman_fn(A , ekf_x_duz , ekf_p_duz , q_p_matris, delta_t, nkf_x_duz, nkf_p_duz, ekf_H,  R , nkf_H ,  zk, x_orj, t):


    ###### KALMAN #####
    #---TAHMIN BLOK---#
    #thmn blok EKF icin
    ekf_x_thm = ekf_thm_modul.ekf_x_thm_fn(A,ekf_x_duz,t)   # NKF & EKF icin ortak kullanım
    ekf_p_thm = ekf_thm_modul.ekf_p_thm_fn(A,ekf_p_duz,q_p_matris,delta_t,t)  # NKF & EKF icin ortak kullanım
    #thmn blok NKF icin 
    nkf_x_thm = nkf_thm_modul.nkf_x_thm_fn(A,nkf_x_duz,t)   # NKF icin ortak kullanım
    nkf_p_thm = nkf_thm_modul.nkf_p_thm_fn(A,nkf_p_duz,q_p_matris,delta_t,t)  # NKF & EKF icin ortak kullanım

    #---KAZANC BLOK---#
    #EKF icin kazanc_modul 
    ekf_K_S = ekf_kazanc_modul.ekf_kazanc_fn(ekf_H , ekf_p_thm , R , t)
    ekf_K = ekf_K_S[0]   
    ekf_S = ekf_K_S[1] 
    #NKF icin kazanc_modul 
    nkf_K_S = nkf_kazanc_modul.nkf_kazanc_fn(nkf_H , nkf_p_thm , R , t)
    nkf_K = nkf_K_S[0]   
    nkf_S = nkf_K_S[1] 

    #---update BLOK---#
    #EKF icin update_modul 
    ekf_x_duz = ekf_duz_modul.ekf_x_duz_fn(zk , ekf_x_thm , ekf_K , x_orj , t)  #EKF  
    ekf_p_duz = ekf_duz_modul.ekf_p_duz_fn(ekf_p_thm , ekf_K , ekf_S , t)  # EKF
    #NKF icin update_modul 
    nkf_x_duz = nkf_duz_modul.nkf_x_duz_fn(zk , nkf_H , nkf_x_thm , nkf_K , x_orj , t)  #EKF  
    nkf_p_duz = nkf_duz_modul.nkf_p_duz_fn(nkf_p_thm , nkf_K , nkf_S , t)  # EKF


    ### GRAFIK ###  
    grafik_cizim.cizim(zk,x_orj,nkf_x_thm,ekf_x_thm)

    ### Performans ### 
    performans.prf_fn(x_orj,nkf_x_thm,ekf_x_thm,t)

    return ekf_x_duz, ekf_p_duz, nkf_x_duz, nkf_p_duz