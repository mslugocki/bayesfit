"""
*******************************************************
*
*  extractPriors - EXTRACT PRIORS PROVIDED BY USER 
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   May 19, 2018
*  Last updated: May 29, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
import re 


#################################################################
#  EXTRACT LIST OF PRIORS PROVIDED
#################################################################

# Extract priors from 
def extract_priors(options): 

    # Initialize empty dictionary to store priors 
    options['priors_definitions'] = dict()
    options['priors_params'] = dict()

    if len(options['priors']) < 1:
        raise Exception('''Please provide at least two arguments for definitions 
                            of priors''')
    
    else: 
        if len(options['priors']) >=2:
            # Extract prior for alpha parameter
            options['priors_definitions']['alpha'] = " ".join(re.findall("[a-zA-Z]+", 
                                                              options['priors'][0]))
            
            alpha_prior_values = re.findall(r'[-+]?\d*\.\d+|\d+', options['priors'][0])
            options['priors_params']['alpha'] = [np.float(x) for x in alpha_prior_values]
            
            # Extract prior for beta parameter
            options['priors_definitions']['beta'] = " ".join(re.findall("[a-zA-Z]+", 
                                                             options['priors'][1]))
            
            beta_prior_values = re.findall(r'[-+]?\d*\.\d+|\d+', options['priors'][1])
            options['priors_params']['beta'] = [np.float(x) for x in beta_prior_values]
            
            
        if len(options['priors']) >= 3:
            # Extract prior for gamma parameter
            options['priors_definitions']['gamma']  = " ".join(re.findall("[a-zA-Z]+", 
                                                               options['priors'][2]))  
            gamma_prior_values = re.findall(r'[-+]?\d*\.\d+|\d+', options['priors'][2])
            options['priors_params']['gamma'] = [np.float(x) for x in gamma_prior_values]
            
        if len(options['priors']) == 4:     
            # Extract prior for lambda parameter
            options['priors_definitions']['lambda']  = " ".join(re.findall("[a-zA-Z]+", 
                                                                options['priors'][3]))
    
            lambda_prior_values = re.findall(r'[-+]?\d*\.\d+|\d+', options['priors'][3])
            options['priors_params']['lambda'] = [np.float(x) for x in lambda_prior_values]
        
        return options
