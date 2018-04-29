"""
*******************************************************
*
*  extractThreshold - EXTRACT THRESHOLD FROM FITTED PARAMETERS
*  
*  Version:      Version 2.0
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 18, 2018
*  Last updated: April 29, 2018
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
def get_threshold(data, metrics, options, threshold_pc):
# Extract threshold at specified level of propertion correct
    # using numerical approximation 
    def _find_nearest(y, x, value):
        idx = (np.abs(y-value)).argmin()
        return x[idx]
    
    x_est = np.linspace(data[:,0].min(), data[:,0].max(), 1e4)
    y_pred = _psyfunction(x_est, 
                          metrics['Fit'][0], 
                          metrics['Fit'][1], 
                          metrics['Fit'][2], 
                          metrics['Fit'][3], 
                          options['sigmoid_type'])
    
    threshold = _find_nearest(y_pred, x_est, threshold_pc)
        
    return threshold