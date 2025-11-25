import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from file
data = pd.read_csv('Crustal_Thickness_CMSC6950.txt')

#Establish Z Variable
Crustal_Thickness = data['Z'].values

#Define Bin Ranges for Crustal Thickness
bins = [0, 1.4, 2.8, 4.2, 5.6, 7.0, 8.4, 9.8, 11.2, 12.6, 14, 15.4, 16.8]
bins_labels = ['0-1.4 km', '1.4-2.8 km', '2.8-4.2 km', '4.2-5.6 km', '5.6-7.0 km', '7.0-8.4 km', '8.4-9.8 km', '9.8-11.2 km', '11.2-14 km', '14-15.4 km', '15.4-16.8 km']

#Calculate Percentages of Points Within Each Range
counts, range_edges = np.histogram(Crustal_Thickness, bins=bins)
Total_Points = len(Crustal_Thickness)
Percentages = (counts / Total_Points) * 100


