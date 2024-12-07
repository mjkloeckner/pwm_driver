import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

delimiter = ';'

file_data_25 = 'vgs_25.csv';
file_data_50 = 'vgs_50.csv';
file_data_75 = 'vgs_75.csv';

time_25 = genfromtxt(file_data_25, delimiter=delimiter, skip_header=1, usecols=[0])
vgs_25  = genfromtxt(file_data_25, delimiter=delimiter, skip_header=1, usecols=[1])

time_50 = genfromtxt(file_data_50, delimiter=delimiter, skip_header=1, usecols=[0])
vgs_50  = genfromtxt(file_data_50, delimiter=delimiter, skip_header=1, usecols=[1])

time_75 = genfromtxt(file_data_75, delimiter=delimiter, skip_header=1, usecols=[0])
vgs_75  = genfromtxt(file_data_75, delimiter=delimiter, skip_header=1, usecols=[1])

fig, axs = plt.subplots(3, figsize=(12, 4), sharex=True)
fig.subplots_adjust(wspace=0.15, hspace=0.15)

axs[1].set_ylabel('TENSIÓN [V]', fontsize=10)
axs[2].set_xlabel('TIEMPO [ms]', fontsize=10)

for i in range(3):
    axs[i].minorticks_on()
    axs[i].grid(True, linestyle='-', alpha=0.7)
    axs[i].grid(True, which='minor', linestyle='--', alpha=0.4)

    axs[i].tick_params(axis='y', which='minor', labelsize=8)
    axs[i].tick_params(axis='x', which='minor', labelsize=8)

    axs[i].set_xlim(0, 0.45)
    # ax.set_ylim(-0.50, 0.50)

axs[0].plot(time_25*1e3-0.037, vgs_25, '-r', markersize=1)
axs[1].plot(time_50*1e3, vgs_50, '-', color='orange', markersize=1)
axs[2].plot(time_75*1e3, vgs_75, '-b', markersize=1)

fig.legend(["CICLO DE TRABAJO 25%", "CICLO DE TRABAJO 50%", "CICLO DE TRABAJO 75%"], fontsize=10, loc='upper center', ncols=3, bbox_to_anchor=(0.5, 0.98))

# plt.show()
plt.savefig('g_vgs.png', dpi=1000, bbox_inches = 'tight')
