"""
*******************************************************
*
*  checkOptions - CHECK USER PROVIDED ARGS FOR OPTIONS
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 14, 2018
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np


#################################################################
#  CHECK OPTIONS PROVIDED
#################################################################
def check_options(options):
    """Check options provided ny user, or assigned by defaults
    are valid arguments.
    
    Keyword arguments:
    options -- contains all options used to fit model (dictionary)
    """
    if options['batch'] not in (True, False):
        raise ValueError('User Error: Invalid argument provided for batch type.')
    if options['sigmoid_type'] not in ('norm', 'logistic', 'gumbel', 'weibull', 'quick', 'log-quick', 'hyperbolic'):
        raise ValueError('User Error: Sigmoid type specified is not one made available by the module.')
    if options['logspace'] not in (True, False):
        raise ValueError('User/Internal Error: Invalid argument for log-spacing of x-values provided.')
    if options['nafc'] not in (1,2,3,4,5,6,7,8,9,10):
        raise ValueError('Warning: Value provided for nAFC is greater than 10, or less than zero!')
    if isinstance(options['threshold'], (int, float, complex)) is False:
        raise ValueError('Please provide a numerical argument for proportion correct estimate of threshold.')
    if not 0 <= options['threshold'] <= 1:
        raise ValueError('User Error: Value provided for threshold estimate not between zero and one!')
    if isinstance(options['nafc'], int) is False:
        raise ValueError('User Error: Please provide a integer for nAFC argument.')
    if isinstance(options['param_ests'], list) is False:
        raise ValueError('User Error: Please provide a argument of type list for the parameter estimates of the model.')
    if isinstance(options['param_free'], list) is False:
        raise ValueError('''User Error: Please provide a argument of type list for the 
                           parameter constraints of the model.''')
    if isinstance(options['density'], int) is False:
        raise ValueError('User Error: Please provide a integer for density of grid.')