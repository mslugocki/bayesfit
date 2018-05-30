"""
*******************************************************
*
*  checkPriors - CHECK PRIORS PROVIDED BY USER 
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   May 19, 2018
*  Last updated: May 19, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np


#################################################################
#  CHECK PRIORS PROVIDED
#################################################################

# Function to check that priors provided by the user are valid 
def check_priors(options): 
    # Check whether distribution types provided are valid
    for keys in options['priors_definitions']:
        if options['priors_definitions'][keys] not in ('Unif', 'Norm', 'Log-Norm', 'Beta', 'Gamma'): 
            raise Exception('''One of the prior distributions defined is not 
                            a valid argument from options available!''')
    # Check whether parameters for distributions within acceptable bounds
    # Note: Does NOT check whether parameters for each distribution are valid.
    for values in options['priors_params']:
        for i in range(0,len(options['priors_params'][values])):
            if options['priors_params'][values][i] > 10000 or options['priors_params'][values][i] < -10000:
                    raise Exception('''One of the parameters that define a prior
                    distribution is greater than 10000 or less than -10000!''')