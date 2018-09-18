"""
*******************************************************
*
*  get_Threshold - EXTRACT THRESHOLD FROM FITTED PARAMETERS
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 18, 2018
*  Last updated: September 12, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
from .psyFunction import psyfunction as _psyfunction


#################################################################
#  EXTRACT THRESHOLD FROM FITTED PARAMETERS
#################################################################
def get_threshold(data, options, metrics, threshold_pc, estimate_type = 'MAP'):
    """Check options provided ny user, or assigned by defaults
    are valid arguments.
    
    Keyword arguments:
    data -- m x 3 numpy array
    metrics -- contain important metrics about fitted model (dictionary)
    options -- contains all options used to fit model (dictionary)
    threshold_pc -- proportion correct to define threshold (float)
    estimate_type -- determines which metric to use for parameters of model (string)
    """
    # Extract threshold at specified level of propertion correct
    # using numerical approximation 
    def _find_nearest(y, x, value):
        idx = (np.abs(y-value)).argmin()
        return x[idx]
    
    x_est = np.linspace(data[:, 0].min(), data[:, 0].max(), 1e4)
    
    if estimate_type not in ('MAP', 'Mean'):
        raise ValueError('Please provide appropriate argument for estimate type (e.g., MAP, Mean)')
        
    # Determine which values to use for vector of parameters 
    param_guess = np.zeros(4)
    counter = 0
    for keys in options['param_free']:
        if keys is True:
            param_guess[counter] = metrics[estimate_type][counter]
        elif keys is False: 
            param_guess[counter] = options['param_ests'][counter]
        counter += 1
    
    y_pred = _psyfunction(x_est, 
                          param_guess[0],
                          param_guess[1],
                          param_guess[2],
                          param_guess[3],
                          options['sigmoid_type'])
    
    threshold = _find_nearest(y_pred, x_est, threshold_pc)
        
    return threshold
