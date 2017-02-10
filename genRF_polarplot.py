# import numpy as np
# import scipy as sp
# import matplotlib.pyplot as plt
# import pandas as pd
# import os 
# from pylab import *
# %matplotlib inline 




# theta = np.arange(0, 2*np.pi, 0.01)

# #r0 = (1.14 + 0.29) * (1 + 0.1 * np.sin(0 * theta + 0))
# r5 = (1.14 + 0.29) * (1 + 0.1 * np.sin(5 * theta + 0))
# r25 = (1.14 + 0.29) * (1 + 0.1 * np.sin(25 * theta + 0))

# plt.figure(figsize=(4, 4)) 
# ax = plt.subplot(111, projection='polar')
# ax.plot(theta, r5, color= "blue", lw=3)
# ax.plot(theta, r25, color= 'red', lw=3)
# ax.set_rmax(2)
# ax.set_rticks([0.5, 1, 1.5])  # less radial ticks
# ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
# ax.grid(True, lw=2) 



# rc('axes', linewidth=3)
# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontsize(12)
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontsize(8)
#     tick.label1.set_fontweight('bold')
# # plt.show()
    
# thetaticks = np.arange(0,360,45)

# # set ticklabels location at 1.3 times the axes' radius
# ax.set_thetagrids(thetaticks, frac=1.15)
    

# plt.savefig("Exp1_RFpolarPlot.png", dpi=100)




# plt.figure(figsize=(8, 4)) 
# degs = theta * (180/np.pi)  
# ax = plt.subplot(111)
# ax.plot(degs,r5, color = "blue", lw=3)
# ax.plot(degs,r25, color = "red", lw=2, alpha = 1)
# ax.axis([0, 360, (1.45 -0.5), (1.45 + 0.5)] )
# ax.xaxis.set_tick_params(width=2, length=6)
# ax.yaxis.set_tick_params(width=2, length=6)
# plt.xlabel('Polar angle', fontsize=16, fontweight="bold")
# plt.ylabel('Radius (Degrees)', fontsize=16, fontweight="bold")
# rc('axes', linewidth=3)
# # ax.xaxis.labelpad = 15

# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontsize(12)
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontsize(12)
#     tick.label1.set_fontweight('bold')

# plt.savefig("Exp1_RFsinPlot.png", dpi=100)





# plt.figure(figsize=(8, 4)) 
# degs = theta * (180/np.pi)  
# ax = plt.subplot(111)
# ax.plot(degs,rComp, color = "black", lw=2.5)
# ax.axis([0, 360, (1.45 -0.5), (1.45 + 0.5)] )
# ax.xaxis.set_tick_params(width=2, length=6)
# ax.yaxis.set_tick_params(width=2, length=6)
# plt.xlabel('Polar angle', fontsize=16, fontweight="bold")
# plt.ylabel('Radius (Degrees)', fontsize=16, fontweight="bold")
# rc('axes', linewidth=3)
# ax.xaxis.labelpad = 5

# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontsize(12)
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontsize(12)
#     tick.label1.set_fontweight('bold')


# plt.savefig("Exp1_RFsinPlot_2.png", dpi=100)






# rComp = (1.14 + 0.29) * (1 + 0.1 * np.sin(5 * theta + 0) + 0.1 * np.sin(25 * theta + 0))
# plt.figure(figsize=(4, 4)) 
# ax = plt.subplot(111, projection='polar')
# ax.plot(theta, rComp, color= "black", lw=3)
# ax.set_rmax(2)
# ax.set_rticks([0.5, 1, 1.5])  # less radial ticks
# ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
# ax.grid(True, lw=1) 


# rc('axes', linewidth=3)
# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontsize(12)
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontsize(8)
#     tick.label1.set_fontweight('bold')
    
# thetaticks = np.arange(0,360,45)

# # set ticklabels location at 1.3 times the axes' radius
# ax.set_thetagrids(thetaticks, frac=1.15)
    

# # plt.show()
    

# plt.savefig("Exp1_RFpolarPlot_2.png", dpi=100)