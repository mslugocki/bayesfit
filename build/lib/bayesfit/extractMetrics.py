"""
*******************************************************
*
*  extractMetrics - EXTRACT RELEVANT METRICS FROM TRACE
*  
*  Version:      Version 2.0
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September, 2017
*  Last updated: April 18, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import pymc3 as pm


#################################################################
#  EXTRACT RELEVANT PARAMETERS FROM TRACE USING PYMC3
#################################################################
# Extract fitted parameters and other metrics 
# of importance from trace
def extract_metrics(trace, options):
    # Generate empty dictionary to store fitted values 
    metrics = dict()
    metrics['Fit'] = np.zeros(4)
    # Extract metrics for ALPHA
    if options['param_constraints'][0] is True:
        metrics['alpha'] = pm.summary(trace, varnames=['alpha'])
        metrics['Fit'][0] = pm.summary(trace, varnames=['alpha'])['mean'][0]
    # Extract metrics for BETA
    if options['param_constraints'][1] is True:
        metrics['beta'] = pm.summary(trace, varnames=['beta'])
        metrics['Fit'][1] = pm.summary(trace, varnames=['beta'])['mean'][0]
    # Extract metrics for GAMMA
    if options['param_constraints'][2] is True:
        metrics['gamma'] = pm.summary(trace, varnames=['gamma'])
        metrics['Fit'][2] = pm.summary(trace, varnames=['gamma'])['mean'][0]
    else:
        metrics['Fit'][2] = options['param_ests'][2]
    # Extract metrics for LAMBDA
    if options['param_constraints'][3] is True:
        metrics['lambda'] = pm.summary(trace, varnames=['lambda'])
        metrics['Fit'][3] = pm.summary(trace, varnames=['lambda'])['mean'][0]
    else:
        metrics['Fit'][2] = options['param_ests'][3]
    
    return metrics