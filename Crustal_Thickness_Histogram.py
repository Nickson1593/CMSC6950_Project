import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from file
data = pd.read_csv('Crustal_Thickness_CMSC6950.txt')

#Establish Z Variable
Crustal_Thickness = data['Z'].values

#Define Bin Ranges for Crustal Thickness
bins = [0, 1.4, 2.8, 4.2, 5.6, 7.0, 8.4, 9.8, 11.2]
bins_labels = ['0-1.4 km', '1.4-2.8 km', '2.8-4.2 km', '4.2-5.6 km', '5.6-7.0 km', '7.0-8.4 km', '8.4-9.8 km', '9.8-11.2 km']

#Calculate Percentages of Points Within Each Range
counts, range_edges = np.histogram(Crustal_Thickness, bins=bins)
Total_Points = len(Crustal_Thickness)
Percentages = (counts / Total_Points) * 100

#Setup Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 6))

#Subplot 1 "Count of Data Points for Ranges of Crustal Thickness"
ax1.hist (Crustal_Thickness, bins=bins, color='blue', edgecolor='black')
ax1.set_title('Count of Data Points for Ranges of Crustal Thickness', fontsize=18)
ax1.set_xlabel('Crustal Thickness (km)', fontsize=14)
ax1.set_ylabel('Number of Data Points', fontsize=14)
ax1.set_xticks(bins)

for i, count in enumerate(Total_Points):
    ax1.text(i, [i] + 1, f'{Total_Points[i]:. 1f}%', ha='center', va='top')

#Subplot 2 "Percentage of Total Data Points Found in Each Range of Crustal Thickness"
ax2.hist (bins_labels, Percentages, color='red', edgecolor='black')
ax2.set_title('Percentage of Total Data Points For Range of Crustal Thickness"', fontsize=18)
ax2.set_xlabel('Range of Crustal Thickness (km)', fontsize=14)
ax2.set_ylabel('Percentage of Total Data Points (%)', fontsize=14)
ax2.set_xticks(bins_labels)

#Add Percentage Values Above Bars
for i, count in enumerate(counts):
    ax2.text(i, percentages[i] + 1, f'{Percentages[i]:. 1f}%', ha='center', va='top')  
    
    
