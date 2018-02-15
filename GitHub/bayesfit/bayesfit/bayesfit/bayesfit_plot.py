"""
*******************************************************
*
*  BAYESFIT - GENERATE PLOTS
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 2017
*  Last updated: February 18, 2018
*
*******************************************************
"""

#######################################################################
#  IMPORT MODULES
#######################################################################
import numpy as np
import pandas as pd
import seaborn as sns
import scipy as sc 
import matplotlib.pyplot as plt
from matplotlib import rc

#######################################################################
#  GENERATE CDF 
#######################################################################
def cdf(data, options, sample, params, threshold):
        
    # Check relevant input arguments
    if isinstance(options['nAFC'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["nAFC"].'
    if options['lapse'] not in (True, False):
        assert False, 'Options provided are not those made available by module. Revise options provided.'        
    if options['sigmoidType'] not in ('cnorm', 'logistic', 'cauchy', 'weibull'):
        assert False, 'Options provided are not those made available by module. Revise options provided.'    

    # Define lambda
    if options['lapse'] == True:
        lamb = params['lambda'][0]
    elif options['lapse'] == False:
        lamb = 0

    # Generate plot of CDF
    sns.set(color_codes=True)
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})
    rc('axes', linewidth=2)
        
    fig,ax = plt.subplots(nrows = 1, ncols = 1, figsize = (5,5))
    
    if options['logspace'] == 1:
        # Generate smooth curve from fitted function
        x_max = max(data.x)
        x_min = min(data.x)
        x = np.linspace(data.x.min(),data.x.max(),1000)
        if options['sigmoidType'] == 'weibull':    
            y_pred = options['gamma'] + (1-lamb-options['gamma'])* (1 - np.exp(-((x/params['alpha'][0])**params['beta'][0])))
        else:
            assert 'Error: Log-space option assigned value of 1 but Weibull function not assigned.'
        ax.set_xscale('log')
        ax.plot([x_min, threshold], 
            [options['thresholdPC'], options['thresholdPC']], 
             color = 'black', 
             linestyle = 'dotted', 
             linewidth = 2, 
             zorder = 1)
        ax.plot([threshold, threshold], 
            [0, options['thresholdPC']], 
            color = 'black', 
            linestyle = 'dotted', 
            linewidth = 2, 
            zorder = 1)
        ax.set_ylim(-0.05,1.05)

        ax.axhline(y=options['gamma'], color = 'r', linestyle = 'dashed', linewidth = 2, zorder = 1)
        # Plot remainder of curve
        ax.scatter(data.x, data.y, color = '#5998ff', s = 125, alpha = 1.0, zorder = 5)
        ax.plot(x, y_pred, linestyle = '-', color = 'black', linewidth = 2, alpha = 0.85, zorder = 10)  
        ax.set_xlabel('Stimulus Intensity', fontsize = 16, fontweight = 'bold')
        ax.set_ylabel('Proportion correct', fontsize = 16, fontweight = 'bold')
        ax.xaxis.set_tick_params(labelsize=13)
        ax.yaxis.set_tick_params(labelsize=13)
        plt.tight_layout()
        plt.show()
        
    elif options['logspace'] == 0:
        # Generate smooth curve from fitted function
        x_max = max(data.x) + 0.10*max(data.x)
        x_min = min(data.x) - 0.10*max(data.x)
        
        x = np.linspace(data.x.min(),data.x.max(),1000)
        if options['sigmoidType'] == 'cnorm':  
            y_pred = options['gamma'] + (1-lamb-options['gamma'])*sc.stats.norm.cdf(x,params['mu'][0],params['sigma'][0])
        elif options['sigmoidType'] == 'cauchy': 
            y_pred = options['gamma'] + (1-lamb-options['gamma'])*sc.stats.cauchy.cdf(x,params['mu'][0],params['sigma'][0])
        elif options['sigmoidType'] == 'logistic':    
            y_pred = options['gamma'] + (1-lamb-options['gamma'])*(1 / (1 + np.exp(-(x- params['mu'][0])/params['sigma'][0] )))
        elif options['sigmoidType'] == 'weibull':    
            assert 'Erorr: Weibull function assigned, but value of log-space under options set to 0!'
            
        ax.plot([x_min, threshold], 
            [options['thresholdPC'], options['thresholdPC']], 
             color = 'black', 
             linestyle = 'dotted', 
             linewidth = 2, 
             zorder = 1)
        ax.plot([threshold, threshold], 
            [0, options['thresholdPC']], 
            color = 'black', 
            linestyle = 'dotted', 
            linewidth = 2, 
            zorder = 1)
        ax.set_xlim(x_min,x_max)
        ax.set_ylim(-0.05,1.05)
        ax.axhline(y=options['gamma'], color = 'r', linestyle = 'dashed', linewidth = 2, zorder = 1)
        # Plot remainder of curve
        ax.scatter(data.x, data.y, color = '#5998ff', s = 125, alpha = 1.0, zorder = 5)
        ax.plot(x, y_pred, linestyle = '-', color = 'black', linewidth = 2, alpha = 0.85, zorder = 10)  
        ax.set_xlabel('Stimulus Intensity', fontsize = 16, fontweight = 'bold')
        ax.set_ylabel('Proportion correct', fontsize = 16, fontweight = 'bold')
        ax.xaxis.set_tick_params(labelsize=13)
        ax.yaxis.set_tick_params(labelsize=13)
        plt.tight_layout()
        plt.show()
        
