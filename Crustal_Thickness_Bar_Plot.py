import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from file
data = pd.read_csv('Crustal_Thickness_With_Boundary_XYZ.txt', sep='\s+', names=['X', 'Y', 'Z'])

#Establish Z Variable
Crustal_Thickness = data['Z'].values

#Compute Meaningful Statistics
mean_crustal_thickness = np.mean(Crustal_Thickness)
median_crustal_thickness = np.median(Crustal_Thickness)
std_dev_crustal_thickness= np.std(Crustal_Thickness)

#Define Bin Ranges for Crustal Thickness
bins = [0, 1.4, 2.8, 4.2, 5.6, 7.0, 8.4, 9.8, 11.2]
bins_labels = ['0-1.4', '1.4-2.8', '2.8-4.2', '4.2-5.6', '5.6-7.0', '7.0-8.4', '8.4-9.8', '9.8-11.2']

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

#Add Meaninful Statistics to Plot
ax.axhline(mean_crustal_thickness, color='red', linestyle='-.', linewidth=2, label=f'Mean Crustal Thickness: {mean_crustal_thickness:.2f} msec')
ax.axhline(median_crustal_thickness, color='Magenta', linestyle=':', linewidth=3, label=f'Median Crustal Thickness: {median_crustal_thickness:.2f} msec')
ax.axhline(std_dev_crustal_thickness, color='Orange', linestyle='-', linewidth=2, label=f'Standard Deviation Crustal Thickness: {std_dev_crustal_thickness:.2f} msec')

ax.legend(fontsize=14)

#Add Percentage Values Above Bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1200, f'{Percentages[i]:.1f}%', ha='center', va='bottom', fontsize=14)

#Format Layout
plt.tight_layout()
plt.show()
 
    
