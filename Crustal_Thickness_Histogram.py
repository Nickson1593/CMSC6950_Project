import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')

#Establish Z Variable
Z = data[:, 2]


