"""
*******************************************************
*
*  checkParams - CHECK USER PROVIDED ESTIMATES FOR PARAMETERS
*
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   April 14, 2018
*  Last updated: April 18, 2018
*
*******************************************************
"""

#################################################################
#  IMPORT MODULES
#################################################################
import numpy as np


#################################################################
#  CHECK PARAMETERS ESTIMATES PROVIDED
#################################################################
def check_params(data, param_ests, nafc, batch):
    if param_ests is not None:
        # Check whether the variable for the parameter estimates provided is of type list
        if isinstance(param_ests, list) is False:
            raise Exception('''User Error: Please provide a argument of type list for the 
            parameter estimates of the model.''')
        # Check whether arguments in list are of type integer or float
        for i in param_ests:
            if isinstance(i, (int, float)) is False:
                raise Exception('''User Error: Please provide numerical values for parameter '
                                estimates of the model.''')
        # Check number of arguments provided and set the remaining arguments to default values.
        if len(param_ests) < 2:
            raise Exception('''User Error: Please provide at least two estimates (alpha; beta) 
                            for parameters of the model.''')
        elif len(param_ests) == 2:
            print('Setting parameter estimates for gamma and lambda to default values!')
            param_ests.append(1/nafc)
            param_ests.append(0)
        elif len(param_ests) == 3:
            print('Setting parameter estimates for lambda to default value!')
            param_ests.append(0)
        elif len(param_ests) > 4:
            raise Exception('''User Error: More than 4 estimates for parameters of the model provided!''')
    elif param_ests is None:
        # Get initial estimate of alpha via linear regression
        def _scale_est(data):
            x = [data[0, 0], data[len(data) - 1, 0]]
            y = [data[0, 1], data[len(data) - 1, 1]]
            init_scale = np.polyfit(x, y, 1)
            scale_estimate = [(0.70 - init_scale[1]) / init_scale[0]]
            return scale_estimate[0]
        # Guess value to use for scale parameter
        if batch is False:
            scale_guess = _scale_est(data)
        elif batch is True:
            scale_guess = 1
        # Set initial parameter estimates
        # default: alpha = lin_guess; beta = 1; gamma = 1/nAFC; lambda = 0)
        param_ests = [scale_guess, 3, 1/nafc, 0]

    return param_ests


#################################################################
#  CHECK PARAMETER CONSTRAINTS PROVIDED
#################################################################
def check_constraints(param_constraints):
    if param_constraints is None:
        # If no parameter constraints provided, set default values to
        # [alpha = True, beta = True, gamma = False, lambda = True]
        param_constraints = [True, True, False, True]
    elif param_constraints is not None:
        # Check whether the variable for the parameter constraints provided is of type list
        if isinstance(param_constraints, list) is False:
            raise Exception('''User Error: Please provide a argument of type list for the 
            parameter constraints of the model.''')
        # Check whether arguments in list are of type boolean
        for i in param_constraints:
            if isinstance(i, bool) is False:
                raise Exception('''User Error: Please provide boolean arguments for parameter '
                                constraints of the model.''')
            # Check number of arguments provided and set the remaining arguments to default values.
            if len(param_constraints) < 2:
                raise Exception('''User Error: Please provide at least two constraints (alpha; beta) 
                                for parameters of the model.''')
            elif len(param_constraints) == 2:
                print('Setting parameter constraints for gamma and lambda to default values!')
                param_constraints.append(False)
                param_constraints.append(True)
            elif len(param_constraints) == 3:
                print('Setting parameter constraints for lambda to default value!')
                param_constraints.append(True)
            elif len(param_constraints) > 4:
                raise Exception('''User Error: More than 4 constraints for parameters of the model provided!''')
    return param_constraints
