"""
*******************************************************
*
*  checkLogspace - LOGSPACE INTENSITIES IF NEEDED
*
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 2017
*  Last updated: April 18, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np


#################################################################
#  CONVERT X-VALUES IN FIRST COLUMN TO LOG-SPACED VALUES
#################################################################
# Convert x-values to logspace
def convert_logspace(data):
    data[:, 0] = np.log10(data[:, 0])
    return data


#################################################################
#  CHECK WHETHER INTENSITIES NEED TO BE LOGSPACED
################################################################
# Check sigmoid type provided to convert x-values to logspace if required
def check_logspace(data, logspace, sigmoid_type):
    # Ensure argument provided for logspace is valid
    if logspace not in (None, True, False):
        raise Exception('User/Internal Error: Invalid argument for log-spacing of x-values provided.')
    # Run through options and logspace x-values if needed
    if logspace is None:
        if sigmoid_type in ('weibull', 'log-quick'):
            logspace = True
            if data[:,0].min() < 0:
                raise Exception('Cannot convert negative data points to log-spaced values!')
            # Convert x-values in data
            data = convert_logspace(data)
        else:
            logspace = False
    elif logspace is True:
        if data[:,0].min() < 0:
            raise Exception('Cannot convert negative data points to log-spaced values!')
        # Convert x-values in data
        data = convert_logspace(data)
    return data, logspace
