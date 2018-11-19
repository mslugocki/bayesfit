"""
*******************************************************
*
*  applyPriors - APPLY PRIORS TO LIKELIHOOD SURFACE TO FORM POSTERIOR
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 3, 2018
*  Last updated: November 19, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import scipy.stats as st


#################################################################
#  FUNCTION THAT DEFINES DISTRIBUTION BASED ON CLASS
#################################################################
def _define_distribution(xx, user_defined_distro, distro_parameters):
    """Assigns probability density to parameters defined by grid
    and specified distribution.

    Keyword arguments:
    xx -- range of values over which to define distribution (ndarray)
    user_defined_distro -- name of distribution (string)
    distro_parameters -- parameters for distribution (list)
    """
    # Define distrobution based on inputs
    if user_defined_distro == 'Unif':
        distro = st.uniform.pdf(xx,
                                distro_parameters[0],
                                distro_parameters[1])
    elif user_defined_distro == 'Norm':
        distro = st.norm.pdf(xx,
                             distro_parameters[0],
                             distro_parameters[1])
    elif user_defined_distro == 'Log-Norm':
        distro = st.lognorm.pdf(xx,
                                distro_parameters[0],
                                distro_parameters[1])
    elif user_defined_distro == 'Beta':
        distro = st.beta.pdf(xx,
                             distro_parameters[0],
                             distro_parameters[1])
    elif user_defined_distro == 'Gamma':
        distro = st.gamma.pdf(xx,
                              distro_parameters[0],
                              distro_parameters[1])

    # Check whether vector or probabilities returns non-zero sum
    if distro.sum() == 0.0:
        raise ValueError('''Error applying priors: A vector representing
            the prior probabilities along the distribution for one of the
            parameters you have specified sums to zero. This suggests one of
            the prior distributions provided are not within the range of, or
            far off from those regions where the best estimated value
            likely exists.
            \n
            Please adjust the priors provided to capture regions where
            value estimates are more probable, or set priors to
            None to obtain use MLE.''')
    else:
        # Ensure distribution sums to one
        distro /= distro.sum()

    return distro


#################################################################
#  APPLY PRIORS
#################################################################
def apply_priors(data, options, posterior, grid):
    """Applies prior to likelihood surface resulting in
    use of Bayesian inference to produce posterior surface.

    Keyword arguments:
    data -- m x 3 numpy array
    options -- contains all options used to fit model (dictionary)
    posterior -- posterior surface (ndarray)
    grid -- grid of values over which likelihood was computed over (ndarray)
    """
    # Apply prior for scale
    if 'scale' in options['priors_params'].keys():
        prior_scale = _define_distribution(grid['scale'], 
                                               options['priors_definitions']['scale'],
                                               options['priors_params']['scale'])
                
        # Log transform to prevent underflow 
        prior_scale = np.log(prior_scale)
        
        # Reshape to ensure broadcast works correctly
        prior_scale = prior_scale.reshape((-1,1,1,1))
        
        # Compute new posterior based on priors
        posterior = posterior + prior_scale
        
    # Apply prior for slope 
    if 'slope' in options['priors_params'].keys():
        prior_slope = _define_distribution(grid['slope'], 
                                              options['priors_definitions']['slope'],
                                              options['priors_params']['slope'])
        
        prior_slope = np.log(prior_slope)
        prior_slope = prior_slope.reshape((1,-1,1,1))
        posterior = posterior + prior_slope

    # Apply prior for gamma 
    if 'gamma' in options['priors_params'].keys():
        prior_gamma = _define_distribution(grid['gamma'], 
                                           options['priors_definitions']['gamma'],
                                           options['priors_params']['gamma'])

        prior_gamma = np.log(prior_gamma)
        prior_gamma = prior_gamma.reshape((1,1,-1,1))
        posterior = posterior + prior_gamma

    # Apply prior for lambda
    if 'lambda' in options['priors_params'].keys():
        prior_lambda = _define_distribution(grid['lambda'], 
                                            options['priors_definitions']['lambda'],
                                            options['priors_params']['lambda'])
    
        prior_lambda = np.log(prior_lambda)
        prior_lambda = prior_lambda.reshape((1,1,1,-1))
        posterior = posterior + prior_lambda
    
    return posterior