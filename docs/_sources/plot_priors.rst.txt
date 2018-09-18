:mod:`bayesfit.plot_priors` - Plot prior distributions 
======================================================

.. py:function:: bayesfit.plot_priors(options, metrics)

Input Arguments
---------------

    options : dictionary
        Stores all settings used when fitting the model.

    metrics : dictionary
        Output from *bayesfit.fitmodel* which contains important metrics from the fitted model to the data. (See desciption in :doc:`bayesfit.fitmodel <fitmodel>` for full description of metrics output)

Output Variables
-----------------
    matplotlib.pyplot Object 
    	Plot of prior distributions defined by user used in fitting procedure. 