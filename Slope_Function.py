import numpy as np
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter

#Define Slope Function
def surface_slope(Crustal_Thickness_With_Boundary_XYZ):
    
    #Load Data File
    data = np.loadtxt('Crustal_Thickness_With_Boundary_XYZ.txt')
    
    #Establish XYZ Variables
    X, Y, Z = data[:, 0], data[:, 1], data[:, 2]
    
    #Create Grid Mesh
    x = np.linspace(X.min(), X.max(), 100)
    y = np.linspace(Y.min(), Y.max(), 100)
    X1, Y1 = np.meshgrid(x, y)
    
    #Interpolate Z Values
    Z1 = griddata((X, Y), Z, (X1, Y1), method = 'cubic')
    
    #Smooth Interpolation
    smoothed_Z1 = gaussian_filter(Z1, sigma = 0.8)
    
    #Define Gradients
    dzdy, dzdx = np.gradient(smoothed_Z1, y[1] - y[0], x[1] - x[0])
    
    #Calculated Gradients
    gradient = np.sqrt(dzdy**2 + dzdy**2)
    
    #Calculate Slopes
    slope = np.degrees(np.arctan(gradient)
    
    return X1, Y1, smoothed_Z1, slope
