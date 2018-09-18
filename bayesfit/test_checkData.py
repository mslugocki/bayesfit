"""
*******************************************************
*
*  test_checkData - UNIT TEST FOR TRAVIS CI
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
from .checkData import check_data as _check_data


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _batch_false(error):    
    # Test cases for batch equal False 
    batch = False    
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
    if error == 0:
        data = data
    elif error == 1:
        data = dict()
    elif error == 2:
        data = data[:,1:2]
    elif error == 3:
        data[0,2] = 0 
    # Call function with arguments above
    _check_data(data, batch)
    # Update success flag
    success = 1
    return success 


def _batch_true(error):    
    # Test cases for batch equal False 
    batch = True    
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
    # Run through possible error types
    if error == 0:
        data = dict()
        data['obs1'] = data_batch
    elif error == 1:
        data = list()
    elif error == 2:
        data = dict()
        data['obs1'] = data_batch[:,1:2]
    elif error == 3:
        data = dict()
        data['obs1'] = data_batch
        data['obs1'][0,2] = 0
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
