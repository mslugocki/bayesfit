"""
*******************************************************
*
*  checkData - CHECK USER PROVIDED DATA
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


#################################################################
#  CHECK DATA STRUCTURE
#################################################################
# Check data structure provided by user
# Format requested is a N x 3 data frame such that [x, y, N]
def check_data(data, batch):
    """Performs a check of the data provided by the user
    to ensure to meets the formatting requirements used by
    Bayesfit

    Keyword arguments:
    data -- m x 3 numpy array
    batch -- specifies whether batch fitting data (logical)
    """
    if batch is False:
        if isinstance(data, np.ndarray) is False:
            raise Exception('Single dataset provided is not of type: np.ndarray. Please change data type provided.') 
        elif isinstance(data, np.ndarray) is True:
            if data.shape[1] != 3:
                raise Exception('Data provided does not contain the number of columns required! (i.e., [x, y, N])')
            for n in data[:,2]:
                if n < 1:
                    raise ValueError('''The number of trials for a stimulus intensity is less than one!''')
    elif batch is True:
        if isinstance(data, dict) is False:
            raise Exception('Batch dataset provided is not of type: dictionary. Please change data type provided.')
        elif isinstance(data, dict) is True:
            for keys in data:
                if data[keys].shape[1] != 3:
                    raise Exception('''A dataset provided in batch does not contain the number of columns required! 
                     (i.e., [x, y, N])''')
                for n in data[keys][:,2]:
                    if n < 1:
                        raise ValueError('''The number of trials for a stimulus intensity is less than one!''')
