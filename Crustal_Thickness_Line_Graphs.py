import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

#Read Crustal Thickness data from file
df = pd.read_csv('Crustal_Thickness_Supplementary_Data.csv', sep='\s+', header=None)

#Define Data Columns
df.columns = ['X1', 'Y1', 'Z1', 'X2', 'Y2', 'Z2', 'X3', 'Y3', 'Z3']

#Define Variables
X1 = df['X1']
X2 = df['X2']
X3 = df['X3']
Z1 = df['Z1']
Z2 = df['Z2']
Z3 = df['Z3']

#Define Initial Thickness of Undeformed Crust
initial_thickness = 10557.39883

#Calculate Stretching Factors
stretching_factor_Z1 = initial_thickness / df['Z1']
stretching_factor_Z2 = initial_thickness / df['Z2']
stretching_factor_Z3 = initial_thickness / df['Z3']

#Set Maximum Stretching Factor
max_stretching_factor = 7.0
clipped_stretching_factor_Z1 = np.clip(stretching_factor_Z1, a_min=None, a_max=max_stretching_factor)
clipped_stretching_factor_Z2 = np.clip(stretching_factor_Z2, a_min=None, a_max=max_stretching_factor)
clipped_stretching_factor_Z3 = np.clip(stretching_factor_Z3, a_min=None, a_max=max_stretching_factor)

#Setup Line Graphs
fig, axs = plt.subplots(3, 1, figsize=(16,14), sharex=True)

#Plot Line 1
ax1 = axs[0]
ax1.tick_params(axis='x', labelsize=14)
ax1.set_xlabel('Easting (m)', fontsize=18)
line1, = ax1.plot(df['X1'], df['Z1'], color='red', label='Crustal Thickness')
ax1_twin = ax1.twinx()
ax1_twin.set_ylabel('Stretching Factor', fontsize=18)
ax1_twin.tick_params(axis='y', labelsize=14)
line2, = ax1_twin.plot(df['X1'], clipped_stretching_factor_Z1, color='red', linestyle='--', label='Stretching Factor')

#Lines 1 & 2 Legend
lines = [line1, line2]
labels = [l.get_label() for l in lines] 
ax1.legend(lines, labels, loc='best') 

#Plot Line 2
ax2 = axs[1]
ax2.tick_params(axis='x', labelsize=14)
ax2.set_xlabel('Easting (m)', fontsize=18)
line3, = ax2.plot(df['X2'], df['Z2'], color='orange', label='Crustal Thickness')
ax2_twin = ax2.twinx()
ax2_twin.set_ylabel('Stretching Factor', fontsize=18)
ax2_twin.tick_params(axis='y', labelsize=14)
line4, = ax2_twin.plot(df['X2'], clipped_stretching_factor_Z2, color='orange', linestyle='--', label='Stretching Factor')

#Lines 3 & 4 Legend
lines = [line3, line4]
labels = [l.get_label() for l in lines] 
ax2.legend(lines, labels, loc='best') 

#Plot Lines 5 & 6
ax3 = axs[2]
ax3.tick_params(axis='x', labelsize=14)
ax3.set_xlabel('Easting (m)', fontsize=18)
line5, = ax3.plot(df['X3'], df['Z3'], color='blue', label='Crustal Thickness')
ax3_twin = ax3.twinx()
ax3_twin.set_ylabel('Stretching Factor', fontsize=18)
ax3_twin.tick_params(axis='y', labelsize=14)
line6, = ax3_twin.plot(df['X3'], clipped_stretching_factor_Z3, color='blue', linestyle='--', label='Stretching Factor')

#Lines 5 & 6 Legend
lines = [line5, line6]
labels = [l.get_label() for l in lines] 
ax3.legend(lines, labels, loc='best') 

#Format Layout
plt.tight_layout()
plt.show()
