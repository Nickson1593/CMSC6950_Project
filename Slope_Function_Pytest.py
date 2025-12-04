from Slope_Function import surface_slope 
import numpy as np
import pytest
import os

'#Identify edge, middle cases'
@pytest.mark.parametrize("X, Y, Z, expected_mean_slope", 
			[([0, 1, 0, 1],
			[0, 0, 1, 1],
			[0, 0, 0, 0],
			0),
			([0, 5, 0, 5],
			[0, 0, 5, 5],
			[0, 0.5, 0, 0.5], 
			5.71),
			([0, 10, 0, 10],
			[0, 0, 10, 10],
			[0, 0, 2, 2],
			11.3)])
def test_slope_function(X, Y, Z, expected_mean_slope):

    '#Define Filename'
    filename = 'Crustal_Thickness_With_Boundary_XYZ.txt'
    
    '#If Filename exists Load it, if not create blank file'
    if os.path.exists(filename):
       original_data = np.loadtxt(filename)
    else:
        original_data = None
  
    X1 = np.array(X)
    Y1 = np.array(Y)
    Z1 = np.array(Z)
    data_test = np.vstack([X1, Y1, Z1]).T

    '#Define the slope array, calculate mean actual slop values'
    try:
    
        np.savetxt(filename, data_test)

        _, _, _, slope_array = surface_slope(filename)
        mean_actual_slope = np.nanmean(slope_array)

        '#mean actual slope isclose to expected mean slope with a tolerance of 1'
        assert np.isclose(mean_actual_slope, expected_mean_slope, atol=1.0)

    finally:
       	np.savetxt(filename, original_data)
