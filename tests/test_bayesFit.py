"""
*******************************************************
*
*  test_bayesfit - UNIT TEST FOR TRAVIS CI
*  
*  Version:      Version 2.0
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 28, 2017
*  Last updated: April 29, 2018
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

def _check_bayesfit_psyfunctions(branch):    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Choose branch that defines sigmoid fit   
    if branch == 0:
        sigmoid_type = 'logistic'
    elif branch == 1:
        sigmoid_type = 'weibull'        
    elif branch == 2:
        sigmoid_type = 'gumbel'
    elif branch == 3:
        sigmoid_type = 'quick'
    elif branch == 4:
        sigmoid_type = 'log-quick'
    elif branch == 5:
        sigmoid_type = 'hyperbolic'
    # Use BayesFit to fit function
    trace, metrics, options = bf.fitmodel(data, sigmoid_type = sigmoid_type)
    # Update success flag
    success = 1
    return success 

def _check_bayesfit_param_constraints(branch):    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Choose branch that defines sigmoid fit   
    if branch == 0:
        param_constraints = [True, True, False, False]
    elif branch == 1:
        param_constraints = [True, True, True, False]      
    elif branch == 2:
        param_constraints = [True, True, True, True]
    # Use BayesFit to fit function
    trace, metrics, options = bf.fitmodel(data, param_constraints = param_constraints)
    # Update success flag
    success = 1
    return success 

#################################################################
#  UNIT TESTS
#################################################################

def test_check_bayesfit_psyfunctions_branch0():
    success = _check_bayesfit_psyfunctions(0)
    # Assert if exception  
    assert success == 1


def test_check_bayesfit_psyfunctions_branch1():
    success = _check_bayesfit_psyfunctions(1)
    # Assert if exception  
    assert success == 1
    
def test_check_bayesfit_psyfunctions_branch2():
    success = _check_bayesfit_psyfunctions(2)
    # Assert if exception  
    assert success == 1
    
def test_check_bayesfit_psyfunctions_branch3():
    success = _check_bayesfit_psyfunctions(3)
    # Assert if exception  
    assert success == 1
    
def test_check_bayesfit_psyfunctions_branch4():
    success = _check_bayesfit_psyfunctions(4)
    # Assert if exception  
    assert success == 1

def test_check_bayesfit_psyfunctions_branch5():
    success = _check_bayesfit_psyfunctions(5)
    # Assert if exception  
    assert success == 1  
    
    
def test_check_bayesfit_param_constraints_branch0():
    success = _check_bayesfit_param_constraints(0)
    # Assert if exception  
    assert success == 1    
    
def test_check_bayesfit_param_constraints_branch1():
    success = _check_bayesfit_param_constraints(1)
    # Assert if exception  
    assert success == 1      
    
def test_check_bayesfit_param_constraints_branch2():
    success = _check_bayesfit_param_constraints(2)
    # Assert if exception  
    assert success == 1     