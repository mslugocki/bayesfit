"""
*******************************************************
*
*  plot_marginals - PLOT MARGINALS
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 10, 2018
*  Last updated: September 18, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import matplotlib.pyplot as plt


#################################################################
#  PLOT MARGINAL DISTRIBUTION
#################################################################
def plot_marginals(metrics):
    """Plots marginal distributions for each parameter of 
    the fitted model.
    
    Keyword arguments:
    metrics -- contain important metrics about fitted model (dictionary)
    """
    # Generate basic plot of marginal distributions
    fig, axes = plt.subplots(2, 2, 
                             subplot_kw=dict(polar=False), 
                             figsize = (7,6))
    # Scale parameter
    axes[0,0].set_xlabel('Scale')
    axes[0,1].set_xlabel('Slope')
    axes[1,0].set_xlabel('Gamma')
    axes[1,1].set_xlabel('Lambda')
    # Loop through and plot marginals that exist
    counter = 0
    idx = np.array([[0,0], [0,1], [1,0], [1,1]])
    for keys in ['scale', 'slope', 'gamma', 'lambda']:
        axes[idx[counter,0],idx[counter,1]].set_ylabel('Probability')
        if metrics['Marginals'][keys] is not np.nan and metrics['Marginals'][keys].size > 1:
            axes[idx[counter,0],idx[counter,1]].plot(metrics['Marginals_X'][keys],
                metrics['Marginals'][keys], 
                lw=3, 
                color='#5998ff')
            axes[idx[counter,0],idx[counter,1]].fill_between(metrics['Marginals_X'][keys],
                metrics['Marginals'][keys], color='#5998ff', alpha = .4)
        elif metrics['Marginals'][keys].size == 1:
            axes[idx[counter,0],idx[counter,1]].text(0.5,0.5, "None",
                horizontalalignment='center', 
                verticalalignment='center', 
                transform=axes[idx[counter,0],idx[counter,1]].transAxes)
        # Update counter
        counter += 1
    plt.tight_layout()
    plt.show()
