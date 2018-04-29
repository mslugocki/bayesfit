"""
*******************************************************
*
*  test_checkData - UNIT TEST FOR TRAVIS CI
*  
*  Version:      Version 2.0
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September, 2017
*  Last updated: April 28, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES 
#################################################################
import numpy as np
import bayesfit as bf


#################################################################
#  DEFINE FUNCTIONS USED FOR UNIT TESTING
#################################################################

def _batch_false(error):    
    # Test cases for batch equal False 
    batch = False    
    # Generate dataset 
    x = [0.1, 0.21, 0.33, 0.44, 0.55, 0.66, 0.78, 0.9]
    y = [0.48, 0.47, 0.53, 0.55, 0.73, 0.83, 0.97, 0.96] 
    N = [100, 100, 100, 100, 100, 100, 100, 100]
    # Run through possible error types
    if error == 1:
        data = dict()
    elif error == 2:
        data = np.array([x, y]).T
    elif error == 3:
        y[0] = -0.1
        data = np.array([x, y, N]).T
    elif error == 4:
        data = np.array([x, y, N]).T
    # Call function with arguments above
    check_data(data, batch)
    # If working, should not make it to flag
    flag = 1
    return flag



def _normal():
    # Generate test data 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.01, 0.08, 0.2, 0.45, 0.75, 0.89, 0.98]
    N = [20, 20, 20, 20, 20, 20, 20]
    data = pd.DataFrame({'x':x, 'y':y, 'N':N})
    # Initialize options variable as dictionary type
    options = dict()
    # Determines the value of gamma (guess rate) to which the function is fit (default = 2)
    options['nAFC'] = 0
    # Define function
    options['sigmoidType'] = 'cnorm'
    # Define lapse rate
    options['lapse'] = True
    # Define fit 
    options['fit'] = 'auto'
    # Build model 
    model, sample, options = bf.bayesfit(data, options)
    # Extract parameters
    params, threshold = bf.extractParams(data, options, sample)
    # Determine success
    success = 1
    return success

def _logistic():
    # Generate test data 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.01, 0.08, 0.2, 0.45, 0.75, 0.89, 0.98]
    N = [20, 20, 20, 20, 20, 20, 20]
    data = pd.DataFrame({'x':x, 'y':y, 'N':N})
    # Initialize options variable as dictionary type
    options = dict()
    # Determines the value of gamma (guess rate) to which the function is fit (default = 2)
    options['nAFC'] = 0
    # Define function
    options['sigmoidType'] = 'logistic'
    # Define lapse rate
    options['lapse'] = True
    # Define fit 
    options['fit'] = 'auto'
    # Build model 
    model, sample, options = bf.bayesfit(data, options)
    # Extract parameters
    params, threshold = bf.extractParams(data, options, sample)
    # Determine success
    success = 1
    return success

def _cauchy():
    # Generate test data 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.01, 0.08, 0.2, 0.45, 0.75, 0.89, 0.98]
    N = [20, 20, 20, 20, 20, 20, 20]
    data = pd.DataFrame({'x':x, 'y':y, 'N':N})
    # Initialize options variable as dictionary type
    options = dict()
    # Determines the value of gamma (guess rate) to which the function is fit (default = 2)
    options['nAFC'] = 0
    # Define function
    options['sigmoidType'] = 'cauchy'
    # Define lapse rate
    options['lapse'] = True
    # Define fit 
    options['fit'] = 'auto'
    # Build model 
    model, sample, options = bf.bayesfit(data, options)
    # Extract parameters
    params, threshold = bf.extractParams(data, options, sample)
    # Determine success
    success = 1
    return success

def _weibull():
    # Generate test data 
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.01, 0.08, 0.2, 0.45, 0.75, 0.89, 0.98]
    N = [20, 20, 20, 20, 20, 20, 20]
    data = pd.DataFrame({'x':x, 'y':y, 'N':N})
    # Initialize options variable as dictionary type
    options = dict()
    # Determines the value of gamma (guess rate) to which the function is fit (default = 2)
    options['nAFC'] = 0
    # Define function
    options['sigmoidType'] = 'weibull'
    # Define lapse rate
    options['lapse'] = True
    # Define fit 
    options['fit'] = 'auto'
    # Build model 
    model, sample, options = bf.bayesfit(data, options)
    # Extract parameters
    params, threshold = bf.extractParams(data, options, sample)
    # Determine success
    success = 1
    return success



def test_batch_false():
    flag = 0
    flag = _batch_false()
    assert flag == 0

def test_logistic():
    assert _logistic() == 1
    
def test_cauchy():
    assert _cauchy() == 1
    
def test_weibull():
    assert _weibull() == 1
