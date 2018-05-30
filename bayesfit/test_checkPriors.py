"""
*******************************************************
*
*  test_check_priors - UNIT TEST FOR TRAVIS WITH CHECK PRIORS
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   May 29, 2018
*  Last updated: May 29, 2018
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

def _check_priors(branch):    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Specify param_constraints
    param_constraints = [True, True, True, True]
    # Choose branch that defines sigmoid fit   
    if branch == 0:
        priors = ['Raise(0.5, 2)', 'Error(3,0.5)'] 
    elif branch == 1:
        priors = ['Norm(10150, 2)', 'Beta(3,0.5)']      
    # Use BayesFit to fit function
    trace, metrics, options = bf.fitmodel(data, 
                                          param_constraints = param_constraints,
                                          priors = priors)
    # Update success flag
    success = 1
    return success 


#################################################################
#  UNIT TESTS
#################################################################

def test_check_priors_branch0():
    raised = False
    try:
        _check_priors(0)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_check_priors_branch1():
    raised = False
    try:
        _check_priors(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
