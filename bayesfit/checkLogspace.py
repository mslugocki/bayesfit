"""
*******************************************************
*
*  checkLogspace - LOGSPACE INTENSITIES IF NEEDED
*
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 2017
*  Last updated: September 13, 2018
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
    """Log-transforms stimulus intensities.

    Keyword arguments:
    data -- m x 3 numpy array
    """
    data_x_logtrans = np.log10(data[:, 0])
    data_trans = np.array([data_x_logtrans, data[:,1], data[:,2]]).T
    return data_trans


#################################################################
#  CHECK WHETHER INTENSITIES NEED TO BE LOGSPACED
################################################################
# Check sigmoid type provided to convert x-values to logspace if required
def check_logspace(data, logspace, sigmoid_type, batch):
    """Performs a check of whether data need to be logspaced
    based on user input via logspace option and sigmoid type
    chosen (i.e, Weibull).

    Keyword arguments:
    data -- m x 3 numpy array
    logspace -- specifies whether to logspace data (logical)
    sigmoid_type -- sigmoid type fit to data (string)
    """
    data_copy = data
    # Ensure argument provided for logspace is valid
    if logspace not in (None, True, False):
        raise Exception('User/Internal Error: Invalid argument for log-spacing of x-values provided.')
    # Run through options and logspace x-values if needed
    if logspace is None:
        if sigmoid_type in ('weibull', 'log-quick'):
            if batch is False:
                logspace = True
                if data[:, 0].min() < 0:
                    raise Exception('Cannot convert negative data points to log-spaced values!')
                # Convert x-values in data
                data_copy = convert_logspace(data)
            elif batch is True:
                logspace = True
                for keys in data:
                    if data[keys][:, 0].min() < 0:
                        raise Exception('Cannot convert negative data points to log-spaced values!')
                    # Convert x-values in data
                    data_copy[keys] = convert_logspace(data[keys])
        else:
            logspace = False
            data_copy = data
    elif logspace is True:
        if batch is False:
            logspace = True
            if data[:, 0].min() < 0:
                raise Exception('Cannot convert negative data points to log-spaced values!')
            # Convert x-values in data
            data_copy = convert_logspace(data)
        elif batch is True:
            logspace = True
            for keys in data:
                if data[keys][:, 0].min() < 0:
                    raise Exception('Cannot convert negative data points to log-spaced values!')
                # Convert x-values in data
                data_copy[keys] = convert_logspace(data[keys])
    elif logspace is False:
        data_copy = data
    return data_copy, logspace
