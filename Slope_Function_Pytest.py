import Slope_Function 
import numpy as np
import pytest

expected_slope = np.degrees(np.arctan(0.1)))

@pytest.mark.parametrize("X, Y, Z, expected_mean_slope", 
			[([0, 5, 0, 9],
			[0, 0, 6, 9],
			[0, 0, 0, 0],
			0),
			([0, 10, 0, 7],
			[0, 0, 7, 7],
			[0, 1, 0, 1], 
			5.71),
			([0, 5, 0, 9],
			[0, 0, 5, 9],
			[0, 0, 2, 2],
			11.3)])
def test_slope_function(X, Y, Z, expected_mean_slope):
    return test_sope_function


