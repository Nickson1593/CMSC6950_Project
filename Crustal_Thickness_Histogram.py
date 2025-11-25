import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from file
data = pd.read_csv('Crustal_Thickness_CMSC6950.txt')

#Establish Z Variable
Crustal_Thickness = data['Z'].values

#Compute meaningful statistics
mean_crustal_thickness = np.mean(Crustal_Thickness)
median_crustal_thickness = np.median(Crustal_Thickness)
std_dev_crustal_thickness= np.std(Crustal_Thickness)

#Define Bin Ranges for Crustal Thickness
bins = [0, 1.4, 2.8, 4.2, 5.6, 7.0, 8.4, 9.8, 11.2]
bins_labels = ['0-1.4 km', '1.4-2.8 km', '2.8-4.2 km', '4.2-5.6 km', '5.6-7.0 km', '7.0-8.4 km', '8.4-9.8 km', '9.8-11.2 km']

#Calculate Percentages of Points Within Each Range
counts, range_edges = np.histogram(Crustal_Thickness, bins=bins)
Total_Points = len(Crustal_Thickness)
Percentages = (counts / Total_Points) * 100

#Setup Bar Plot
fig, ax = plt.subplots(figsize=(12,10))

#Plot "Count of Data Points for Ranges of Crustal Thickness"
bars = ax.bar (bins_labels, counts, color='blue', edgecolor='black', width = 0.9)
ax.set_title('Count of Data Points for Ranges of Crustal Thickness', fontsize=24)
ax.set_xlabel('Crustal Thickness (msec)', fontsize=18)
ax.set_ylabel('Number of Data Points', fontsize=18)
ax.set_xticks(bins_labels)
ax.set_xticklabels(bins_labels, rotation=20, fontsize=14)
ax.tick_params(axis='y', labelsize=14

#Add Percentage Values Above Bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1200, f'{Percentages[i]:.1f}%', ha='center', va='bottom', fontsize=14)

#Format Layout
plt.tight_layout()
plt.show()
 
    
