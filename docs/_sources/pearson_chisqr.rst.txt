:mod:`bayesfit.pearson_chisqr` - Compute Pearson's Chi-squared 
==============================================================

.. py:function:: bayesfit.pearson_chisqr(data, options, metrics, estimate_type)

Input Arguments
---------------
    data : Numpy array
        A m-row by 3-column Numpy array corresponding to data from the experiment. (See desciption in :doc:`bayesfit.fitmodel <fitmodel>` for full description)

    options : dictionary
        Stores all settings used when fitting the model.

    metrics : dictionary
        Output from *bayesfit.fitmodel* which contains important metrics from the fitted model to the data. (See desciption in :doc:`bayesfit.fitmodel <fitmodel>` for full description of metrics output)

    estimate_type : str ('MAP' or 'Mean')
        Determines which metric used for parameter estimates.

Output Variables
-----------------
    pearson_chisqr : float 
    	Pearson's Chi-squared metric used to assess goodness-of-fit of model.