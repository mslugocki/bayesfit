:mod:`bayesfit.deviance` - Compute deviance 
============================================

.. py:function:: bayesfit.deviance(data, options, metrics, estimate_type)

Input Arguments
---------------
    data : Numpy array
        A m-row by 3-column Numpy array corresponding to data from the experiment. 

    options : dictionary
        Stores all settings used when fitting the model.

    metrics : dictionary
        Output from *bayesfit.fitmodel* which contains important metrics from the fitted model to the data. (See desciption in :doc:`bayesfit.fitmodel <fitmodel>` for full description of metrics output)

    estimate_type : str ('MAP' or 'Mean')
        Determines which metric used for parameter estimates.

Output Variables
-----------------
    deviance : float 
    	Deviance metric used to assess goodness-of-fit of model.