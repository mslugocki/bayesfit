:mod:`bayesfit.plot_psyfcn` - Plot psychometric function 
========================================================

.. py:function:: bayesfit.plot_psyfcn(data, options, metrics, log_xscale = False, scale_pnts = True, estimate_type = 'MAP')

Input Arguments
---------------
    data : Numpy array
        A m-row by 3-column Numpy array corresponding to data from the experiment.

    options : dictionary
        Stores all settings used when fitting the model.

    metrics : dictionary
        Output from *bayesfit.fitmodel* which contains important metrics from the fitted model to the data. (See desciption in :doc:`bayesfit.fitmodel <fitmodel>` for full description of metrics output)

    log_xscale : logical
        Determines whether to log-transform the x-axisl

    scale_pnts : logical
        Scales size of data points by the number of trials each point was sampled.

    estimate_type : str ('MAP' or 'Mean')
		Determines which metric used for parameter estimates.

Output Variables
-----------------
    matplotlib.pyplot Object 
    	Plot of psychometric function using parameters from fitted model. 