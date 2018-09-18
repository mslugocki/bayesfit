"""
*******************************************************
*
*  test_checkParams - UNIT TEST FOR TRAVIS CI
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
from .checkParams import check_params as _check_params


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _check_params_none(branch):    
    # Test cases for param_ests is None
    param_ests = None
    # Generate dataset 
    data01 = np.array([[0.0010,   45.0000,   90.0000],
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
    # Define nafc
    nafc = 2
    # Choose branch 
    if branch == 0:
        batch = False
        data = data01
    elif branch == 1:
        batch = True
        data = dict()
        data['data01'] = data01
    # Call function with arguments above
    _check_params(data, param_ests, nafc, batch, 'weibull')
    # Update success flag
    success = 1
    return success 

def _check_params_not_none(branch):    
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
    # Define nafc
    nafc = 2
    # Define batch
    batch = False
    # Choose branch 
    if branch == 0:
        # Set param_ests to trigger event
        param_ests = dict()
    elif branch == 1:
        # Set param_ests to trigger event
        param_ests = ['Trigger', 'Event']
    elif branch == 2:
        # Set param_ests to trigger event
        param_ests = [0.005]
    elif branch == 3:
        # Set param_ests vector with full length
        param_ests = [0.005, 2, None, 0]
    elif branch == 4:
        # Set param_ests to go through different number of args (trigger error)
        param_ests = [0.005, 2, 0.5, 0, 0.09]
    # Call function with arguments above
    _check_params(data, param_ests, nafc, batch, 'weibull')
    # Update success flag
    success = 1
    return success 

#################################################################
#  UNIT TESTS
#################################################################

def test_check_params_none_branch0():
    success = _check_params_none(0)
    # Assert if exception   
    assert success == 1

def test_check_params_none_branch1():
    success = _check_params_none(1)
    # Assert if exception   
    assert success == 1

def test_check_params_not_none_branch0():
    raised = False
    try:
        _check_params_not_none(0)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_check_params_not_none_branch1():
    raised = False
    try:
        _check_params_not_none(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_params_not_none_branch2():
    raised = False
    try:
        _check_params_not_none(2)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_params_not_none_branch3():
    success = _check_params_not_none(3)
    # Assert if exception   
    assert success == 1
    
def test_check_params_not_none_branch4():
    raised = False
    try:
        _check_params_not_none(6)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
