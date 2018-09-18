:mod:`bayesfit.get_threshold` - Extract threshold from fitted model
===================================================================

.. py:function:: bayesfit.get_threshold(data, metrics, options, threshold_pc, estimate_type = 'MAP')

Input Arguments
---------------
    data : Numpy array
        A m-row by 3-column Numpy array corresponding to data from the experiment. 
        
    options : dictionary
        Stores all settings used when fitting the model.

    metrics : dictionary
        Output from *bayesfit.fitmodel* which contains important metrics from the fitted model to the data. (See desciption in :doc:`bayesfit.fitmodel <fitmodel>` for full description of metrics output)

    threshold_pc : float (range limited: 0 - 1)
        Value of proportion correct response to define threshold. This will influence what threshold value is returned in the metrics['threshold'] variable that is output by BayesFit upon completion of the fitting procedure.

    estimate_type : str ('MAP' or 'Mean')
		What estimate to use for free parameters when extracting threshold from fitted model.

Output Variables
-----------------
    threshold : float
    	Threshold at specified point along fitted psychometric function based on specified proportion correct response from input argument. 
