"""
*******************************************************
*
*  BAYESFIT - CORE FILE
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
import pystan as ps 
import pandas as pd
import scipy as sc
from copy import deepcopy as _deepcopy

# Functions from other files in module
from . import bayesfit_plot as plot


#######################################################################
#  WRAPPER FUNCTION FOR ACCEPTING INPUTS
#######################################################################
def bayesfit(data, options):

    # Check data structure provided by user
    # Format requested is a N x 3 data frame such that [x, y, N]
    if data.shape[1] != 3:
        raise Exception('Data provided does not contain the number of columns required! (i.e., [x, y, N])') 
    assert data.y.min() >= 0, 'The y-values provided contain a proportion less than zero! ' 
    assert data.y.max() <= 1, 'The y-values provided contain a proportion greater than one! ' 

    # Check user input for options
    if not('options' in locals()): 
        options = dict()
        
    else:
        options = _deepcopy(options)
        
    # Define sigmoid function 
    if not('sigmoidType' in options.keys()):
        options['sigmoidType'] = 'cnorm'
        
    # Define number of alternatives
    if not('nAFC' in options.keys()):
        options['nAFC'] = 2
         
    # Define gamma
    if options['nAFC'] == 0:
        options['gamma'] = 0
    else:
        options['gamma'] = 1/options['nAFC']
        
    # Specify wehtehr lapse rate should be estimated
    if not('lapse' in options.keys()):
        options['lapse'] = True
        
    # Determines whether the fit 
    if not('fit' in options.keys()):
        options['fit'] = 'auto'
            
    # Determines whether aggregate data provided
    if not('agg_data' in options.keys()):
        options['agg_data'] = False
        data = gen_aggregateData(data)
                
    # How the parameter estimated are obtained from posterior
    if not('param_ests' in options.keys()):
        options['param_ests'] = 'mean'
        
    # Value that threshold is defined at
    if not('thresholdPC' in options.keys()):
        options['thresholdPC'] = .75    
        
    # Check arguments for sampling the posterior
    if not('iter' in options.keys()):
        options['iter'] = 10000
        
    if not('chains' in options.keys()):
        options['chains'] = 1  
    
    # Check sigmoid type provided to convert to logspace where necessary 
    if options['sigmoidType'] in ['weibull']:
        options['logspace'] = 1
        assert data.x.min() > 0, 'The sigmoid you specified is not defined for negative data points!'
    else:
        options['logspace'] = 0

    # Check options provided are valid options
    if options['fit'] not in ('auto', 'manual_full', 'manual_part'):
        assert False, 'Options provided are not those made available by module. Revise options provided.'
    if options['lapse'] not in (True, False):
        assert False, 'Options provided are not those made available by module. Revise options provided.'        
    if options['sigmoidType'] not in ('cnorm', 'logistic', 'cauchy', 'weibull'):
        assert False, 'Options provided are not those made available by module. Revise options provided.'                
    if isinstance(options['nAFC'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["nAFC"].'
    if isinstance(options['iter'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["iter"].'    
    if isinstance(options['chains'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["chains"].'
    
    # File that performs compilation of model in STAN  
    print('---------------------------------------------------') 
    print('--- COMPILE MODEL ...                  ')
    model = modelCompile(data,options)
    print('--- COMPILE MODEL ...      COMPLETE ---------------')

    # File that samples from posterior    
    print('--- SAMPLE USING MODEL ...             ')
    sample = modelSample(data, options, model)    
    print('--- SAMPLE USING MODEL ... COMPLETE ---------------')
    
    # Print message to update user that process is complete
    print('---                           ')
    print('--- ALL PROCESSES COMPLETE ---')
    
    # Return tuple of objects
    return (model, sample, options)


#######################################################################
#  FUNCTION FOR COMPILING MODEL INTO C++ CODE
#######################################################################
def modelCompile(data, options, model_definition=dict()):
    
    # Check argument for model definition 
    if not('model_definition' in locals()):
        if options['fit'] == 'auto':
            model_definition = dict()
        elif options['fit'] == 'manual_full':
            assert False, 'Manual fit option chosen!\nNeed to provide *COMPLETE* model definition for STAN!'
    
    #######################################################################
    #  MODEL_DEFINITION == AUTO
    #######################################################################
    if options['fit'] in ('auto', 'manual_part'):
        
        # Get initial estimate of alpha via linear regression
        def scale_est(data,options):
            y = [data.y[0], data.y[data.y.shape[0]-1]]
            x = [data.x[0], data.x[data.x.shape[0]-1]] 
            init_scale = np.polyfit(x, y, 1)
            scale_estimate = [(0.70 - init_scale[1]) / init_scale[0]]
            return scale_estimate[0]
        
        # Guess value to use for scale parameter
        scale_guess = scale_est(data, options) 
        
        # Define distributions and bounds to use for each parameter
        if options['fit'] == 'auto':
            if options['sigmoidType'] == 'weibull':
                parinis = {'alpha':['normal', scale_guess, 3], 'beta':['uniform', 0, 9]}
            else:
                parinis = {'mu':['normal', scale_guess, 3], 'sigma':['uniform', 0, 9]}
        elif options['fit'] == 'manual_part':
            parinis = options['parinis']
            if len(parinis) < 2:
                assert True, '''You have provided less than two lists in dictionary 
                                to use for distributions when compiling model.
                                Please revise and provide at least two arguments.'''
        
        # Define data structure for stable portions of code 
        model_definition['data'] = '''
            data {
            int<lower=1> N;
            real x[N];
            int<lower=0,upper=1> y[N];
            }'''            
        
        # Define sigmoid function to use
        if options['sigmoidType'] == 'weibull':
            model_definition['parameters_pt1'] = '''
                parameters {
                real<lower=0> beta;
                real<lower=0> alpha; '''
            model_definition['likelihood_scale'] = ('''model {beta ~ %s(%f,%f);''' 
                            %(parinis['beta'][0], 
                            parinis['beta'][1], 
                            parinis['beta'][2]))
            model_definition['likelihood_shape'] = ('''alpha ~ %s(%f,%f);''' 
                            %(parinis['alpha'][0],
                              parinis['alpha'][1], 
                              parinis['alpha'][2]))            
        else:
            model_definition['parameters_pt1'] = '''
                parameters {
                real<lower=0> mu;
                real<lower=0> sigma; '''
            model_definition['likelihood_scale'] = ('''model {mu ~ %s(%f,%f);''' 
                            %(parinis['mu'][0], 
                            parinis['mu'][1], 
                            parinis['mu'][2]))
            model_definition['likelihood_shape'] = ('''sigma ~ %s(%f,%f);''' 
                            %(parinis['sigma'][0],
                              parinis['sigma'][1], 
                              parinis['sigma'][2]))           
                
        # Define sigmoid likelihood functions
        if options['sigmoidType'] == 'cnorm':    
            model_definition['likelihood_model_pt2'] = ''' *normal_cdf(x[i],mu, sigma));}} '''  
        elif options['sigmoidType'] == 'logistic':    
            model_definition['likelihood_model_pt2'] = ''' *logistic_cdf(x[i],mu, sigma));}} '''  
        elif options['sigmoidType'] == 'cauchy':    
            model_definition['likelihood_model_pt2'] = ''' *cauchy_cdf(x[i],mu, sigma));}} '''
        elif options['sigmoidType'] == 'weibull':
            model_definition['likelihood_model_pt2'] = ''' *weibull_cdf(x[i],beta, alpha));}} '''

        # Define lapse specific structures 
        if options['lapse'] == True:
            model_definition['parameters_pt2'] = '''
                real<lower=0> lambda;
                }'''
            model_definition['likelihood_lambda'] = '''   
                lambda ~ beta(2,20); '''   
            model_definition['likelihood_model_pt1'] = ('''  for (i in 1:N){y[i] ~ bernoulli(%f + (1-lambda-%f) ''' 
                            %(options['gamma'], options['gamma']))

        else:     
            model_definition['parameters_pt2'] = '''}'''
            model_definition['likelihood_lambda'] = '''  '''   
            model_definition['likelihood_model_pt1'] = ('''  for (i in 1:N){y[i] ~ bernoulli(%f + (1-%f) ''' 
                            %(options['gamma'], options['gamma']))

        # Combine full model together
        model_definition['full_model'] = (model_definition['data'] + 
                model_definition['parameters_pt1'] + 
                model_definition['parameters_pt2'] +
                model_definition['likelihood_scale'] + 
                model_definition['likelihood_shape'] + 
                model_definition['likelihood_lambda'] + 
                model_definition['likelihood_model_pt1'] + 
                model_definition['likelihood_model_pt2'])

        # Compile model in STAN
        compiled_model = ps.StanModel(model_code = model_definition['full_model']) 
    
    #######################################################################
    #  MODEL_DEFINITION == MANUAL (FULL)
    #######################################################################
    elif options['fit'] in ('manual_full'):
        compiled_model = ps.StanModel(model_code = model_definition) 
    
    return compiled_model
    

#######################################################################
#  FUNCTION THAT GENERATES POSTERIOR FROM MODEL USING STAN
#######################################################################
def modelSample(data, options, model):
    
    # Convert from average to numerical 1 and 0 sequence is provided with MOCS
    df = pd.DataFrame([],columns=['x','y']) 
    for i in range(len(data.x)):
        approx_numsequence = np.round(data.y[i]*data.N[i])   
        response_y = np.zeros(data.N[i])
        response_y[:int(approx_numsequence)] = 1
        response_x = np.repeat(data.x[i],data.N[i])
        tmp_df = pd.DataFrame(np.column_stack((response_x,response_y)), columns=['x','y'])
        df = df.append(tmp_df)

    # Convert data frame above to list 
    x = [float(i) for i in pd.Series.tolist(df.x)]
    y = [int(i) for i in pd.Series.tolist(df.y)]
    
    # Create list to be used as input into the main the sampler
    data_model= {'N': len(df.x),'x': x,'y': y}

    # Generate samples from compiled model 
    sample = model.sampling(data=data_model, iter=options['iter'], chains=options['chains'])
    return sample


#######################################################################
#  EXTRACT PARAMETERS FROM POSTERIOR
#######################################################################
def extractParams(data, options, sample):
    
    # Check arguments provided are numerical for threshold
    if options['param_ests'] not in ('mean'):
        assert False, 'Options provided are not those made available by module. Revise options provided.'
    if isinstance(options['thresholdPC'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["thresholdPC"].'
    if isinstance(options['nAFC'], (int, float, complex)) == False:
        assert False, 'Please provide a numerical argument for options["nAFC"].'
    if options['lapse'] not in (True, False):
        assert False, 'Options provided are not those made available by module. Revise options provided.'        
    if options['sigmoidType'] not in ('cnorm', 'logistic', 'cauchy', 'weibull'):
        assert False, 'Options provided are not those made available by module. Revise options provided.'    

    # Extract summary table
    fit_summary = sample.summary()
    # Extract summary of mean estimates for parameters
    params = pd.DataFrame([fit_summary['summary'][:,0]],columns=fit_summary['summary_rownames'])
    
    # Define lambda based on option
    if options['lapse'] == True:
        lamb = params['lambda'][0]
    elif options['lapse'] == False:
        lamb = 0
    
    # Generate fitted function based on parameters from posterior
    x = np.linspace(data.x.min(),data.x.max(),1000)
    if options['sigmoidType'] == 'cnorm':  
        y_pred = options['gamma'] + (1-lamb-options['gamma'])*sc.stats.norm.cdf(x,params['mu'][0],params['sigma'][0])
    elif options['sigmoidType'] == 'cauchy': 
        y_pred = options['gamma'] + (1-lamb-options['gamma'])*sc.stats.cauchy.cdf(x,params['mu'][0],params['sigma'][0])
    elif options['sigmoidType'] == 'logistic':    
        y_pred = options['gamma'] + (1-lamb-options['gamma'])*(1 / (1 + np.exp(-(x- params['mu'][0])/params['sigma'][0] )))
    elif options['sigmoidType'] == 'weibull':    
        y_pred = options['gamma'] + (1-lamb-options['gamma'])* (1 - np.exp(-((x/params['alpha'][0])**params['beta'][0])))
    
    # Extract estimate of threshold from fitted function
    threshold = np.interp(options['thresholdPC'], y_pred, x)
    
    return params, threshold



#######################################################################
#  GENERATE SUMMARY TABLE FROM DATA INPUT 
#######################################################################

def gen_aggregateData(data):
    
    print('----------------------------------------------')        
    print('''WARNING: 
             Grouping data based on assumption that raw data was provided.
             Change settings through assignment in options.''')
    print('----------------------------------------------')   
    
    # Count the number of corect responses per stim. level
    num_corr_responses = data.groupby('x')['y'].sum()    
    num_corr_responses = num_corr_responses.reset_index() 
    
    # Count number of total stimulus presentations
    num_stim_presentations = data.groupby('x')['y'].count()
    num_stim_presentations = num_stim_presentations.reset_index()      
    
    # Calculate proportion correct per stimulus level         
    prop_correct = num_corr_responses['y'] / num_stim_presentations['y']                     
    prop_correct = prop_correct.reset_index()                        
                    
    # Combine prop_correct series with count to form final data frame
    summary_dat = pd.DataFrame(data = dict({'x':num_corr_responses['x'], 
                                           'y':prop_correct['y'], 
                                           'N':num_stim_presentations['y']}))                                   
        
    return summary_dat
            
    
