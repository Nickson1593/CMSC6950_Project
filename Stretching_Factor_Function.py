import numpy as np
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter

'#Define Stretching Factor Function'
def stretching_factor_calculation(input_data):

    '#Load Data'
    data = input_data

    '#Establish XYZ Variables'
    X, Y, Z = data[:, 0], data[:, 1], data[:, 2]

    '#Create Grid Mesh'
    x = np.linspace(X.min(), X.max(), 100)
    y = np.linspace(Y.min(), Y.max(), 100)
    X1, Y1 = np.meshgrid(x, y)

    '#Interpolate Z Values'
    Z1 = griddata((X, Y), Z, (X1, Y1), method='linear')

    '#Smooth Interpolation'
    smoothed_Z1 = gaussian_filter(Z1, sigma=0.8)

    '#Calculate Stretching Factor'
    stretching_factor = 10557.39883 / smoothed_Z1

    '#Set Maximum Stretching Factor'
    max_stretching_factor = 7.0
    clipped_stretching_factor = np.clip(stretching_factor, a_min=None,
                                        a_max=max_stretching_factor)

    return X1, Y1, smoothed_Z1, clipped_stretching_factor
