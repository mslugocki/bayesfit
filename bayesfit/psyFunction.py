"""
*******************************************************
*
*  psyFunction - GENERATE GENERAL FORMULATION OF PSYCHOMETRIC FUNCTION
*
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 18, 2018
*  Last updated: August 30, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
from scipy.special import erf


#################################################################
#  DEFINE PSYCHOMETRIC FUNCTIONS
#################################################################
# Cumulative Gaussian
def _norm(x, xShift, sd):
    return ((erf((x-xShift)/(np.sqrt(2)*sd))+1)*0.5)

# Logistic
def _logistic(x, alpha, beta):
    return 1 / (1 + np.exp(-beta*(x - alpha)))


# Weibull
def _weibull(x, alpha, beta):
    return 1 - np.exp(-(x/alpha)**beta) 


# Gumbel
def _gumbel(x, alpha, beta):
    return 1 - np.exp(-10**(beta*(x-alpha)))


# Quick
def _quick(x, alpha, beta):
    return 1 - 2**(-(x/alpha)**beta)


# Log-Quick
def _quicklog(x, alpha, beta):
    return 1 - 2**(-10**(beta*(x - alpha)))


# Hyperbolic Secant
def _hyperbolic_secant(x, alpha, beta):
    return (2/np.pi)*np.arctan(np.exp((np.pi/2)*beta*(x - alpha)))


#################################################################
#  DEFINE GENERIC FORMULATION OP PSYCHOMETRIC FUNCTIONS
#################################################################

# Note: Although laballed as scale and slope, these parameters
# can jointly determine such characteristics depending upon
# the PF function chosen (e.g., Weibull).
def psyfunction(x, scale, slope, gamma, lambda_, sigmoid_type):
    with np.errstate(divide='ignore',invalid='ignore', over ='ignore'):
        if sigmoid_type == 'norm':
            return gamma + (1 - lambda_ - gamma) * _norm(x, scale, slope)
        elif sigmoid_type == 'logistic':
            return gamma + (1 - lambda_ - gamma) * _logistic(x, scale, slope)
        elif sigmoid_type == 'weibull':
            return gamma + (1 - lambda_ - gamma) * _weibull(x, scale, slope)
        elif sigmoid_type == 'gumbel':
            return gamma + (1 - lambda_ - gamma) * _gumbel(x, scale, slope)
        elif sigmoid_type == 'quick':
            return gamma + (1 - lambda_ - gamma) * _quick(x, scale, slope)
        elif sigmoid_type == 'log-quick':
            return gamma + (1 - lambda_ - gamma) * _quicklog(x, scale, slope)
        elif sigmoid_type == 'hyperbolic':
            return gamma + (1 - lambda_ - gamma) * _hyperbolic_secant(x, scale, slope)
