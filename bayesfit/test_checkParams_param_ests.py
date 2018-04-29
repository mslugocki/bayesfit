"""
*******************************************************
*
*  test_checkParams - UNIT TEST FOR TRAVIS CI
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
from .checkParams import check_params as _check_params


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _check_params_none(branch):    
    # Test cases for param_ests is None
    param_ests = None
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
    # Define nafc
    nafc = 2
    # Choose branch 
    if branch == 0:
        batch = False
    elif branch == 1:
        batch = True
    # Call function with arguments above
    _check_params(data, param_ests, nafc, batch)
    # Update success flag
    success = 1
    return success 

def _check_params_not_none(branch):    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    data = np.array([x, y, N]).T
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
        param_ests = [0.5]
    elif branch == 3:
        # Set param_ests to go through different number of args
        param_ests = [0.05, 2]
    elif branch == 4:
        # Set param_ests to go through different number of args
        param_ests = [0.05, 2, 0.5]
    elif branch == 5:
        # Set param_ests to go through different number of args
        param_ests = [0.05, 2, 0.5, 0]
    elif branch == 6:
        # Set param_ests to go through different number of args (trigger error)
        param_ests = [0.05, 2, 0.5, 0, 0.09]
    # Call function with arguments above
    _check_params(data, param_ests, nafc, batch)
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
    success = _check_params_not_none(4)
    # Assert if exception   
    assert success == 1
    
def test_check_params_not_none_branch5():
    success = _check_params_not_none(5)
    # Assert if exception   
    assert success == 1
    
def test_check_params_not_none_branch6():
    raised = False
    try:
        _check_params_not_none(6)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True