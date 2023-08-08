import numpy as np
from numpy import inf
import matplotlib as mpl
from pylab import *
from matplotlib import cm
import pandas as pd
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from matplotlib.image import NonUniformImage
from scipy.stats import kde
import os,glob
import seaborn as sb
import scipy.stats as stats
from matplotlib.font_manager import FontProperties
from scipy.stats import norm
rep1 = pd.read_csv('rep1.csv', sep=',', header=None)
rep1.columns = ['proj1', 'proj2']
rep2 = pd.read_csv('rep2.csv', sep=',', header=None)
rep2.columns = ['proj1', 'proj2']
rep3 = pd.read_csv('rep3.csv', sep=',', header=None)
rep3.columns = ['proj1', 'proj2']
rep4 = pd.read_csv('rep4.csv', sep=',', header=None)
rep4.columns = ['proj1', 'proj2']

rep1_x = rep1['proj1']
rep1_y = rep1['proj2']
rep2_x = rep2['proj1']
rep2_y = rep2['proj2']
rep3_x = rep3['proj1']
rep3_y = rep3['proj2']
rep4_x = rep4['proj1']
rep4_y = rep4['proj2']

rep1_x=np.asarray(rep1_x)
rep1_y=np.asarray(rep1_y)
rep2_x=np.asarray(rep2_x)
rep2_y=np.asarray(rep2_y)
rep3_x=np.asarray(rep3_x)
rep3_y=np.asarray(rep3_y)
rep4_x=np.asarray(rep4_x)
rep4_y=np.asarray(rep4_y)

rep1_H, rep1_xedges, rep1_yedges = np.histogram2d(rep1_x, rep1_y, bins=(51,51), density=True)
rep1_dummyVariable, rep1_xedges, rep1_yedges = np.histogram2d(rep1_x, rep1_y, bins=(50,50), density=True)
rep1_H = rep1_H.T


rep2_H, rep2_xedges, rep2_yedges = np.histogram2d(rep2_x, rep2_y, bins=(51,51), density=True)
rep2_dummyVariable, rep2_xedges, rep2_yedges = np.histogram2d(rep2_x, rep2_y, bins=(50,50), density=True)
rep2_H = rep2_H.T

rep3_H, rep3_xedges, rep3_yedges = np.histogram2d(rep3_x, rep3_y, bins=(51,51), density=True)
rep3_dummyVariable, rep3_xedges, rep3_yedges = np.histogram2d(rep3_x, rep3_y, bins=(50,50), density=True)
rep3_H = rep3_H.T

rep4_H, rep4_xedges, rep4_yedges = np.histogram2d(rep4_x, rep4_y, bins=(51,51), density=True)
rep4_dummyVariable, rep4_xedges, rep4_yedges = np.histogram2d(rep4_x, rep4_y, bins=(50,50), density=True)
rep4_H = rep4_H.T

rep1_energy = -np.log(rep1_H)*0.001987204259*310.15
rep2_energy = -np.log(rep2_H)*0.001987204259*310.15
rep3_energy = -np.log(rep3_H)*0.001987204259*310.15
rep4_energy = -np.log(rep4_H)*0.001987204259*310.15

minEnergy = [np.min(rep1_energy), np.min(rep2_energy), np.min(rep3_energy), np.min(rep4_energy)]
rep1_energy = rep1_energy - np.min(minEnergy)
rep2_energy = rep2_energy - np.min(minEnergy)
rep3_energy = rep3_energy - np.min(minEnergy)
rep4_energy = rep4_energy - np.min(minEnergy)
maxEnergy = np.max([np.max(rep1_energy),np.max(rep2_energy),np.max(rep3_energy),np.max(rep4_energy)])

xlimSet = [np.min(rep1_x), np.max(rep1_x), np.min(rep2_x), np.max(rep2_x),np.min(rep3_x), np.max(rep3_x),np.min(rep4_x), np.max(rep4_x)]
ylimSet = [np.min(rep1_y), np.max(rep1_y), np.min(rep2_y), np.max(rep2_y),np.min(rep3_y), np.max(rep3_y),np.min(rep4_y), np.max(rep4_y)]

fig, axs = plt.subplots(2, 2, figsize=(15, 15), sharey=True, sharex=True, gridspec_kw = {'wspace':0, 'hspace':0})


cmap= cm.get_cmap('tab20b',20)
for i in range(cmap.N) :
    rgba=cmap(i)

im1 = axs[0,0].contourf(rep1_xedges,rep1_yedges,rep1_energy, cmap='turbo', vmin=0, vmax=3.6)
im2 = axs[0,1].contourf(rep2_xedges,rep2_yedges,rep2_energy, cmap='turbo', vmin=0, vmax=3.6)
im3 = axs[1,0].contourf(rep3_xedges,rep3_yedges,rep3_energy, cmap='turbo', vmin=0, vmax=3.6)
im4 = axs[1,1].contourf(rep4_xedges,rep4_yedges,rep4_energy, cmap='turbo', vmin=0, vmax=3.6)
fig.subplots_adjust(bottom=0.1, top=0.9, left=0.1, right=0.8,
                    wspace=0.02, hspace=0.02)

cbar = fig.colorbar(im2, ax=axs.ravel().tolist(), shrink=1.0)
cbar.ax.tick_params(labelsize=23)
cbar.set_label('ΔG (kcal/mol)', rotation=90, fontsize=23, fontweight='bold')

axs[0,0].tick_params(axis='both', which='major', labelsize=23)
axs[0,1].tick_params(axis='both', which='major', labelsize=23)
axs[1,0].tick_params(axis='both', which='major', labelsize=23)
axs[1,1].tick_params(axis='both', which='major', labelsize=23)
fig.supxlabel('PC-1', fontweight='bold', fontsize='25')
fig.supylabel('PC-2', fontweight='bold', fontsize='25')
plt.xlim(np.min(xlimSet),np.max(xlimSet),0.2)
plt.ylim(np.min(ylimSet),np.max(ylimSet),0.2)
plt.savefig('APOzwitterionic.png', dpi=400, bbox_inches='tight')
plt.show()
