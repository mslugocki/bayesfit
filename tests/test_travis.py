"""
*******************************************************
*
*  TRAVIS CI SYNC TEST
*  
*  Version:      Version 2.0
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September, 2017
*  Last updated: April 28, 2018
*
*******************************************************
"""

# This file is used to test whether Travis CI is working 
# with repository. 
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5
