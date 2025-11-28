import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load data from file
data = pd.read_csv('Crustal_Thickness_CMSC6950.txt', sep='\s+', names=['X','Y','Z'])

#Establish Z Variable
Crustal_Thickness = data['Z'].values

#Compute Meaningful Statistics
mean_crustal_thickness = np.mean(Crustal_Thickness)
median_crustal_thickness = np.median(Crustal_Thickness)
std_dev_crustal_thickness= np.std(Crustal_Thickness)

#Define Bin Ranges for Crustal Thickness
bins = [0, 1400, 2800, 4200, 5600, 7000, 8400, 9800, 11200, 12600, 14000, 15400, 16800]
bins_labels = ['0-1.4', '1.4-2.8', '2.8-4.2', '4.2-5.6', '5.6-7.0', '7.0-8.4', '8.4-9.8', '9.8-11.2', '11.2-12.6', '12.6-14.0', '14.0-15.4', '15.4-16.8']

#Calculate Percentages of Points Within Each Range
counts, range_edges= np.histogram(Crustal_Thickness, bins=bins)
Total_Points = len(Crustal_Thickness)
Percentages = (counts / Total_Points) * 100

#Setup Bar Plot
fig, ax = plt.subplots(figsize=(12,10))


