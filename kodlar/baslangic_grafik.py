import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random

#################################### 
###### x_orj :  ground truth   #####
####################################

def ilk_veriler(delta_t):

    #////////////Grafik - BAS//////////////
    plt.subplot(311)
    plt.title("EKF & NKF Tahmin - Orj - Olcum")
    #plt.xlabel("X Konumu")
    plt.ylabel("Y Konumu")
    plt.grid() # ızgara ekleme

    plt.subplot(312)
    plt.title("NKF Tahmin - Orj - Olcum")
    #plt.xlabel("X Konumu")
    plt.ylabel("Y Konumu")
    plt.grid() # ızgara ekleme

    plt.subplot(313)
    plt.title("EKF Tahmin - Orj - Olcum")
    plt.xlabel("X Konumu")
    plt.ylabel("Y Konumu")
    plt.grid() # ızgara ekleme
    #////////////Grafik - SON//////////////

    

    # A matris tanımı
    A = np.eye(4);
    A[0, 1] = delta_t
    A[2, 3] = delta_t

    #EKF & NKF icin ortak ORJ denklem (Groundtruth) için ilk tanım
    x_orj = np.zeros((4, 1))
    x_orj[0, 0] = 1
    x_orj[1, 0] = 5
    x_orj[2, 0] = 2
    x_orj[3, 0] = 5

    #EKF DUZELTME X & P için ilk tanımlar
    ekf_x_duz = np.zeros((4,1))
    ekf_x_duz[0, 0] = 0.9
    ekf_x_duz[1, 0] = 5
    ekf_x_duz[2, 0] = 1.9
    ekf_x_duz[3, 0] = 5
    ekf_p_duz = np.eye((4))

    #EKF --Tahmin modulunda kovaryans icinde kullanilacak
    q_p_matris = np.eye(2)*(0.01**2)  # NKF & EKF icin ortak kullanım

    #-- Kazancda kullanilacak olan R
    R = np.eye(2)
    R[0, 0] = 5**2  # r icin
    R[1, 1] = math.radians(0.5)**2  # teta icin

    
    
    return A,x_orj,ekf_x_duz,ekf_p_duz,q_p_matris,R

def orneklem_adedi_fn():
    orneklem_adedi = 30 # tekrar sayisi
    return orneklem_adedi

def ivme_durum_fn(t):
    ivme_durumu = 0 # ivme_durumu = 0 iseivmesiz hareket. Digerleri ivmeli hareket
    ivme = 0.1
    ivme_vektor = np.zeros((4, 1))
    ivme_vektor[0, 0] = 0.5*ivme*t*t
    ivme_vektor[1, 0] = ivme*t
    ivme_vektor[2, 0] = 0.5*ivme*t*t
    ivme_vektor[3, 0] = ivme*t
    return ivme_durumu,ivme_vektor