"""
*******************************************************
*
*  gridLikelihood - COMPUTES LIKELIHOOD USING GRID EVALUATION
*
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 3, 2018
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
from .psyFunction import psyfunction as _psyfunction


#################################################################
#  COMPUTE LIKELIHOOD USING GRID EVALUATION
#################################################################

def grid_likelihood(data, options, grid):
    """Computes likelihood across of parameters defined by grid
    given the data. 
    
    Keyword arguments:
    data -- m x 3 numpy array
    options -- contains all options used to fit model (dictionary)
    grid -- grid of values over which to compute likelihood over (ndarray) 
    """
    # Initialize posterior
    likelihood = np.zeros(shape = grid['A'].shape)
    
    # Compute likelihood
    for i in range(0,len(data[:,0])):
        y = _psyfunction(data[i,0], 
                         grid['A'], 
                         grid['B'], 
                         grid['G'], 
                         grid['L'], 
                         options['sigmoid_type'])*.99 + 0.005
                         
        likelihood += data[i,1]*np.log(y) + (data[i,2] - data[i,1])*np.log(1-y)
        
    return likelihood
