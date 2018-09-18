"""
*******************************************************
*
*  plot_psyFcn - PLOT MODEL FIT TO DATA
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 18, 2017
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import matplotlib.pyplot as plt
from .psyFunction import psyfunction as _psyfunction
from .checkLogspace import check_logspace as _check_logspace


#################################################################
#  GENERATE PLOT OF MODEL FIT TO DATA
#################################################################
def plot_psyfcn(data, 
                options,
                metrics,
                log_xscale = False, 
                scale_pnts = True,
                estimate_type = 'MAP'):
    """Plots psychometric function from fitted model.
    
    Keyword arguments:
    data -- m x 3 numpy array
    options -- contains all options used to fit model (dictionary)
    metrics -- contain important metrics about fitted model (dictionary)
    log_xscale -- log-transform x-scale (logical)
    scale_pnts -- scale size of points by N-trial number (logical)
    estimate_type -- determines which metric to use for parameters of model (string)
    """
    
    if estimate_type not in ('MAP', 'Mean'):
        raise ValueError('Please provide appropriate argument for estimate type (e.g., MAP, Mean)')
    
    # Determine which values to use for vector of parameters 
    param_guess = np.zeros(4)
    counter = 0
    for keys in options['param_free']:
        if keys is True:
            param_guess[counter] = metrics[estimate_type][counter]
        elif keys is False: 
            param_guess[counter] = options['param_ests'][counter]
        counter += 1

    # Generate copy of data
    data_copy = data
    # Check whether x-values need to be log-spaced
    data_copy, logspace = _check_logspace(data, 
                                          options['logspace'], 
                                          options['sigmoid_type'],
                                          options['batch'])
    
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
    
    # Generate smooth curve from fitted function
    x_max = data_copy[:, 0].max()
    x_min = data_copy[:, 0].min()
    x_est = np.linspace(x_min, x_max, 1000)
    
    y_pred = _psyfunction(x_est, 
                          param_guess[0],
                          param_guess[1],
                          param_guess[2],
                          param_guess[3],
                          options['sigmoid_type'])

    if log_xscale is True:
        ax.set_xscale('log')
    ax.plot([x_min, metrics['threshold']],
            [options['threshold'], options['threshold']],
            color='black',
            linestyle='dotted',
            linewidth=2,
            zorder=1)
    ax.plot([metrics['threshold'], metrics['threshold']], 
            [0, options['threshold']],
            color='black',
            linestyle='dotted',
            linewidth=2,
            zorder=1)
    ax.set_ylim(-0.05, 1.05)
    ax.axhline(y=param_guess[2], color='r', linestyle='dashed', linewidth=2, zorder=1)
    # Plot remainder of curve            
    if scale_pnts is True:
        for i in range(data[:,0].shape[0]): 
            ax.scatter(data_copy[i,0], 
                       data_copy[i,1]/data_copy[i,2], 
                       color='#5998ff', 
                       s=data_copy[i,2]*2, 
                       alpha=0.5, 
                       zorder=5, 
                       marker='o')
    elif scale_pnts is False: 
        ax.scatter(data_copy[:,0], 
                   data_copy[:,1]/data_copy[:,2], 
                   color='#5998ff', 
                   s=135, 
                   alpha=0.5, 
                   zorder=5, 
                   marker='o')    
     ax.plot(x_est, y_pred, linestyle='-', color='black', linewidth=2, alpha=0.85, zorder=10)
    ax.set_xlabel('Stimulus Intensity', fontsize=16)
    ax.set_ylabel('Proportion correct', fontsize=16)
    ax.xaxis.set_tick_params(labelsize=13)
    ax.yaxis.set_tick_params(labelsize=13)
    plt.tight_layout()
    plt.show()
