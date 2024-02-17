"""
*******************************************************
*
*  BayesFit - CORE FILE
*  
*  Version:      Version 2.4
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September, 2017
*  Last updated: February 11, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES 
#################################################################
# Core modules 
import numpy as np
import re
import os 
import warnings
import matplotlib
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore", UserWarning)
    if os.environ.get('DISPLAY', '') == '':
       print('no display found. Using non-interactive Agg backend')
       matplotlib.use('Agg')
# Functions designed to check ser input
from .checkData import check_data as _check_data
from .checkLogspace import check_logspace as _check_logspace
from .checkParams import check_params as _check_params
from .checkParams import check_constraints as _check_constraints
from .checkOptions import check_options as _check_options 
from .checkPriors import check_priors as _check_priors
from .extractPriors import extract_priors as _extract_priors
# Core functions for computing likelihood/posterior
from .psyFunction import psyfunction as _psyfunction
from .genGrid import gen_grid as _gen_grid
from .gridLikelihood import grid_likelihood as _grid_likelihood
from .applyPriors import apply_priors as _apply_priors
from .calc_integral import calc_integral as _calc_integral
# Functions for extracting relevant metrics from posterior
from .extractMetrics import extract_metrics_grid as _extract_metrics_grid 
from .get_Threshold import get_threshold
# Plotting functions
from .plot_psyFcn import plot_psyfcn
from .plot_Posterior import plot_posterior
from .plot_Marginals import plot_marginals
from .plot_Priors import plot_priors


#################################################################
#  BAYESFIT CORE FUNCTION THAT ACCEPTS ARGUMENTS FROM USE 
#################################################################
def fitmodel(data,
             batch=False,
             logspace=None,
             nafc=2,
             sigmoid_type='logistic',
             param_ests=None,
             param_free=None,
             priors=None,
             threshold=0.75,
             density=100,
             ):
    """Main function used to fit psychometric functions 
    to data provided by the user.
    
    Keyword arguments:
    data -- m x 3 numpy array
    batch -- specifies whether batch fitting data (logical)
    logspace -- specifies whether to logspace data (logical)
    nafc -- N-alternative forced choice experiment (integer)
    sigmoid_type -- sigmoid type fit to data (string)
    param_ests -- estimates for each parameter (list)
    param_free -- specifies which parameters to estimate (list)
    priors -- define distributions to use as priors (list)
    threshold -- proportion correct to define threshold (float)
    density -- defines grid size across free parameters (int)
    """
    
    # Check that user provided data meets structure expected
    _check_data(data, batch)

    # Check whether x-values need to be log-spaced
    data_copy, logspace = _check_logspace(data, logspace, sigmoid_type, batch)

    # Check that parameter estimates/constraints are reasonable
    param_ests = _check_params(data_copy, param_ests, nafc, batch, sigmoid_type)

    # Check parameter constraints provided
    param_free = _check_constraints(param_free)

    # Save options used to fit functions in dictionary for reference
    options = dict()
    options['batch'] = batch
    options['logspace'] = logspace
    options['nafc'] = nafc
    options['sigmoid_type'] = sigmoid_type
    options['param_ests'] = param_ests
    options['param_free'] = param_free
    options['priors'] = priors
    options['threshold'] = threshold
    options['density'] = density

    if options['priors'] is not None:
        # Extract priors defined by user 
        options = _extract_priors(options)
        # Check priors defined by user 
        _check_priors(options)

    # Check that all options provided by user or defaults assigned are acceptable
    _check_options(options)

    # Fit models to data
    if batch is True:
        # Raise warning to inform user that only select parameters will be 
        # saved.
        warnings.warn('''\nWhen Batch mode is TRUE, Bayesfit outputs only select metrics to prevent memory issues that can arise from saving posterior and marginal distributions for a large nuber of datasets.''')
        tmp_metrics = dict()
        metrics = dict()
        for keys in data_copy:
            tmp_options = options.copy()
            tmp_options['param_ests'] = list()
            for i in range(0,4):
                tmp_options['param_ests'].append(options['param_ests'][i][keys])
            # Fit model
            tmp_metrics = _fit_Grid(data_copy[keys], tmp_options)
            tmp_metrics['threshold'] = get_threshold(data_copy[keys], tmp_options, tmp_metrics, tmp_options['threshold'])
            # Record only minimal values about fit to 
            # ensure memory issues are not encountered
            del tmp_metrics['posterior'], tmp_metrics['Marginals'], tmp_metrics['Marginals_X']
            metrics[keys] = tmp_metrics
    elif batch is False:
        metrics = _fit_Grid(data_copy, options)
        metrics['threshold'] = get_threshold(data_copy, options, metrics, options['threshold'])
    # Return tuple of objects
    return metrics, options


#################################################################
#  FITTING FUNCTION USING NUMERICAL INTEGRATION
#################################################################
def _fit_Grid(data, options):
    """Function used to run scripts associated with using 
    grid approximation.
    
    Keyword arguments:
    data -- m x 3 numpy array
    options -- contains all options used to fit model (dictionary)
    """    
    # Initialize metrics dictionary
    metrics = dict()
    
    # Generate grid of values for parameters (force to be equal length)
    grid = _gen_grid(data, options)

    # Save x values for grid/marginals
    metrics['Marginals_X'] = dict()
    metrics['Marginals_X']['scale'] = grid['scale']
    metrics['Marginals_X']['slope'] = grid['slope']
    metrics['Marginals_X']['gamma'] = grid['gamma']
    metrics['Marginals_X']['lambda'] = grid['lambda']
    
    # Compute likelihood
    posterior = _grid_likelihood(data, options, grid)
    metrics['likelihood_surface'] = posterior
    
    # Apply priors to likel1ihood if using Bayesian inference
    if options['priors'] is not None:
        posterior = _apply_priors(data, options, posterior, grid)
    posterior = np.exp(posterior - np.max(posterior))
    
    # Calculate integral of surface
    integral = _calc_integral(posterior, options, metrics)
    metrics['integral'] = integral
    
    # Normalize surface by integral approximated via numerical integration
    posterior /= integral
    posterior /= posterior.sum()

    # Extract relevant metrics from surface
    metrics['posterior'] = posterior
    metrics = _extract_metrics_grid(data, options, metrics, posterior, grid)
    
    # Return variables of interest 
    return metrics    
