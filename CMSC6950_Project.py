import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Set fonts
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=15)

# Load data from file
data = np.loadtxt('Crustal_Thickness_CMSC6950.txt')
