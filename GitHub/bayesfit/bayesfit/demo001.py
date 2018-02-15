"""
*******************************************************
*
*  BAYESFIT - DEMO 001
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September 2017
*  Last updated: February 18, 2018
*
*******************************************************
"""

# This demo shows you how to use BayesFit with the AUTO fitting
# feature.  This feature usually performs quite well if you 
# have well behaving functions at choosing the appropriate distributions
# and bounds to assign. 


#######################################################################
#  IMPORT MODULES 
#######################################################################
import os 
import pandas as pd
import bayesfit as bf
import numpy as np


#######################################################################
#  GENERATE DATA SET
#######################################################################
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
y = [0.51, 0.53, 0.57, 0.81, 0.94, 0.96, 0.99] 
N = [20, 20, 20, 20, 20, 20, 20]
data = pd.DataFrame({'x':x, 'y':y, 'N':N})


#######################################################################
#  INITIALIZE OPTIONS, GENERATE MODEL, SAMPLE FROM MODEL, AND EXTRACT PARAMS
#######################################################################
# Initialize options variable as dictionary type
options = dict()
# Determines the value of gamma (guess rate) to which the function is fit (default = 2)
options['nAFC'] = 2
# Define function
options['sigmoidType'] = 'cnorm'
# Define lapse rate
options['lapse'] = True
# Define fit 
options['fit'] = 'auto'
# Aggregate data options
options['agg_data'] = True
# Build model 
model, sample, options = bf.bayesfit(data, options)
# Extract parameters
params, threshold = bf.extractParams(data, options, sample)


#######################################################################
#  PLOT FUNCTIONS 
#######################################################################
# Plot CDF
bf.plot.cdf(data, options, sample, params, threshold)
# Plot desnity
bf.plot.density(data, options, sample, params)
# Plot 2D desnity 
bf.plot.td_density(data, options, sample, params)
# Plot traces
bf.plot.trace(data, options, sample, params)