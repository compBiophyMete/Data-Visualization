import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df_rmsd= pd.read_csv('RMSDcluster1.csv', sep=',', header=None)
df_rmsd.columns = ['moleculeNo', 'RMSD', 'STD']
molNo = df_rmsd['moleculeNo']
rmsd = df_rmsd['RMSD']
std = df_rmsd['STD']
df_deltaG = pd.read_csv('PRODIGYcluster1.csv', sep=',', header=None)
df_deltaG.columns = ['moleculeNo', 'deltaG', 'STD']
deltaG = df_deltaG['deltaG']
deltaG_std = df_deltaG['STD']
print('Genarating the plots...')
fig = plt.figure()
gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True)
axs[0].plot(molNo, rmsd, 'k')
axs[0].fill_between(molNo, rmsd-std, rmsd+std, alpha=0.4, edgecolor='#FF0000', facecolor='#FF0000')
axs[1].plot(molNo, deltaG, 'k')
axs[1].fill_between(molNo, deltaG-deltaG_std, deltaG+deltaG_std, alpha=0.4, edgecolor='#FF0000', facecolor='#FF0000')
axs[0].tick_params(axis='both', which='major', labelsize=13)
axs[1].tick_params(axis='both', which='major', labelsize=13)
fig.supxlabel('Molecule no.', fontweight = 'bold', fontsize='16')
axs[0].set_ylabel('RMSD (nm)', fontsize='15', fontweight='bold')
axs[1].set_ylabel('ΔGpred (kcal/mol)', fontsize='15', fontweight='bold')
axs[1].set_ylim(-7.55,-4.50)
from matplotlib.ticker import StrMethodFormatter
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}')) # 2 decimal places
plt.savefig('MDcluster1.png', dpi=300, bbox_inches='tight')
plt.show()
