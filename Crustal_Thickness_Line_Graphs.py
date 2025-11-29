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


