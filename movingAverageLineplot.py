import numpy as np
import matplotlib.pyplot as plt
import os,glob
import seaborn as sb
from matplotlib.font_manager import FontProperties
rep1_pro, rep1_dist, rep2_pro, rep2_dist, rep3_pro, rep3_dist, rep4_pro, rep4_dist = [],[],[],[],[],[],[],[]
print('Reading the data files...')
df1p=open('df1_PRO.xvg', 'r')
df1r=open('df1_DIST.xvg', 'r')
df2p=open('df2_PRO.xvg', 'r')
df2r=open('df2_DIST.xvg', 'r')
df3p=open('df3_PRO.xvg', 'r')
df3r=open('df3_DIST.xvg', 'r')
df4p=open('df4_PRO.xvg', 'r')
df4r=open('df4_DIST.xvg', 'r')
print('Post-processing...')
for line in df1p :
    line = line.split()
    if len(line) == 2 :
        rep1_pro.append(float(line[1]))
for line in df1r :
    line = line.split()
    if len(line) == 2 :
        rep1_dist.append(float(line[1]))
for line in df2p :
    line = line.split()
    if len(line) == 2 :
        rep2_pro.append(float(line[1]))
for line in df2r :
    line = line.split()
    if len(line) == 2 :
        rep2_dist.append(float(line[1]))
for line in df3p :
    line = line.split()
    if len(line) == 2 :
        rep3_pro.append(float(line[1]))
for line in df3r :
    line = line.split()
    if len(line) == 2 :
        rep3_dist.append(float(line[1]))
for line in df4p :
    line = line.split()
    if len(line) == 2 :
        rep4_pro.append(float(line[1]))
for line in df4r :
    line = line.split()
    if len(line) == 2 :
        rep4_dist.append(float(line[1]))
print('Calculating the number of frames...')
rep1 = np.linspace(0, (int(len(rep1_pro))-1)/10, int(len(rep1_pro)))
rep2 = np.linspace(0, (int(len(rep2_pro))-1)/10, int(len(rep2_pro)))
rep3 = np.linspace(0, (int(len(rep3_pro))-1)/10, int(len(rep3_pro)))
rep4 = np.linspace(0, (int(len(rep4_pro))-1)/10, int(len(rep4_pro)))

#Moving average
def movingaverage(interval, window_size):
    window= np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')
rep1_pro = movingaverage(rep1_pro, 50)
rep2_pro = movingaverage(rep2_pro, 50)
rep3_pro = movingaverage(rep3_pro, 50)
rep4_pro = movingaverage(rep4_pro, 50)
rep1_dist = movingaverage(rep1_dist, 50)
rep2_dist = movingaverage(rep2_dist, 50)
rep3_dist = movingaverage(rep3_dist, 50)
rep4_dist = movingaverage(rep4_dist, 50)
print('Genarating the plots...')
fig = plt.figure()
gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True, sharey=True)
axs[0].plot(rep1, rep1_pro, 'purple')
axs[0].plot(rep2, rep2_pro, 'tab:purple')
axs[0].plot(rep3, rep3_pro, 'darkorchid')
axs[0].plot(rep4, rep4_pro, 'darkviolet')
axs[1].plot(rep1, rep1_dist, 'brown')
axs[1].plot(rep2, rep2_dist, 'tab:brown')
axs[1].plot(rep3, rep3_dist, 'firebrick')
axs[1].plot(rep4, rep4_dist, 'darkred')

axs[0].tick_params(axis='both', which='major', labelsize=13)
axs[1].tick_params(axis='both', which='major', labelsize=13)
fig.supxlabel('Time \ ns', style='italic', fontsize='16')
plt.xlim(0,len(rep1)/10)
fig.supylabel('Change with respect to initial state \ nm' , style='italic', fontsize='16')
plt.savefig('RMSDUbqs.png', dpi=300)
