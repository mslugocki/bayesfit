"""
*******************************************************
*
*  test_plots - UNIT TEST FOR TRAVIS CI
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 28, 2017
*  Last updated: September 17, 2018
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

def _check_plot_psyfcn():    
    # Generate dataset 
    data = np.array([[0.0010,   45.0000,   90.0000],
                     [0.0015,   50.0000,   90.0000],
                     [0.0020,   44.0000,   90.0000],
                     [0.0025,   44.0000,   90.0000],
                     [0.0030,   52.0000,   90.0000],
                     [0.0035,   53.0000,   90.0000],
                     [0.0040,   62.0000,   90.0000],
                     [0.0045,   64.0000,   90.0000],
                     [0.0050,   76.0000,   90.0000],
                     [0.0060,   79.0000,   90.0000],
                     [0.0070,   88.0000,   90.0000],
                     [0.0080,   90.0000,   90.0000],
                     [0.0100,   90.0000,   90.0000]]);
    # Use BayesFit to fit function
    metrics, options = bf.fitmodel(data, sigmoid_type = 'norm')
    # Generate plot
    bf.plot_psyfcn(data, options, metrics)
    # Update success flag
    success = 1
    return success 

def _check_plot_posterior():    
    # Generate dataset 
    data = np.array([[0.0010,   45.0000,   90.0000],
                     [0.0015,   50.0000,   90.0000],
                     [0.0020,   44.0000,   90.0000],
                     [0.0025,   44.0000,   90.0000],
                     [0.0030,   52.0000,   90.0000],
                     [0.0035,   53.0000,   90.0000],
                     [0.0040,   62.0000,   90.0000],
                     [0.0045,   64.0000,   90.0000],
                     [0.0050,   76.0000,   90.0000],
                     [0.0060,   79.0000,   90.0000],
                     [0.0070,   88.0000,   90.0000],
                     [0.0080,   90.0000,   90.0000],
                     [0.0100,   90.0000,   90.0000]]);
    # Use BayesFit to fit function
    metrics, options = bf.fitmodel(data, sigmoid_type = 'norm')
    # Generate plot
    bf.plot_posterior(metrics)
    # Update success flag
    success = 1
    return success 

def _check_plot_marginals():    
    # Generate dataset 
    data = np.array([[0.0010,   45.0000,   90.0000],
                     [0.0015,   50.0000,   90.0000],
                     [0.0020,   44.0000,   90.0000],
                     [0.0025,   44.0000,   90.0000],
                     [0.0030,   52.0000,   90.0000],
                     [0.0035,   53.0000,   90.0000],
                     [0.0040,   62.0000,   90.0000],
                     [0.0045,   64.0000,   90.0000],
                     [0.0050,   76.0000,   90.0000],
                     [0.0060,   79.0000,   90.0000],
                     [0.0070,   88.0000,   90.0000],
                     [0.0080,   90.0000,   90.0000],
                     [0.0100,   90.0000,   90.0000]]);
    # Use BayesFit to fit function
    metrics, options = bf.fitmodel(data, sigmoid_type = 'norm')
    # Generate geweke plot
    bf.plot_marginals(metrics)
    # Update success flag
    success = 1
    return success 

def _check_plot_priors():    
    # Generate dataset 
    data = np.array([[0.0010,   45.0000,   90.0000],
                     [0.0015,   50.0000,   90.0000],
                     [0.0020,   44.0000,   90.0000],
                     [0.0025,   44.0000,   90.0000],
                     [0.0030,   52.0000,   90.0000],
                     [0.0035,   53.0000,   90.0000],
                     [0.0040,   62.0000,   90.0000],
                     [0.0045,   64.0000,   90.0000],
                     [0.0050,   76.0000,   90.0000],
                     [0.0060,   79.0000,   90.0000],
                     [0.0070,   88.0000,   90.0000],
                     [0.0080,   90.0000,   90.0000],
                     [0.0100,   90.0000,   90.0000]]);
    # Choose branch that defines sigmoid fit   
    priors = ['Norm(0.005,0.001)', 'Norm(3,0.75)', None, None]
    metrics, options = bf.fitmodel(data, priors = priors, sigmoid_type='weibull', logspace=False)
    # Generate geweke plot
    bf.plot_priors(options, metrics)
    # Update success flag
    success = 1
    return success 

#################################################################
#  UNIT TESTS
#################################################################

def test_check_plot_psyfcn():
    success = _check_plot_psyfcn()
    # Assert if exception   
    assert success == 1

def test_check_plot_posterior():
    success = _check_plot_posterior()
    # Assert if exception   
    assert success == 1

def test_check_plot_marginals():
    success = _check_plot_marginals()
    # Assert if exception   
    assert success == 1

def test_check_plot_priors():
    success = _check_plot_priors()
    # Assert if exception   
    assert success == 1