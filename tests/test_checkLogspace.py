"""
*******************************************************
*
*  test_checkLogspace - UNIT TEST FOR TRAVIS CI
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

def _logspace_arg():    
    # Test cases for logspace is None
    logspace = 'Not an options'    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Define sigmoid type 
    sigmoid_type = 'weibull'
    # Call function with arguments above
    bf.check_logspace(data, logspace, sigmoid_type)


def _logspace_none(branch):    
    # Test cases for logspace is None
    logspace = None    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Run through possible error types
    if branch == 0:
        # Define sigmoid type 
        sigmoid_type = 'weibull'
    elif branch == 1:
        # Define sigmoid type 
        sigmoid_type = 'weibull'
        # Add negative number to raise exception
        y[0] = -0.1
        data = np.array([x, y, N]).T
    elif branch == 2:
        # Define sigmoid type 
        sigmoid_type = 'logistic'
    # Call function with arguments above
    bf.check_logspace(data, logspace, sigmoid_type)


def _logspace_true(branch):    
    # Test cases for logspace is None
    logspace = True    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Run through possible error types
    if branch == 0:
        # Define sigmoid type 
        sigmoid_type = 'weibull'
    elif branch == 1:
        # Define sigmoid type 
        sigmoid_type = 'weibull'
        # Add negative number to raise exception
        y[0] = -0.1
        data = np.array([x, y, N]).T
    # Call function with arguments above
    bf.check_logspace(data, logspace, sigmoid_type)
    

def _logspace_false():    
    # Test cases for logspace is None
    logspace = False    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Define sigmoid type 
    sigmoid_type = 'weibull'
    # Call function with arguments above
    bf.check_logspace(data, logspace, sigmoid_type)


#################################################################
#  UNIT TESTS
#################################################################

def test_logspace_arg():
    raised = False
    try:
        _logspace_arg(0)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True


def test_logspace_none_branch0():
    raised = False
    try:
        _logspace_none(0)
    except:
        raised = True
    # Assert if exception flag is raised     
    assert raised is False
    
    
def test_logspace_none_branch1():
    raised = False
    try:
        _logspace_none(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_logspace_none_branch2():
    raised = False
    try:
        _logspace_none(2)
    except:
        raised = True
    # Assert if exception flag is raised     
    assert raised is False
    
    
def test_logspace_true_branch0():
    raised = False
    try:
        _logspace_true(0)
    except:
        raised = True
    # Assert if exception flag is raised     
    assert raised is False
    
    
def test_logspace_true_branch1():
    raised = False
    try:
        _logspace_true(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True


def test_logspace_false():
    raised = False
    try:
        _logspace_false()
    except:
        raised = True
    # Assert if exception flag is raised     
    assert raised is False