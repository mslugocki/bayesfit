"""
*******************************************************
*
*  BayesFit - CORE FILE
*  
*  Version:      Version 2.2
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September, 2017
*  Last updated: May 29, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES 
#################################################################

import numpy as np
import re
import os 
import matplotlib
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    matplotlib.use('Agg')
import pymc3 as pm

from .checkData import check_data as _check_data
from .checkLogspace import check_logspace as _check_logspace
from .checkParams import check_params as _check_params
from .checkParams import check_constraints as _check_constraints
from .checkOptions import check_options as _check_options 
from .psyFunction import psyfunction as _psyfunction
from .extractMetrics import extract_metrics as _extract_metrics
from .extractThreshold import get_threshold
from .extractPriors import extract_priors as _extract_priors
from .checkPriors import check_priors as _check_priors
from .definePriors import define_priors as _define_priors
from .gewekePlot import geweke_plot
from .plot_CDF import plot_cdf


#################################################################
#  BAYESFIT CORE FUNCTION THAT ACCEPTS ARGUMENTS FROM USE 
#################################################################

def fitmodel(data,
             batch=False,
             logspace=None,
             nafc=2,
             sigmoid_type='logistic',
             param_ests=None,
             param_constraints=None,
             priors=None,
             threshold=0.75,
             n_samples=5000,
             chains=2,
             n_workers=1
             ):
    
    # Check that user provided data meets structure expected
    _check_data(data, batch)

    # Check whether x-values need to be log-spaced
    data_copy, logspace = _check_logspace(data, logspace, sigmoid_type)

    # Check that parameter estimates/constraints are reasonable
    param_ests = _check_params(data_copy, param_ests, nafc, batch)

    # Check parameter constraints provided
    param_constraints = _check_constraints(param_constraints)

    # Save options used to fit functions in dictionary for reference
    options = dict()
    options['batch'] = batch
    options['logspace'] = logspace
    options['nafc'] = nafc
    options['sigmoid_type'] = sigmoid_type
    options['param_ests'] = param_ests
    options['param_constraints'] = param_constraints
    options['priors'] = priors
    options['threshold'] = threshold
    options['n_samples'] = n_samples
    options['chains'] = chains
    options['n_workers'] = n_workers

    if options['priors'] is not None:
        # Extract priors defined by user 
        options = _extract_priors(options)
        # Check priors defined by user 
        _check_priors(options)

    # Check that all options provided by user or defaults assigned are acceptable
    _check_options(options)

    # Fit models to data
    if batch is True:
        metrics = dict()
        trace = dict()
        for keys in data_copy:
            trace[keys] = _fitmodel(data_copy[keys], options)
            metrics[keys] = _extract_metrics(trace[keys], options)
            metrics[keys]['threshold'] = get_threshold(data_copy[keys], metrics[keys], options, options['threshold'])
    elif batch is False:
        trace = _fitmodel(data_copy, options)
        metrics = _extract_metrics(trace, options)
        metrics['threshold'] = get_threshold(data_copy, metrics, options, options['threshold'])
    # Return tuple of objects
    return trace, metrics, options


#################################################################
#  FITTING FUNCTION THAT USES PYMC3 TO DRAW SAMPLES
#  FROM THE POSTERIOR
#################################################################

def _fitmodel(data, options):

    # Convert data to long sequence
    x = np.array([])
    y = np.array([])
    for i in range(len(data[:, 0])):
        approx_numsequence = np.round(data[i, 1]*data[i, 2])
        response_y = np.zeros(int(data[i, 2]))
        response_y[:int(approx_numsequence)] = 1
        response_x = np.repeat(data[i, 0], data[i, 2])
        x = np.append(x, response_x)
        y = np.append(y, response_y)
    
    # Fit model
    with pm.Model() as fitted_model:
        if options['priors'] is not None:
            # Define distributions
            alpha, beta, gamma, lambda_ = _define_priors(data, options)
            
        else: 
            # Create the priors for alpha and beta parameters
            alpha = pm.Normal('alpha', 
                              mu=options['param_ests'][0], 
                              sd=2)
            beta = pm.Gamma('beta', 
                            alpha=options['param_ests'][1], 
                            beta=0.5)
            # Create priors for gamma
            if options['param_constraints'][2] is True:
                gamma = pm.Normal('gamma',
                                  mu=options['param_ests'][2], 
                                  sd=0.2)
            else:
                gamma = options['param_ests'][2]
            # Create prior for lambda
            if options['param_constraints'][3] is True:
                if data[len(data[:, 2])-1, 1] > 0.80:
                    lambda_ = pm.Beta('lambda', 2, 20)
                else:
                    lambda_ = pm.Beta('lambda', 1.5, 12)
            else:
                lambda_ = options['param_ests'][3]

        # Create the probability from the logistic function
        p = pm.Deterministic('p',  _psyfunction(x,
                                                alpha,
                                                beta,
                                                gamma,
                                                lambda_,
                                                options['sigmoid_type']))

        # Create the bernoulli parameter which makes use of the observed data
        observed = pm.Bernoulli('obs', p, observed=y)

        # Choose MCMC sampling algorithm
        mcmc_sampler = pm.Metropolis()

        # Sample from the posterior using the sampling method
        model_trace = pm.sample(options['n_samples'],
                                step=mcmc_sampler,
                                njobs=1,
                                chains=2)

        return model_trace
