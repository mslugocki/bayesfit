"""
*******************************************************
*
*  plot_cdf - PLOT MODEL FIT TO DATA
*  
*  Version:      Version 2.0
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 18, 2017
*  Last updated: April 18, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import matplotlib.pyplot as plt
from .psyFunction import psyfunction as _psyfunction


#################################################################
#  GENERATE CDF PLOT OF MODEL FIT TO DATA
#################################################################

def plot_cdf(data, metrics, options):
    
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5))
    
    # Generate smooth curve from fitted function
    x_max = data[:, 0].max()
    x_min = data[:, 0].min()
    x_est = np.linspace(x_min, x_max, 1000)
    
    y_pred = _psyfunction(x_est, 
                          metrics['Fit'][0],
                          metrics['Fit'][1],
                          metrics['Fit'][2],
                          metrics['Fit'][3],
                          options['sigmoid_type'])
    if options['logspace'] is True:
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
    ax.scatter(data[:, 0], data[:, 1], color='#5998ff', s=125, alpha=1.0, zorder=5)
    ax.plot(x_est, y_pred, linestyle='-', color='black', linewidth=2, alpha=0.85, zorder=10)
    ax.set_xlabel('Stimulus Intensity', fontsize=16, fontweight='bold')
    ax.set_ylabel('Proportion correct', fontsize=16, fontweight='bold')
    ax.xaxis.set_tick_params(labelsize=13)
    ax.yaxis.set_tick_params(labelsize=13)
    plt.tight_layout()
    plt.show()
