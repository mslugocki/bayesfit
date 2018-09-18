:mod:`bayesfit.plot_marginals` - Plot marginal distributions 
==============================================================

.. py:function:: bayesfit.plot_marginals(metrics)

Input Arguments
---------------

    metrics : dictionary
        Output from *bayesfit.fitmodel* which contains important metrics from the fitted model to the data. (See desciption in :doc:`bayesfit.fitmodel <fitmodel>` for full description of metrics output)

Output Variables
-----------------
    matplotlib.pyplot Object 
    	Plot of marginal distributions for each parameter as computed from posterior surface. 