"""
*******************************************************
*
*  geweke_plot - GENERATE GEWEKE PLOT TO TEST FOR CONVERGENCE
*  
*  Version:      Version 2.1
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


#################################################################
#  FUNCTION IMPLEMENTING THE GEWEKE DIAGNOSTIC
#################################################################

# Function to correlate two segments of trace
def _rhot(x, t_idx):
    n = len(x)
    return np.corrcoef(x[0:(n-t_idx)], x[t_idx:n])[0, 1]


def _geweke(trace, intervals, length):
    # Divide trace minus burn-in into equal intervals. 
    jump = int(0.7*len(trace)/(2*intervals))
    # Get rid of the burnin segment
    first = 0.3*len(trace)
    
    z = np.empty(intervals)
    # Loop through each pair of intervals 
    for k in np.arange(0, intervals):
        samplepool_a = np.int(first+k*jump)
        samplepoolb = np.int(len(trace)/2 + k*jump)
        sub_trace_a = np.array(trace[samplepool_a:samplepool_a+length])
        sub_trace_b = np.array(trace[samplepoolb:samplepoolb+length])
        theta_a = np.mean(sub_trace_a)
        theta_b = np.mean(sub_trace_b)
        rho_a, rho_b = 1.0, 1.0
        
        for i in np.arange(int(0.1*length)):
            rho_a += 2*_rhot(sub_trace_a, i+1)
            rho_b += 2*_rhot(sub_trace_b, i+1)
            
        var_a = np.var(sub_trace_a)*rho_a/length
        var_b = np.var(sub_trace_b)*rho_b/length
        
        z[k] = (theta_a-theta_b)/np.sqrt(var_a + var_b)
    
    return z


#################################################################
#  PLOT GEWEKE Z-SCORES
#################################################################
def geweke_plot(trace, intervals, length):
    # Plot Geweke z-scores
    geweke_zscores = _geweke(trace=trace,
                             intervals=intervals,
                             length=length)
    plt.plot(geweke_zscores, 'o')
    plt.hlines([-2, 2],
               xmin=0,
               xmax=intervals + 1,
               linestyles='dotted')
    plt.ylim(-3, 3)
    plt.xlabel('Interval')
    plt.ylabel('Geweke z-score')
    plt.show()
