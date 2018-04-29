"""
*******************************************************
*
*  psyFunction - GENERATE GENERAL FORMULATION OF PSYCHOMETRIC FUNCTION
*
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 18, 2018
*  Last updated: April 18, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np


#################################################################
#  DEFINE PSYCHOMETRIC FUNCTIONS
#################################################################
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

def psyfunction(x, alpha, beta, gamma, lambda_, sigmoid_type):
    if sigmoid_type == 'logistic':
        return gamma + (1 - lambda_ - gamma) * _logistic(x, alpha, beta)
    elif sigmoid_type == 'weibull':
        return gamma + (1 - lambda_ - gamma) * _weibull(x, alpha, beta)
    elif sigmoid_type == 'gumbel':
        return gamma + (1 - lambda_ - gamma) * _gumbel(x, alpha, beta)
    elif sigmoid_type == 'quick':
        return gamma + (1 - lambda_ - gamma) * _quick(x, alpha, beta)
    elif sigmoid_type == 'log-quick':
        return gamma + (1 - lambda_ - gamma) * _quicklog(x, alpha, beta)
    elif sigmoid_type == 'hyperbolic':
        return gamma + (1 - lambda_ - gamma) * _hyperbolic_secant(x, alpha, beta)
