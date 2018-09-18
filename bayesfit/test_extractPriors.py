"""
*******************************************************
*
*  test_extract_priors - UNIT TEST FOR TRAVIS WITH EXTRACT PRIORS
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   May 29, 2018
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES 
#################################################################
import numpy as np
from .extractPriors import extract_priors as _extract_priors


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _check_extract_priors(branch):    
    # Choose branch that defines sigmoid fit   
    if branch == 0:
        priors = ['Norm(0.5,2)']
    elif branch == 1:
        priors = ['Norm(0.5,2)', 'Beta(3,0.5)', 'Beta(3,0.5)', 'Beta(3,0.5)', 'Beta(3,0.5)']      
    elif branch == 2:
        priors = ['Norm(0.5,2)', 'Beta(3,0.5)', 'Norm(0.5,2)', 7]
    elif branch == 3:
        priors = ['Norm(0.5,2)', 'Beta(3,0.5)', 'Norm(0.5,2)', 'Beta(2,20)']
    # Use BayesFit to fit function
    options = dict()
    options['priors'] = priors
    _extract_priors(options)
    # Update success flag
    success = 1
    return success 


#################################################################
#  UNIT TESTS
#################################################################

def test_check_extract_priors_branch0():
    raised = False
    try:
        _check_extract_priors(0)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_check_extract_priors_branch1():
    raised = False
    try:
        _check_extract_priors(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
    
def test_check_extract_priors_branch2():
    raised = False
    try:
        _check_extract_priors(2)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
def test_check_extract_priors_branch3():
    success = _check_extract_priors(3)
    # Assert if exception  
    assert success == 1
