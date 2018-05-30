"""
*******************************************************
*
*  definePriors - DEFINE PRIORS PROVIDED BY USER TO PM MODEL
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   May 18, 2018
*  Last updated: May 29, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import pymc3 as pm
import re


#################################################################
#  FUNCTION THAT DEFINES DISTRIBUTION BASED ON CLASS
#################################################################

def _define_distribution(param_name, user_defined_distro, distro_parameters):
    
    # Define distrobution based on inputs
    if user_defined_distro == 'Unif':
        distro = pm.Uniform(param_name, 
                            upper=distro_parameters[0], 
                            lower=distro_parameters[1])
    elif user_defined_distro == 'Norm':
        distro = pm.Normal(param_name, 
                           mu=distro_parameters[0], 
                           sd=distro_parameters[1])
    elif user_defined_distro == 'Log-Norm':
        distro = pm.Lognormal(param_name, 
                              mu=distro_parameters[0], 
                              sd=distro_parameters[1])
    elif user_defined_distro == 'Beta':
        distro = pm.Beta(param_name, 
                         alpha=distro_parameters[0], 
                         beta=distro_parameters[1])
    elif user_defined_distro == 'Gamma':
        distro = pm.Gamma(param_name, 
                          mu=distro_parameters[0], 
                          sd=distro_parameters[1])
    return distro
        

#################################################################
#  CHECK LIST OF PRIORS
#################################################################

# If priors are defined, this will overide parameter estimate to use for 
# default priors if provided 
def define_priors(data, options):
    if len(options['priors']) >= 2:
        # Define alpha distribution 
        alpha = _define_distribution('alpha', 
                                     options['priors_definitions']['alpha'], 
                                     options['priors_params']['alpha'])    
        # Define beta distribution 
        beta = _define_distribution('beta', 
                                    options['priors_definitions']['beta'], 
                                    options['priors_params']['beta'])
        
    if len(options['priors']) >= 3:
        # Define gamma distribution 
        gamma = _define_distribution('gamma', 
                                     options['priors_definitions']['gamma'], 
                                     options['priors_params']['gamma'])
    else: 
        if options['param_constraints'][2] is True:
            gamma = pm.Normal('gamma',
                              mu=options['param_ests'][2], 
                              sd=0.2)
        else:
            gamma = options['param_ests'][2]

        
    if len(options['priors']) == 4:     
        # Define lambda distribution 
        lambda_ = _define_distribution('lambda', 
                                       options['priors_definitions']['lambda'], 
                                       options['priors_params']['lambda'])
    else: 
        if options['param_constraints'][3] is True:
            if data[len(data[:, 2])-1, 1] > 0.80:
                lambda_ = pm.Beta('lambda', 2, 20)
            else:
                lambda_ = pm.Beta('lambda', 1.5, 12)
        else:
            lambda_ = options['param_ests'][3]

    return alpha, beta, gamma, lambda_
