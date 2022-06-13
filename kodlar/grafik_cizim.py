import numpy as np
import matplotlib.pyplot as plt
import math
import random
from numpy import random



def cizim(zk,x_orj,nkf_x_thm,ekf_x_thm):
    
    # z_x & z_y bunlar r ve tetayı X ve Y ye dönüştürür sonrasında çizimde kullanılacak
    z_x = zk[0,0]*math.sin(zk[1,0])
    z_y = zk[0,0]*math.cos(zk[1,0])

    plt.subplot(311) #NKF & EKF
    plt.plot(z_y, z_x, c='y', marker="o") # OLCUM
    plt.plot(x_orj[0], x_orj[2], c='r', marker="X") # ORJ SINYAL
    plt.plot(nkf_x_thm[0], nkf_x_thm[2], c='g', marker="^") # NKF THM(predic.)
    plt.plot(ekf_x_thm[0], ekf_x_thm[2], c='b', marker="^") # EKF THM(predic.)

    plt.subplot(312) #NKF
    plt.plot(z_y, z_x, c='y', marker="o") # OLCUM
    plt.plot(x_orj[0], x_orj[2], c='r', marker="X") # ORJ SINYAL
    plt.plot(nkf_x_thm[0], nkf_x_thm[2], c='g', marker="^") # NKF THM(predic.)

    plt.subplot(313) #EKF
    plt.plot(z_y, z_x, c='y', marker="o") # OLCUM
    plt.plot(x_orj[0], x_orj[2], c='r', marker="X") # ORJ SINYAL
    plt.plot(ekf_x_thm[0], ekf_x_thm[2], c='b', marker="^") # EKF THM(predic.)
    

    plt.pause(0.01)

    return 0