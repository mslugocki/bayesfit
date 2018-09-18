"""
*******************************************************
*
*  test_bayesfit - UNIT TEST FOR TRAVIS CI
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

def _check_bayesfit_psyfunctions(branch):    
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
    elif branch == 6:
        sigmoid_type = 'norm'
    # Use BayesFit to fit function
    metrics, options = bf.fitmodel(data, sigmoid_type = sigmoid_type, logspace=False)
    # Update success flag
    success = 1
    return success 

def _check_bayesfit_param_constraints(branch):    
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
    if branch == 0:
        param_free = [True, True, False, False]
    elif branch == 1:
        param_free = [True, True, True, False]      
    elif branch == 2:
        param_free = [True, True, True, True]
    # Use BayesFit to fit function
    metrics, options = bf.fitmodel(data, param_free = param_free, density = 20)
    # Update success flag
    success = 1
    return success 

def _check_bayesfit_priors():    
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
    priors = ['Norm(0.005,0.001)', 'Norm(3,0.75)', None, None]
    metrics, options = bf.fitmodel(data, priors = priors, sigmoid_type='weibull', logspace=False)
    # Update success flag
    success = 1
    return success 

def _check_bayesfit_batch_process(branch):    
    # Generate dataset 
    data_batch = np.array([[0.0010,   45.0000,   90.0000],
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
    # Create batch data object 
    data = dict()
    data['data01'] = data_batch
    data['data02'] = data_batch
    # Choose branch that defines sigmoid fit   
    if branch == 0:
        param_free = [True, True, False, False]
    elif branch == 1:
        param_free = [True, True, True, False]      
    elif branch == 2:
        param_free = [True, True, True, True]
    # Use BayesFit to fit function
    metrics, options = bf.fitmodel(data, batch = True, param_free = param_free, density = 20)
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

def test_check_bayesfit_psyfunctions_branch6():
    success = _check_bayesfit_psyfunctions(6)
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

def test_check_bayesfit_batch_process_branch0():
    success = _check_bayesfit_batch_process(0)
    # Assert if exception  
    assert success == 1    

def test_check_bayesfit_batch_process_branch1():
    success = _check_bayesfit_batch_process(1)
    # Assert if exception  
    assert success == 1   

def test_check_bayesfit_batch_process_branch2():
    success = _check_bayesfit_batch_process(2)
    # Assert if exception  
    assert success == 1   

def test_check_bayesfit_priors():
    success = _check_bayesfit_priors()
    # Assert if exception  
    assert success == 1   
