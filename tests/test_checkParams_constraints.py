"""
*******************************************************
*
*  test_checkParams_constraints - UNIT TEST FOR TRAVIS CI
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

def _check_constraints_none():    
    # Test cases for param_constraints is None
    param_constraints = None
    # Call function with arguments above
    bf.check_constraints(param_constraints)
    
    
def _check_constraints_not_none(branch):    
    if branch == 0:
        # Test cases for param_constraints
        param_constraints = dict()
    elif branch == 1:
        # Test cases for param_constraints
        param_constraints = ['Raise', 'Exception']
    elif branch == 2:
        # Test cases for param_constraints
        param_constraints = [True]
    elif branch == 3:
        # Test cases for param_constraints
        param_constraints = [True, True]
    elif branch == 4:
        # Test cases for param_constraints
        param_constraints = [True, True, False]
    elif branch == 5:
        # Test cases for param_constraints
        param_constraints = [True, True, False, True]
    elif branch == 6:
        # Test cases for param_constraints
        param_constraints = [True, True, False, True, False]
    # Call function with arguments above
    bf.check_constraints(param_constraints)   


#################################################################
#  UNIT TESTS
#################################################################

def test_check_params_none():
    raised = False
    try:
        _check_params_none(0)
    except:
        raised = True
    # Assert if exception flag is raised     
    assert raised is False
    

def test_check_params_not_none_branch0():
    raised = False
    try:
        _check_constraints_not_none(0)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_params_not_none_branch1():
    raised = False
    try:
        _check_constraints_not_none(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_params_not_none_branch2():
    raised = False
    try:
        _check_constraints_not_none(2)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_params_not_none_branch3():
    raised = False
    try:
        _check_constraints_not_none(3)
    except:
        raised = True
    # Assert if exception flag is raised     
    assert raised is False
    
def test_check_params_not_none_branch4():
    raised = False
    try:
        _check_constraints_not_none(4)
    except:
        raised = True
    # Assert if exception flag is raised     
    assert raised is False
    
def test_check_params_not_none_branch5():
    raised = False
    try:
        _check_constraints_not_none(5)
    except:
        raised = True
    # Assert if exception flag is raised     
    assert raised is False
    
def test_check_params_not_none_branch6():
    raised = False
    try:
        _check_constraints_not_none(6)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True