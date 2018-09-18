"""
*******************************************************
*
*  plot_posterior - PLOT POSTERIOR
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 8, 2018
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import matplotlib.pyplot as plt


#################################################################
#  PLOT POSTERIOR 
#################################################################
def plot_posterior(metrics):
    """Plots posterior surface for scale and slope parameters
    collapsing across guess and lapse rates.
    
    Keyword arguments:
    metrics -- contain important metrics about fitted model (dictionary)
    """
    # If other method other than numerical integration used, 
    # raise error 
    try: 
        metrics['posterior'] 
    except NameError: 
        raise ValueError('Posterior can only be plotted for numerical integration method (i.e., grid)')
    # Compute joint marginal posterior collapsing across nusiance 
    # parameters 
    posterior = np.sum(metrics['posterior'], axis = (2,3))
    # Generate plot of posterior with scale and 
    plt.contourf(metrics['Marginals_X']['scale'], 
                 metrics['Marginals_X']['slope'], 
                 posterior)
    plt.xlabel('scale', fontsize = 16)
    plt.ylabel('slope', fontsize = 16)
    plt.colorbar()
    plt.tight_layout()
    plt.show()
