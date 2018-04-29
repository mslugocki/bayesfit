"""
*******************************************************
*
*  test_plots - UNIT TEST FOR TRAVIS CI
*  
*  Version:      Version 2.0
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 28, 2017
*  Last updated: April 28, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES 
#################################################################
import numpy as np
import bayesfit as bf


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _check_geweke_plot():    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Use BayesFit to fit function
    trace, metrics, options = bf.fitmodel(data)
    # Generate geweke plot
    bf.geweke_plot(trace = trace['alpha'], intervals = 10, length = 300)
    # Update success flag
    success = 1
    return success 

def _check_plot_cdf():    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Use BayesFit to fit function
    trace, metrics, options = bf.fitmodel(data)
    # Generate cdf plot
    bf.plot_cdf(data, metrics, options)
    # Update success flag
    success = 1
    return success 

#################################################################
#  UNIT TESTS
#################################################################

def test_check_geweke_plot():
    success = _check_geweke_plot()
    # Assert if exception   
    assert success == 1

def test_check_plot_cdf():
    success = _check_plot_cdf()
    # Assert if exception   
    assert success == 1