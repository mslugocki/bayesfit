"""
*******************************************************
*
*  checkOptions - CHECK USER PROVIDED ARGS FOR OPTIONS
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 14, 2018
*  Last updated: April 18, 2018
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
# Check options provided ny user, or assigned by defaults
# are valid arguments.
def check_options(options):
    if options['batch'] not in (True, False):
        raise Exception('User Error: Invalid argument provided for batch type.')
    if options['sigmoid_type'] not in ('logistic', 'gumbel', 'weibull', 'quick', 'log-quick', 'hyperbolic'):
        raise Exception('User Error: Sigmoid type specified is not one made available by the module.')
    if options['logspace'] not in (True, False):
        raise Exception('User/Internal Error: Invalid argument for log-spacing of x-values provided.')
    if options['nafc'] not in np.linspace(0, 10, 11):
        raise Warning('Warning: Value provided for nAFC is greater than 10, or less than zero!')
    if isinstance(options['threshold'], (int, float, complex)) is False:
        raise Exception('Please provide a numerical argument for proportion correct estimate of threshold.')
    if not 0 <= options['threshold'] <= 1:
        raise Warning('User Error: Value provided for threshold estimate not between zero and one!')
    if isinstance(options['nafc'], int) is False:
        raise Exception('User Error: Please provide a integer for nAFC argument.')
    if isinstance(options['n_samples'], (int, float, complex)) is False:
        raise Exception('Please provide a numerical argument for number of samples to draw.')
    if isinstance(options['chains'], (int, float, complex)) is False:
        raise Exception('User Error: Please provide a numerical argument for number of chains.')
    if isinstance(options['param_ests'], list) is False:
        raise Exception('User Error: Please provide a argument of type list for the parameter estimates of the model.')
    if isinstance(options['param_constraints'], list) is False:
        raise Exception('''User Error: Please provide a argument of type list for the 
                           parameter constraints of the model.''')
    if options['n_workers'] not in np.linspace(1, 8, 8):
        raise Warning(''''Warning: Value for number of workers provided not in range 1 - 8! 
                          Issues with sampling would likely occur.''')