#######################################################################
#  GENERATE DENSITY PLOT
#######################################################################
def density(data, options, sample, params):
    
    # Check relevant input arguments
    if isinstance(options['nAFC'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["nAFC"].'
    if options['sigmoidType'] != 'cnorm' and 'logistic' and 'cauchy' and 'gumbel' and 'weibull' == False:
        assert False, 'Options provided are not those made available by module. Revise options provided.'
    if options['lapse'] != True and False == False:
        assert False, 'Options provided are not those made available by module. Revise options provided.'

    # Get parameter labels
    x_labels = list(params.columns.values)
    
    # Plot density
    sns.set(color_codes=True)
    samples = sample.extract()
    fig,(ax1,ax2,ax3) = plt.subplots(3,1)
    sns.distplot(samples[x_labels[0]],ax=ax1)
    ax1.set(ylabel='Frequency', xlabel=x_labels[0].capitalize())
    sns.distplot(samples[x_labels[1]],ax=ax2)
    ax2.set(ylabel='Frequency', xlabel=x_labels[1].capitalize())
    if options['lapse'] == True:
        sns.distplot(samples['lambda'],ax=ax3)
        ax3.set(ylabel='Frequency', xlabel=x_labels[2].capitalize())
    fig.tight_layout()
    plt.show()
    
    
#######################################################################
#  GENERATE 2D DENSITY PLOT
#######################################################################
def td_density(data, options, sample, params):
    
    # Check relevant input arguments
    if isinstance(options['nAFC'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["nAFC"].'
    if options['sigmoidType'] != 'cnorm' and 'logistic' and 'cauchy' and 'gumbel' and 'weibull' == False:
        assert False, 'Options provided are not those made available by module. Revise options provided.'
    if options['lapse'] != True and False == False:
        assert False, 'Options provided are not those made available by module. Revise options provided.'

    # Get parameter labels
    x_labels = list(params.columns.values)
    
    # Plot 2D density
    sns.set(color_codes=True)
    samples = sample.extract()
    temp_frame = pd.DataFrame(samples,columns=x_labels) 
    sns.jointplot(x = x_labels[0],y = x_labels[1],data=temp_frame, kind="kde")
    plt.show()
    
    
#######################################################################
#  GENERATE PLOT OF TRACES
#######################################################################
def trace(data, options, sample, params):
    
    # Check relevant input arguments
    if isinstance(options['nAFC'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["nAFC"].'
    if options['sigmoidType'] != 'cnorm' and 'logistic' and 'cauchy' and 'gumbel' and 'weibull' == False:
        assert False, 'Options provided are not those made available by module. Revise options provided.'
    if options['lapse'] != True and False == False:
        assert False, 'Options provided are not those made available by module. Revise options provided.'

    # Get parameter labels
    x_labels = list(params.columns.values)
    
    # Plot traces
    sns.set(color_codes=True)
    samples = sample.extract()
    fig,(ax1,ax2,ax3) = plt.subplots(3,1)
    ax1.plot(samples[x_labels[0]])
    ax1.set_xlabel(x_labels[0].capitalize())
    ax2.plot(samples[x_labels[1]])
    ax2.set_xlabel(x_labels[1].capitalize())
    ax3.plot(samples[x_labels[2]])
    ax3.set_xlabel(x_labels[2].capitalize())
    fig.tight_layout()
    plt.show()