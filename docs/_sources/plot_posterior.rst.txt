:mod:`bayesfit.plot_posterior` - Plot posterior surface 
=======================================================

.. py:function:: bayesfit.plot_posterior(metrics)

Input Arguments
---------------

    metrics : dictionary
        Output from *bayesfit.fitmodel* which contains important metrics from the fitted model to the data. (See desciption in :doc:`bayesfit.fitmodel <fitmodel>` for full description of metrics output)

Output Variables
-----------------
    matplotlib.pyplot Object 
    	Plot of posterior surface collapsed across gamma (guess rate) and lambda (lapse rate) parameters. Therefore, the 2D posterior surface reflects probabilities associated with the scale and slope parameters of the psychometric function. 