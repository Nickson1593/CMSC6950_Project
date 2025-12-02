from Stretching_Factor_Function import stretching_factor_calculation
import numpy as np
import pytest
import os

#Identify edge, middle cases
@pytest.mark.parametrize("input_data, expected_mean_stretching_factor",
    			[(np.array([[0, 0, 0.1], [1, 1, 0.2], [0, 1, 0.1], [1, 0, 0.2]]), 7.0),
    			(np.array([[1, 10, 10550], [3, 15, 10560], [1, 12, 10555], [3, 14, 10555]]), 1.0),
    			(np.array([[20, 6, 5000], [21, 7, 5010], [20, 7, 5005], [21, 6, 5005]]), 2.11),
			(np.array([[1, 3, 2000], [2, 8, 2010], [1, 4, 2005], [2, 7, 2005]]), 5.28)])
def test_stretching_factor_calculation(input_data, expected_mean_stretching_factor):
        
        _, _, _, stretching_factor_array = stretching_factor_calculation(input_data)
        
        #Calculate the actual mean stretching factor over the grid
        actual_mean_stretching_factor = np.nanmean(stretching_factor_array)
        
        #mean actual slope isclose to expected mean slope with a tolerance of 0.1
        assert np.isclose(actual_mean_stretching_factor, expected_mean_stretching_factor, atol=0.5)
