"""
*******************************************************
*
*  plot_priors - PLOT PRIORS
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 10, 2018
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


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
    
    # Ensure distribution sums to one
    distro /= distro.sum()
        
    return distro


#################################################################
#  PLOT PRIORS
#################################################################
def plot_priors(options, metrics):
    """Plots prior distribution defined by user when fitting model.
    
    Keyword arguments:
    options -- contains all options used to fit model (dictionary)
    metrics -- contain important metrics about fitted model (dictionary)
    """
    # Generate basic plot of marginal distributions
    fig, axes = plt.subplots(2, 2, 
                             subplot_kw=dict(polar=False), 
                             figsize = (7,6))
    # Label axes
    axes[0,0].set_xlabel('Scale')
    axes[0,1].set_xlabel('Slope')
    axes[1,0].set_xlabel('Gamma')
    axes[1,1].set_xlabel('Lambda')
    axes[0,0].set_ylabel('Probability')
    axes[0,1].set_ylabel('Probability')
    axes[1,0].set_ylabel('Probability')
    axes[1,1].set_ylabel('Probability')
    # Scale parameter
    if 'scale' in options['priors_params'].keys():
        prior = _define_distribution(metrics['Marginals_X']['scale'], 
                                       options['priors_definitions']['scale'],
                                       options['priors_params']['scale'])
        axes[0,0].plot(metrics['Marginals_X']['scale'],
            prior, 
            lw=3, 
            color='#5998ff')
        axes[0,0].fill_between(metrics['Marginals_X']['scale'],
            prior, color='#5998ff', alpha = .4)
    else:
        axes[0,0].text(0.5,0.5, "None",
            horizontalalignment='center', 
            verticalalignment='center', 
            transform=axes[0,0].transAxes)       
    # Slope parameter
    if 'slope' in options['priors_params'].keys():
        prior = _define_distribution(metrics['Marginals_X']['slope'], 
                                       options['priors_definitions']['slope'],
                                       options['priors_params']['slope'])
        axes[0,1].plot(metrics['Marginals_X']['slope'],
            prior, 
            lw=3, 
            color='#5998ff')
        axes[0,1].fill_between(metrics['Marginals_X']['slope'],
            prior, color='#5998ff', alpha = .4)
    else:
        axes[0,1].text(0.5,0.5, "None",
            horizontalalignment='center', 
            verticalalignment='center', 
            transform=axes[0,1].transAxes)     
    # Gamma 
    if 'gamma' in options['priors_params'].keys():
        prior = _define_distribution(metrics['Marginals_X']['gamma'], 
                                       options['priors_definitions']['gamma'],
                                       options['priors_params']['gamma'])
        axes[1,0].plot(metrics['Marginals_X']['gamma'],
            prior, 
            lw=3, 
            color='#5998ff')
        axes[1,0].fill_between(metrics['Marginals_X']['gamma'],
            prior, color='#5998ff', alpha = .4)
    else:
        axes[1,0].text(0.5,0.5, "None",
            horizontalalignment='center', 
            verticalalignment='center', 
            transform=axes[1,0].transAxes)     
    # Lambda
    if 'lambda' in options['priors_params'].keys():
        prior = _define_distribution(metrics['Marginals_X']['lambda'], 
                                       options['priors_definitions']['lambda'],
                                       options['priors_params']['lambda'])
        axes[1,1].plot(metrics['Marginals_X']['lambda'],
            prior, 
            lw=3, 
            color='#5998ff')
        axes[1,1].fill_between(metrics['Marginals_X']['lambda'],
            prior, color='#5998ff', alpha = .4)
    else:
        axes[1,1].text(0.5,0.5, "None",
            horizontalalignment='center', 
            verticalalignment='center', 
            transform=axes[1,1].transAxes)     
    
    plt.tight_layout()
    plt.show()
