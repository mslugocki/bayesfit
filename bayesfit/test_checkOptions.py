"""
*******************************************************
*
*  test_checkOptions - UNIT TEST FOR TRAVIS CI
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
from .checkOptions import check_options as _check_options


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _check_options_function(branch):    
    # Initialize options dictionary
    options = dict()
    options['batch'] = False
    options['logspace'] = False
    options['nafc'] = 2
    options['sigmoid_type'] = 'logistic'
    options['param_ests'] = [0.05, 3, 0.5, 0]
    options['param_constraints'] = [True, True, False, True]
    options['threshold'] = 0.75
    options['n_samples'] = 5000
    options['chains'] = 2
    options['n_workers'] = 1
    # Choose branch        
    if branch == 0:
        nothing = True
    elif branch == 1:
        options['batch'] = 'Raise Error'
    elif branch == 2:
        options['sigmoid_type'] = 'Raise Error'
    elif branch == 3:
        options['logspace'] = 'Raise Error'
    elif branch == 4:
        options['nafc'] = 12
    elif branch == 5:
        options['nafc'] = 'Raise Error'
    elif branch == 6:
        options['threshold'] = 'Raise Error'
    elif branch == 7:
        options['threshold'] = 1.5
    elif branch == 7:
        options['n_samples'] = 'Raise Error'
    elif branch == 8:
        options['chains'] = 'Raise Error'
    elif branch == 9:
        options['param_ests'] = dict()
    elif branch == 10:
        options['param_constraints'] = dict()
    elif branch == 11:
        options['n_workers'] = 25
    # Call function with arguments above
    _check_options(options)
    # Update success flag
    success = 1
    return success 

#################################################################
#  UNIT TESTS
#################################################################

def test_check_options_branch0():
    success = _check_options_function(0)
    # Assert if exception   
    assert success == 1

def test_check_options_branch1():
    raised = False
    try:
        _check_options_function(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch2():
    raised = False
    try:
        _check_options_function(2)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch3():
    raised = False
    try:
        _check_options_function(3)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch4():
    raised = False
    try:
        _check_options_function(4)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch5():
    raised = False
    try:
        _check_options_function(5)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch6():
    raised = False
    try:
        _check_options_function(6)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch7():
    raised = False
    try:
        _check_options_function(7)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch8():
    raised = False
    try:
        _check_options_function(8)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch9():
    raised = False
    try:
        _check_options_function(9)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch10():
    raised = False
    try:
        _check_options_function(10)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_options_branch11():
    raised = False
    try:
        _check_options_function(11)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True