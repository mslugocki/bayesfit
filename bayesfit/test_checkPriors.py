"""
*******************************************************
*
*  test_check_priors - UNIT TEST FOR TRAVIS WITH CHECK PRIORS
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
from .checkPriors import check_priors as _check_priors


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _check_assigned_priors(branch):
    # Choose branch that defines sigmoid fit   
    if branch == 0:
        priors = ['Raise(0.5, 2)', 'Error(3,0.5)'] 
    elif branch == 1:
        priors = ['Norm(10150, 2)', 'Beta(3,0.5)']      
    # Check priors
    options = dict()
    options['priors'] = priors
    options = _extract_priors(options)
    _check_priors(options)
    # Update success flag
    success = 1
    return success


#################################################################
#  UNIT TESTS
#################################################################

def test_check_priors_branch0():
    raised = False
    try:
        _check_assigned_priors(0)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True

def test_check_priors_branch1():
    raised = False
    try:
        _check_assigned_priors(1)
    except:
        raised = True
    # Assert if exception flag is not raised     
    assert raised is True
