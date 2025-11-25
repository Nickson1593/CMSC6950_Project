import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from file
data = pd.read_csv('Crustal_Thickness_CMSC6950.txt')

#Establish Z Variable
Crustal_Thickness = data['Z'].values

#Define Bin Ranges for Crustal Thickness
Crustal_Thickness_Ranges = [0, 1.4, 2.8, 4.2, 5.6, 7.0, 8.4, 9.8, 11.2, 12.6, 14, 15.4, 16.8]
