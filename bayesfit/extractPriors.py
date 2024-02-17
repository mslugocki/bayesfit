"""
*******************************************************
*
*  extractPriors - EXTRACT PRIORS PROVIDED BY USER 
*  
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   May 19, 2018
*  Last updated: February 17, 2024
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
# Extract priors from options
def extract_priors(options): 
    """Extract priors from user definitions using regular
    expressions, and store under new keys in options.

    Keyword arguments:
    options -- contains all options used to fit model (dictionary)
    """
    # Initialize empty dictionary to store priors 
    options['priors_definitions'] = dict()
    options['priors_params'] = dict()

    if len(options['priors']) < 4:
        raise ValueError('''Please provide list of four arguments for 
                            priors. Less than four arguments provided.''')
    elif len(options['priors']) > 4:
        raise ValueError('''Please provide list of four arguments for 
                            priors. More than four arguments provided.''')
    elif len(options['priors']) == 4: 
        NoneType = type(None)
        # Check whether arguments in list are of type integer or float
        for i in range(0,4):
            if isinstance(options['priors'][i], (str, NoneType)) is False:
                raise ValueError('''User Error: Please provide numerical values or NoneType 
                                 for priors of parameters of the model.''')
        
            if options['priors'][i] is not None:
                if i == 0:
                    # Extract prior for alpha parameter
                    options['priors_definitions']['scale'] = " ".join(re.findall("[a-zA-Z]+", 
                                                                      options['priors'][0]))
                    
                    alpha_prior_values = re.findall(r'[-+]?\d*\.\d+|\d+', options['priors'][0])
                    options['priors_params']['scale'] = [float(x) for x in alpha_prior_values]
                elif i == 1:
                    # Extract prior for beta parameter
                    options['priors_definitions']['slope'] = " ".join(re.findall("[a-zA-Z]+", 
                                                                     options['priors'][1]))
                    
                    beta_prior_values = re.findall(r'[-+]?\d*\.\d+|\d+', options['priors'][1])
                    options['priors_params']['slope'] = [float(x) for x in beta_prior_values]    
                elif i == 2:
                    # Extract prior for gamma parameter
                    options['priors_definitions']['gamma']  = " ".join(re.findall("[a-zA-Z]+", 
                                                                       options['priors'][2]))  
                    gamma_prior_values = re.findall(r'[-+]?\d*\.\d+|\d+', options['priors'][2])
                    options['priors_params']['gamma'] = [float(x) for x in gamma_prior_values]
                elif i == 3:
                    # Extract prior for lambda parameter
                    options['priors_definitions']['lambda']  = " ".join(re.findall("[a-zA-Z]+", 
                                                                        options['priors'][3]))
            
                    lambda_prior_values = re.findall(r'[-+]?\d*\.\d+|\d+', options['priors'][3])
                    options['priors_params']['lambda'] = [float(x) for x in lambda_prior_values]
            
        return options
