"""
*******************************************************
*
*  checkParams - CHECK USER PROVIDED ESTIMATES FOR PARAMETERS
*
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 14, 2018
*  Last updated: September 13, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np
from .psyFunction import psyfunction as _psyfunction
from scipy.optimize import curve_fit
import warnings


#################################################################
#  COMPUTE ESTIMATES FOR SCALE/SLOPE PARAMETERS
#################################################################
def _param_guess(data, nafc, sigmoid_type):
    """Generate initial estimate for parameters governing 
    scale and slope of sigmoidal function.

    Keyword arguments:
    data -- m x 3 numpy array
    nafc -- N-alternative forced choice experiment (integer)
    sigmoid_type -- sigmoid type fit to data (string)
    """
    # Wrapper function to avoid errors with passing sigmoid type defintion
    # to curve fit function
    def wrapper_fnc(x,scale,slope):
        return _psyfunction(x, scale, slope, 1/nafc, 0.001, sigmoid_type)

    # Fit quick function to estimate scale and slope
    param_est = curve_fit(wrapper_fnc, data[:,0], data[:,1]/data[:,2])
    
    # If initial estimates fail, try brute force method
    if param_est[0][0] != param_est[0][0]:
        warnings.warn('''Initial estimation of parameters failed. Now using brute method to try and compute initial estimates. Sit tight!''')
        
    counter = 0
    while param_est[0][0] != param_est[0][0]:
        scale_guess = (data[:,0].min() + data[:,0].max()) / 2
        slope_guess = np.linspace(-200,1000,1000)
        p0 = [scale_guess, slope_guess[counter]]
        param_est = curve_fit(wrapper_fnc, data[:,0], data[:,1]/data[:,2], p0)
        counter += 1
        
        if counter == 999:
            raise Exception('''Initial parameter estimates could not be generated!
                            While this error can arise for a number of reasons.
                            Please see API for more details.''')
    
    return param_est[0]
    

#################################################################
#  CHECK PARAMETERS ESTIMATES PROVIDED
#################################################################
def check_params(data, param_ests, nafc, batch, sigmoid_type):
    """Performs that initial parameter estimates provided 
    by user is in proper format, and assigns default values 
    where necessary.

    Keyword arguments:
    data -- m x 3 numpy array
    param_ests -- list of user specified initial parameter estimates (list)
    nafc -- N-alternative forced choice experiment (integer)
    batch -- specifies whether batch fitting data (logical)
    sigmoid_type -- sigmoid type fit to data (string)
    """
    if param_ests is not None:
        # If batch, param_ests needs to be set to None to auto generate
        # values 
        if batch is True:
            raise Warning('''Warning: User cannot provide estimates for 
                            parameters when Batch options set to TRUE!''')
        # Check whether the variable for the parameter estimates provided is of type list
        if isinstance(param_ests, list) is False:
            raise ValueError('''User Error: Please provide a argument of type list for the 
            parameter estimates of the model.''')
        # Check number of arguments provided
        if len(param_ests) < 4:
            raise ValueError('''User Error: Please provide a list of four parameter
                            estimates for the model. Set estimate to NoneType if
                            want BayesFit to generate estimate for a parameter.''')
        elif len(param_ests) > 4:
            raise ValueError('''User Error: More than 4 estimates for parameters of the model provided!''')
        # Generate value estimates for initialization to fill in those not 
        # provided
        param_initial = [0, 0, 0, 0]
        param_guess = _param_guess(data, nafc, sigmoid_type)
        scale_guess = param_guess[0]
        slope_guess = param_guess[1]
        gamma_guess = 1/nafc
        lambda_guess = 0.001
        param_tmp = [scale_guess, slope_guess, gamma_guess, lambda_guess]
        # Check whether arguments in list are of type integer or float
        NoneType = type(None)
        for i in range(0,4):
            if isinstance(param_ests[i], (int, float, NoneType)) is False:
                raise ValueError('''User Error: Please provide numerical values or NoneType 
                                 for parameter estimates of the model.''')
            # Assign default value as needed
            if param_ests[i] is None:
                param_initial[i] = param_tmp[i]
                print('Setting parameter estimates for %s to default value!')
            elif param_ests[i] is not None:
                param_initial[i] = param_ests[i]
    elif param_ests is None:
        # Get initial estimate of scale and slope
        if batch is False:
            param_guess = _param_guess(data, nafc, sigmoid_type)
            scale_guess = param_guess[0]
            slope_guess = param_guess[1]
            gamma_guess = 1/nafc
            lambda_guess = 0.001
        elif batch is True:
            # Iterate over datasets in dictionary and generate scale estimate
            # for each set
            scale_guess = dict()
            slope_guess = dict()
            gamma_guess = dict()
            lambda_guess = dict()
            for n_datasets in data:
                param_guess = _param_guess(data[n_datasets], nafc, sigmoid_type)
                scale_guess[n_datasets] = param_guess[0]
                slope_guess[n_datasets] = param_guess[1]           
                gamma_guess[n_datasets] = 1/nafc
                lambda_guess[n_datasets] = 0.001
        # Set initial parameter estimates
        param_initial = [scale_guess, slope_guess, gamma_guess, lambda_guess]

    return param_initial


#################################################################
#  CHECK WHICH PARAMETERS ARE FREE (1) VERSUS FIXED (0) 
#################################################################
def check_constraints(param_constraints):
    """Checks whether user provided list specifying which parameters 
    are to be free versus fixed is in proper format, and assigns
    default values where necessary.
    
    Keyword arguments:
    param_constraints -- specifies which parameters to estimate (list)
    """
    if param_constraints is None:
        # If no parameter constraints provided, set default values to
        # [alpha = True, beta = True, gamma = False, lambda = True]
        param_constraints = [True, True, False, False]
    elif param_constraints is not None:
        # Check whether the variable for the parameter constraints provided is of type list
        if isinstance(param_constraints, list) is False:
            raise ValueError('''User Error: Please provide a argument of type list indicating
            which parameters of the model are free (i.e., TRUE) versus fixed (i.e., FALSE).''')
        # Check whether arguments in list are of type boolean
        for i in param_constraints:
            if isinstance(i, bool) is False:
                raise ValueError('''User Error: Please provide boolean arguments for parameter '
                                constraints (i.e., free vs fixed) of the model.''')
            # Check number of arguments provided and set the remaining arguments to default values.
            if len(param_constraints) < 2:
                raise ValueError('''User Error: Please provide at least two constraints (scale; slope)
                                for parameters of the model.''')
            elif len(param_constraints) == 2:
                print('Setting parameter constraints for gamma and lambda to default values (i.e., fixed)!')
                param_constraints.append(False)
                param_constraints.append(True)
            elif len(param_constraints) == 3:
                print('Setting parameter constraints for lambda to default value (i.e., fixed)!')
                param_constraints.append(True)
            elif len(param_constraints) > 4:
                raise ValueError('''User Error: More than 4 constraints for parameters of the model provided!''')
    return param_constraints
