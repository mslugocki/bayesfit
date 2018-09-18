"""
*******************************************************
*
*  test_checkLogspace - UNIT TEST FOR TRAVIS CI
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 28, 2017
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES 
#################################################################
import numpy as np
from .checkLogspace import check_logspace as _check_logspace


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _logspace_arg():    
    # Test cases for logspace is None
    logspace = 'Not an options'    
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
    # Define sigmoid type 
    sigmoid_type = 'weibull'
    # Call function with arguments above
    _check_logspace(data, logspace, sigmoid_type, batch = False)
    # Update success flag
    success = 1
    return success 

def _logspace_none(branch):    
    # Test cases for logspace is None
    logspace = None    
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
    # Run through possible error types
    if branch == 0:
        # Define sigmoid type 
        sigmoid_type = 'weibull'
    elif branch == 1:
        # Define sigmoid type 
        sigmoid_type = 'weibull'
        # Add negative number to raise exception
        data[0,0] = -0.1
    elif branch == 2:
        # Define sigmoid type 
        sigmoid_type = 'logistic'
    # Call function with arguments above
    _check_logspace(data, logspace, sigmoid_type, batch = False)
    # Update success flag
    success = 1
    return success 

def _logspace_true(branch):    
    # Test cases for logspace is None
    logspace = True    
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
    # Run through possible error types
    if branch == 0:
        # Define sigmoid type 
        sigmoid_type = 'weibull'
    elif branch == 1:
        # Define sigmoid type 
        sigmoid_type = 'weibull'
        # Add negative number to raise exception
        data[0,0] = -0.1
    # Call function with arguments above
    _check_logspace(data, logspace, sigmoid_type, batch = False)
    # Update success flag
    success = 1
    return success    

def _logspace_false():    
    # Test cases for logspace is None
    logspace = False    
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
    # Define sigmoid type 
    sigmoid_type = 'weibull'
    # Call function with arguments above
    _check_logspace(data, logspace, sigmoid_type, batch = False)
    # Update success flag
    success = 1
    return success 

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
    success = _logspace_none(0)
    # Assert if exception  
    assert success == 1
    
    
def test_logspace_none_branch1():
    raised = False
    try:
        _logspace_none(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_logspace_none_branch2():
    success = _logspace_none(2)
    # Assert if exception  
    assert success == 1
    
    
def test_logspace_true_branch0():
    success = _logspace_true(0)
    # Assert if exception  
    assert success == 1
    
    
def test_logspace_true_branch1():
    raised = False
    try:
        _logspace_true(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True


def test_logspace_false():
    success = _logspace_false()
    # Assert if exception  
    assert success == 1
