"""
*******************************************************
*
*  plot_cdf - PLOT MODEL FIT TO DATA
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 18, 2017
*  Last updated: May 29, 2018
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
#  GENERATE CDF PLOT OF MODEL FIT TO DATA
#################################################################

def plot_cdf(data, metrics, options, log_xscale = False):
    
    # Generate copy of data
    data_copy = data
    # Check whether x-values need to be log-spaced
    data_copy, logspace = _check_logspace(data, 
                                          options['logspace'], 
                                          options['sigmoid_type'])
    
    
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
    
    # Generate smooth curve from fitted function
    x_max = data_copy[:, 0].max()
    x_min = data_copy[:, 0].min()
    x_est = np.linspace(x_min, x_max, 1000)
    
    y_pred = _psyfunction(x_est, 
                          metrics['Fit'][0],
                          metrics['Fit'][1],
                          metrics['Fit'][2],
                          metrics['Fit'][3],
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
    ax.axhline(y=metrics['Fit'][2], color='r', linestyle='dashed', linewidth=2, zorder=1)
    # Plot remainder of curve
    ax.scatter(data_copy[:, 0], data_copy[:, 1], color='#5998ff', s=125, alpha=1.0, zorder=5)
    ax.plot(x_est, y_pred, linestyle='-', color='black', linewidth=2, alpha=0.85, zorder=10)
    ax.set_xlabel('Stimulus Intensity', fontsize=16, fontweight='bold')
    ax.set_ylabel('Proportion correct', fontsize=16, fontweight='bold')
    ax.xaxis.set_tick_params(labelsize=13)
    ax.yaxis.set_tick_params(labelsize=13)
    plt.tight_layout()
    plt.show()
