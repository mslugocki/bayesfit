:mod:`bayesfit.fitmodel` - Main function used to fit models
============================================================

.. py:function:: bayesfit.fitmodel(data, batch = False, logspace = False, nafc = 2, sigmoid_type = 'logistic', param_ests = None, param_free = None, priors = None, threshold = 0.75, density = 100)

Input Arguments
---------------
    data : Numpy array
        A m-row by 3-column Numpy array corresponding to data from the experiment,
        whereby columns are organized according to: 
            ==================   ================  ==============
            Stimulus intensity   N-trials correct  N-trials total
            ==================   ================  ==============
                    ...                 ...                 ...
            ==================   ================  ==============

    batch : logical (True/False)
        Specifies whether data provided meant to be batch fit. By default, this options is set to *False*, which assumes that the user has provided a single Numpy array with data that they would like to fit a single model. If this options is set to *True*, then the same model options will be fit to all datasets with the exception of initial parameter estimates. If batch fitting data, be sure to provide BayesFit with a dictionary that contains multiple datasets, such that each dataset has its own key. For more information on how to batch fit data using BayesFit, see usage tutorial for batch fitting under home directory.

    logspace : logical (True/False)
        Informs BayesFit whether the intensities provided need to be logspaced. By default, BayesFit will attempt to logspace values for Weibull and Log-Quick functions. Therefore, if your intensities are already logspaced, and you are fitting one of these function, set this options to False. Otherwise, omit this argument, or set to None. If you are certain you would like to logspace your intensities despite what function you fit, set this argument to True.

    nafc : int (range limited: 1 - 10)
        Number of alternative options provided to observer when making a judgment during the experiment. By default, BayesFit assumes a 2AFC design, such that observers have two choices that they can make for their response. This argument is important in fixing the guess rate when fitting a psychometric function to data. 

    sigmoid_type : str 
        Defines what sigmoid function to use in modelling an observer's response given a stimulus intensity. By default, a logistic function is used in fitting a model to data. However, if uncertain as to which function to use, it is best to fit serveral different sigmoid types to data and perform comparisons between fits to see which function should be used in modelling an observer's response

        Functions available include: 

            **'norm'** - Cumulative Normal 

            **'logistic'** - Logistic 

            **'weibull'** - Weibull

            **'quick'** - Quick

            **'quick-log'** - Log-Quick

            **'gumbel'** - Gumbel

            **'hyperbolic'** - Hyperbolic secant

    param_ests : list of float or NoneType (length = 4) [scale, slope, gamma, lambda]
        A list of parameter estimates for the four parameters that define a psychometric function.

        This include parameters that control the scale and slope (usually alpha and beta), which are typically denoted as alpha and beta. Gamma is the guess rate (usually 1/nafc). Lambda is the lapse rate, as sometimes observers get stimulus intensities of large magnitude incorrect for various reasons not associated with their perception of the stimulus iteself. 

        If this argument is provided, the list must be of length 4. By default, both the scale and slope parameters will be estimated via least-squares. Gamma by default is assigned as 1/nafc. Lambda by default is set close to zero (0.001).

        **Important: When providing this argument, any estimate given that is not labelled as a free parameter via the** *param_free* **list as described below will be treated as a fixed value during the fitting procedure.**

        **If you do not have a reasonable estimate in mind for a parameter that is to be estimated, please set the estimate to NoneType for that parameter.**

    param_free : list of logicals or NoneType (length = 4) [scale, slope, gamma, lambda]
        A list indicating which parameters should be estimated versus which values should remain fixed. For example, if a parameter estimate was provided for lambda, and the param_free for lambda is set to False, the parameter estimate specified will remain fixed at that value specified. 

    priors : list of strings or NoneType (length = 4) [scale, slope, gamma, lambda]
        A list where each argument defines prior distributions to use for each parameter of psychometric function. It is encouraged to specify priors for each parameter when you have some knowledge about the data, but be cautious as to what distribution, and values, you choose. Choosing inappropriate arguments can lead to poor estimates. By default, each argument is set to NoneType, and therefore is equivalent to performing maximum likelihood estimation.

        Formatting must follow: **'distribution_name(loc_val, var_val)'**

        List of available prior distributions include:

        **'Unif(a,b)'** - Uniform

        **'Norm(a,b)'** - Normal 

        **'Log-Norm(a,b)'** - Log-normal 

        **'Beta(a,b)'** - Beta

        **'Gamma(a,b)'** - Gamma

        Example of usage: 
        ['Unif(1,10)', 'Norm(5,2)', None, None]

    threshold : float (range limited: 0 - 1)
        Value of proportion correct response to define threshold. This will influence what threshold value is returned in the metrics['threshold'] variable that is output by BayesFit upon completion of the fitting procedure.

    density : int
        Determines the density of the grid used to compute the posterior surface over. If this value is too large, may take a long time to compute. 


Output Variables
-----------------

    options : dictionary
        Dictionary containing all the settings used when fitting the model.

    metrics : dictionary
        A dictionary containing important metrics associated with fitting the model to the data.  These metrics include: 

        * MAP - Maximum a posteriori estimates

        * Mean - Mean estimates

        * BCI - Bayesian Credible Interval (BCI)

        * HPDI - Highest Posterior Density Interval

        * SD - Standard deviation

        * Deviance

        * Pearson's Chi-square

        * Posterior 

        * Mrginals - Marginals distributions

        * Marginals_X - Values over which Marginals are computed over
