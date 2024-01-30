:mod:`bayesfit.bci` - Bayesian Credible Interval (BCI)
=========================================================

.. py:function:: bayesfit.bci(marginal, alpha)

Input Arguments
---------------
    marginal : Numpy array
        A marginal distribution obatined from the metrics dictionary object output after fitting a model to data via the :doc:`bayesfit.fitmodel <fitmodel>` function. 

    alpha : float (limited range: 0 - 1)
        Level of confidence.

Output Variables
-----------------
    lower, upper : float 
    	Upper and lower bounds of Bayesian Credible Interval (BCI) for a marginal distribution given a specified level of confidence.