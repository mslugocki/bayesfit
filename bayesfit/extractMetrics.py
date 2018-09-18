"""
*******************************************************
*
*  extractMetrics - EXTRACT RELEVANT METRICS FROM TRACE
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September, 2017
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
from .psyFunction import psyfunction


#################################################################
#  COMPUTE MARGINAL DISTRIBUTION
#################################################################

# Compute marginal posterior distributions
def _compute_marginal(post_mat, axes_sum_over): 
    """Computes marginal distribution given a
    posterior surface.
    
    Keyword arguments:
    post_mat -- posterior surface (ndarray)
    axes_sum_over -- axes over which to sum across (tuple)
    """
    marginal = np.sum(post_mat, axes_sum_over) 
    return marginal


#################################################################
#  COMPUTE STANDARD DEVIATION
#################################################################
def _std_marginal(x_values, marginal_distro, mean_marginal_distro):
    """Computes standard deviation of marginal distribution.
    
    Keyword arguments:
    x_values -- stimulus intensities (ndarray)
    marginal_distro -- marginal distribution of specified parameter (ndarray)
    mean_marginal_distro -- expectation of marginal distribution (float)
    """
    return np.sqrt(np.sum( ((x_values - mean_marginal_distro)**2)*marginal_distro))


#################################################################
#  COMPUTE DEVIANCE OF MODEL
#################################################################
def deviance(data, options, metrics, estimate_type):
    """Computes deviance metric to assess
    goodness-of-fit of model.
    
    Keyword arguments:
    data -- m x 3 numpy array
    options -- contains all options used to fit model (dictionary)
    metrics -- contain important metrics about fitted model (dictionary)
    estimate_type -- determines which metric used for parameter estimates (string)
    """
    # Determine which values to use for vector of parameters 
    param_guess = np.zeros(4)
    counter = 0
    for keys in options['param_free']:
        if keys is True:
            param_guess[counter] = metrics[estimate_type][counter]
        elif keys is False: 
            param_guess[counter] = options['param_ests'][counter]
        counter += 1
    
    # Number of trials per intensity
    n = data[:,2]
    
    # Number of correct responses per intensity
    y = data[:,1]
    
    # First generate predictions based on user defined 
    # point estiamtes of function
    p = psyfunction(data[:,0], 
                      param_guess[0],
                      param_guess[1],
                      param_guess[2],
                      param_guess[3],
                      options['sigmoid_type'])
    p = np.rint(p*n)
    
    # Compute deviance measure for binomial model
    Deviance = 2*np.sum(n*y*np.log(y/p) + n*(1-y)*np.log((1-y)/(1-p)))
    
    return Deviance


#################################################################
#  COMPUTE PEARSON'S CHI SQUARED
#################################################################
def pearson_chisqr(data, options, metrics, estimate_type):
    """Computes Pearson's Chi-squared to assess
    goodness-of-fit of model.
    
    Keyword arguments:
    data -- m x 3 numpy array
    options -- contains all options used to fit model (dictionary)
    metrics -- contain important metrics about fitted model (dictionary)
    estimate_type -- determines which metric used for parameter estimates (string)
    """
    # Determine which values to use for vector of parameters 
    param_guess = np.zeros(4)
    counter = 0
    for keys in options['param_free']:
        if keys is True:
            param_guess[counter] = metrics[estimate_type][counter]
        elif keys is False: 
            param_guess[counter] = options['param_ests'][counter]
        counter += 1
    
    # Number of trials per intensity
    n = data[:,2]
    
    # Number of correct responses per intensity
    y = data[:,1]
    
    # First generate predictions based on user defined 
    # point estiamtes of function
    p = psyfunction(data[:,0], 
                      param_guess[0],
                      param_guess[1],
                      param_guess[2],
                      param_guess[3],
                      options['sigmoid_type'])
    p = np.rint(p*n)
    
    # Compute Pearson's Chi Squared 
    p_chisqr = np.sum(((y-p)**2)/p)
    
    return p_chisqr
    
    
#################################################################
#  COMPUTE HIGHEST POSTERIOR DENSITY INTERVAL
#################################################################

def hpdi(marginal, marginal_labels, alpha):
    """Computes Highest Posterior Density Interval (HPDI)
    for a marginal distribution given a specified level
    of confidence.
    
    Keyword arguments:
    marginal -- marginal distribution to compute bci (ndarray)
    marginal_labels -- values over which marginal was computed (ndarray)
    alpha -- confidence interval (float)
    """
    # Calculate credible mass
    cred_mass = 1 - alpha
    
    # Sort marginal distribution
    # Sort marginal and extract indices
    sort_idx = np.argsort(marginal)
    # Sort marginal vector itself
    sort_marg = np.sort(marginal)[::-1]
    # Label Idxs as binary 
    binary_idx = np.where(np.cumsum(sort_marg) <= cred_mass)

    # Label points that are part of highest posterior interval
    hpdi = marginal_labels[sort_idx[binary_idx]]
    
    # Calculate cutoff probability
    # i.e., above this probability, all points are part of hpdi
    hpdi_px = sort_marg[binary_idx].min()

    return hpdi_px, hpdi


#################################################################
#  COMPUTE BAYESIAN CREDIBLE INTERVAL
#################################################################

# Compute Bayesian Credible Interval   
def bci(marginal, alpha):
    """Computes Bayesian Credible Interval (BCI) for
    a marginal distribution given a specified level
    of confidence.
    
    Keyword arguments:
    marginal -- marginal distribution to compute bci (ndarray)
    alpha -- confidence interval (float)
    """
    # Compute cumulative sum of marginal distribution
    cpxx = np.cumsum(marginal) 
    
    # Boundary
    bound = (1-alpha)/2
    # Lower boundary 
    lower = marginal[np.where(cpxx >= 0 + bound)][0]   
    # Upper boundary
    upper = marginal[np.where(cpxx >= 1 - bound)][0]   
    
    return lower, upper 


#################################################################
#  EXTRACT RELEVANT PARAMETERS FROM POSTERIOR GRID
#################################################################
# Extract fitted parameters and other metrics 
# of importance from posterior grid
def extract_metrics_grid(data, options, metrics, posterior, grid):
    """Computes relevant metrics from fitted model.
    
    Keyword arguments:
    data -- m x 3 numpy array
    options -- contains all options used to fit model (dictionary)
    metrics -- contain important metrics about fitted model (dictionary)
    posterior -- posterior surface (ndarray)
    grid -- grid of values over which likelihood was computed over (ndarray) 
    """
    
    #################################################################
    #  COMPUTE MARGINAL POSTERIOR DISTRIBUTIONS
    #################################################################
    
    # Compute marginal posterior distributions
    metrics['Marginals'] = dict()
    metrics['Marginals']['scale'] = _compute_marginal(posterior, (1,2,3))
    metrics['Marginals']['slope'] = _compute_marginal(posterior, (0,2,3))
    metrics['Marginals']['gamma'] = _compute_marginal(posterior, (0,1,3))
    metrics['Marginals']['lambda'] = _compute_marginal(posterior, (0,1,2))
    
    #################################################################
    #  GET MAP ESTIMATE FROM POSTERIOR 
    #################################################################
    
    # Get index of MAP estimate
    map_index = np.where(posterior == np.max(posterior.ravel()))
    
    # Form vector for MAP estimate of each parameter if free parameter
    metrics['MAP'] = np.zeros(4)
    for i in range(0,4):
        if options['param_free'][i] is True:
            if i == 0:
                metrics['MAP'][i] = grid['A'][map_index]
            elif i == 1: 
                metrics['MAP'][i] = grid['B'][map_index]
            elif i == 2: 
                metrics['MAP'][i] = grid['G'][map_index]   
            elif i == 3: 
                metrics['MAP'][i] = grid['L'][map_index]
        elif options['param_free'][i] is False:
            metrics['MAP'][i] = np.nan
    
    #################################################################
    #  GET MEAN ESTIMATE FROM MARGINALS 
    #################################################################
    
    # Form vector for MAP estimate of each parameter if free parameter
    metrics['Mean'] = np.zeros(4)
    for i in range(0,4):
        if options['param_free'][i] is True:
            if i == 0:
                metrics['Mean'][i] = np.sum(metrics['Marginals']['scale']*grid['scale']) 
            elif i == 1:                 
                metrics['Mean'][i] = np.sum(metrics['Marginals']['slope']*grid['slope']) 
            elif i == 2:                 
                metrics['Mean'][i] = np.sum(metrics['Marginals']['gamma']*grid['gamma']) 
            elif i == 3:                 
                metrics['Mean'][i] = np.sum(metrics['Marginals']['lambda']*grid['lambda']) 
        elif options['param_free'][i] is False:
            metrics['Mean'][i] = np.nan
    
    #################################################################
    #  CALCULATE SD FOR EACH PARAMETER
    #################################################################
    
    # Form vector for MAP estimate of each parameter if free parameter
    metrics['SD'] = np.zeros(4)
    for i in range(0,4):
        if options['param_free'][i] is True:
            if i == 0:
                metrics['SD'][i] = _std_marginal(grid['scale'], 
                                                   metrics['Marginals']['scale'], 
                                                   metrics['Mean'][0])
            elif i == 1:                 
                metrics['SD'][i] = _std_marginal(grid['slope'], 
                                                   metrics['Marginals']['slope'], 
                                                   metrics['Mean'][1])
            elif i == 2:                 
                metrics['SD'][i] = _std_marginal(grid['gamma'], 
                                                   metrics['Marginals']['gamma'], 
                                                   metrics['Mean'][2])
            elif i == 3:                 
                metrics['SD'][i] = _std_marginal(grid['lambda'], 
                                                   metrics['Marginals']['lambda'], 
                                                   metrics['Mean'][3])
        elif options['param_free'][i] is False:
            metrics['SD'][i] = np.nan

    #################################################################
    #  CALCULATE BOUNDS FOR HIGHEST POSTERIOR DENSITY
    #################################################################
    
    # Form vector for MAP estimate of each parameter if free parameter
    metrics['BCI'] = np.zeros(shape=(2,4))
    for i in range(0,4):
        if options['param_free'][i] is True:
            if i == 0:
                metrics['BCI'][0,i], metrics['BCI'][1,i] = bci(metrics['Marginals']['scale'], 0.05)
            elif i == 1:                 
                metrics['BCI'][0,i], metrics['BCI'][1,i] = bci(metrics['Marginals']['slope'], 0.05)
            elif i == 2:                 
                metrics['BCI'][0,i], metrics['BCI'][1,i] = bci(metrics['Marginals']['gamma'], 0.05)
            elif i == 3:                 
                metrics['BCI'][0,i], metrics['BCI'][1,i] = bci(metrics['Marginals']['lambda'], 0.05)
        elif options['param_free'][i] is False:
            metrics['BCI'][0,i] = np.nan
            metrics['BCI'][1,i] = np.nan
            
    #################################################################
    #  CALCULATE DEVIANCE
    #################################################################
    metrics['deviance'] = deviance(data, options, metrics, 'MAP')
    
    #################################################################
    #  CALCULATE DEVIANCE
    #################################################################
    metrics['pearsons_chisqr'] = pearson_chisqr(data, options, metrics, 'MAP')
    
    return metrics
