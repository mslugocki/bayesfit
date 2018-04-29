"""
*******************************************************
*
*  test_checkData - UNIT TEST FOR TRAVIS CI
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
from .checkData import check_data as _check_data


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _batch_false(error):    
    # Test cases for batch equal False 
    batch = False    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    # Run through possible error types
    if error == 0:
        data = np.array([x, y, N]).T
    elif error == 1:
        data = dict()
    elif error == 2:
        data = np.array([x, y]).T
    elif error == 3:
        y[0] = -0.1
        data = np.array([x, y, N]).T
    # Call function with arguments above
    _check_data(data, batch)
    # Update success flag
    success = 1
    return success 


def _batch_true(error):    
    # Test cases for batch equal False 
    batch = True    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    # Run through possible error types
    if error == 0:
        data = dict()
        data['obs1'] = np.array([x, y, N]).T
    elif error == 1:
        data = [1, 2, 3]
    elif error == 2:
        data = dict()
        data['obs1'] = np.array([x, y]).T
    elif error == 3:
        y[0] = -0.1
        data = dict()
        data['obs1'] = np.array([x, y, N]).T
    # Call function with arguments above
    _check_data(data, batch)
    # Update success flag
    success = 1
    return success 


#################################################################
#  UNIT TESTS
#################################################################

def test_batch_false_noerror():
    success = _batch_false(0)
    # Assert if exception  
    assert success == 1

def test_batch_false_error1():
    raised = False
    try:
        _batch_false(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_batch_false_error2():
    raised = False
    try:
        _batch_false(2)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_batch_false_error3():
    raised = False
    try:
        _batch_false(3)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True


def test_batch_true_noerror():
    success = _batch_true(0)
    # Assert if exception  
    assert success == 1

def test_batch_true_error1():
    raised = False
    try:
        _batch_true(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_batch_true_error2():
    raised = False
    try:
        _batch_true(2)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_batch_true_error3():
    raised = False
    try:
        _batch_true(3)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True