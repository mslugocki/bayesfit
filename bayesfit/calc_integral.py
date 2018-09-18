"""
*******************************************************
*
*  calc_integral - APPROXIMATE INTEGRAL OF POSTERIOR
*
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 17, 2018
*  Last updated: September 17, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np


#################################################################
#  APPROXIMATE INTEGRAL USING NUMERICAL INTEGRATION
#################################################################

def calc_integral(posterior, options, metrics):
    """Compute integral of posterior surface using numerical
    integration.

    Keyword arguments:
    posterior -- 
    options -- 
    metrics --
    """
    
    # Generate list of free parameters to integrate
    list_free = []
    for i in range(0,4):
        if options['param_free'][i] is True:
            if i == 0:
                list_free.append('scale')
            elif i ==1:
                list_free.append('slope')
            elif i ==2:
                list_free.append('gamma') 
            elif i ==2:
                list_free.append('lambda')

    # Calculate step size and mass
    list_step = []
    for key in list_free:
        if metrics['Marginals_X'][key].shape[0] > 1:
            step = (metrics['Marginals_X'][key].max() - metrics['Marginals_X'][key].min()) / (len(metrics['Marginals_X'][key]) - 1)
            list_step.append(step)
    
    # Compute mass
    mass = np.product(list_step)
    
    # COmpute Integral
    integral = np.sum(posterior * mass)
    
    return integral