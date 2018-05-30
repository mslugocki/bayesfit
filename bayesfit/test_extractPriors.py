"""
*******************************************************
*
*  test_extract_priors - UNIT TEST FOR TRAVIS WITH EXTRACT PRIORS
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

def _check_extract_priors(branch):    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Specify param_constraints
    param_constraints = [True, True, True, True]
    # Choose branch that defines sigmoid fit   
    if branch == 0:
        priors = ['Norm(0.5,2)']
    elif branch == 1:
        priors = ['Norm(0.5,2)', 'Beta(3,0.5)']      
    elif branch == 2:
        priors = ['Norm(0.5,2)', 'Beta(3,0.5)', 'Norm(0.5,2)']
    elif branch == 3:
        priors = ['Norm(0.5,2)', 'Beta(3,0.5)', 'Norm(0.5,2)', 'Beta(2,20)']
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

def test_check_extract_priors_branch0():
    raised = False
    try:
        _check_extract_priors(0)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_check_extract_priors_branch1():
    success = _check_extract_priors(1)
    # Assert if exception  
    assert success == 1
    
def test_check_extract_priors_branch2():
    success = _check_extract_priors(2)
    # Assert if exception  
    assert success == 1

def test_check_extract_priors_branch3():
    success = _check_extract_priors(3)
    # Assert if exception  
    assert success == 1
