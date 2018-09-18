"""
*******************************************************
*
*  genGrid - GENERATE GRID FOR PRIORS AND POSTERIOR 
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   August 31, 2018
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import scipy.stats as st


#################################################################
#  GENERATE GRID OF VALUES BASED ON FREE PARAMETERS TO ESTIMATE
#################################################################

def gen_grid(data, options):
    """Generates grid of values over which to compute the likelihood
    for each parameter to be estimated.
    
    Keyword arguments:
    data -- m x 3 numpy array
    options -- contains all options used to fit model (dictionary)
    """
    # Determine grid spacing and assignment for each parameter
    # Scale (typically alpha)
    if options['param_free'][0] is True:
        scale = np.linspace(data[:,0].min(), data[:,0].max(), options['density'])
    else:
        scale = options['param_ests'][0]
    
    # Slope (typically beta)
    if options['param_free'][1] is True:
        slope = np.linspace(options['param_ests'][1]*0.5, options['param_ests'][1]*1.5, options['density'])
    else: 
        slope = options['param_ests'][1]
    
    # Gamma (Guess rate)
    if options['param_free'][2] is True:
        lower_bound_gamma = options['param_ests'][2] - 0.25
        if lower_bound_gamma < 0:
            lower_bound_gamma = 0.0001
        upper_bound_gamma = options['param_ests'][2] + 0.25
        if upper_bound_gamma > 1:
            upper_bound_gamma = 0.9999
        gamma = np.linspace(lower_bound_gamma, upper_bound_gamma, options['density'])
    else:
        gamma = options['param_ests'][2]
        
    # Lambda (Lapse rate)
    if options['param_free'][3] is True:
        lambda_ = np.linspace(0.0001, 0.50, options['density'])
    else:
        lambda_ = options['param_ests'][3]

    # Determine meshgrid for posterior
    grid = dict()
    grid['A'], grid['B'], grid['G'], grid['L'] = np.meshgrid(scale, slope, gamma, lambda_)    
    
    # Save variables for defining and applying priors
    grid['scale'] = scale
    grid['slope'] = slope
    grid['gamma'] = gamma
    grid['lambda'] = lambda_
    
    # Output ditionary with grid
    return grid
