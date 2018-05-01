Bayesian Psychometric Curve Fitting tool 
====================================

.. image:: https://github.com/SlugocM/bayesfit/blob/master/logos/logo.png
    :alt: BayesFit Logo
    :scale: 50 %

|pypi| |travis| |coverage|

:Authors:
    Michael Slugocki
   

--------------------------------------------------

NEWS: 

**VERSION 2.0 NOW RELEASED!  PLEASE READ RELEASE NOTES AS SIGNIFICANT CHANGES HAVE BEEN MADE**

Release Notes
------------------

Release 2.0 (noteable mentions):

- **BayeFit has switched from use of pystan to pyMC3. We feel that this module is better suited for our purposes, and also has less overhead for Windows users** 
- Entirely new function for model fitting that does everything in one shot!
- Batch fitting has now been released with greater ease of use. The same function as for fitting a model to a single dataset is used.
- A function to perform the Geweke diagnostic test for convergence of chains has been added.
- Unit tests on all functions have been updated, and a coverage report (badge above) has been posted on the BayesFit read me page.
- Added additional safeguards for using options that are not permitted have been added. 

Link to v2.0 in PyPI archive (https://pypi.org/project/bayesfit/)

--------------------------------------------------

**BayesFit** provides a simple and easy to use interface to fit and plot psychometric functions by making use of PyMC3, which perform Bayesian inference using MCMC sampling.  

Important links
---------------
- Use documentation: https://github.com/SlugocM/bayesfit/blob/master/documentation/bayesfit_documentation.ipynb
- Source code repository: https://github.com/slugocm/bayesfit
- Issue tracker: https://github.com/slugocm/bayesfit/issues
- For latest update on new version releases, follow me on twitter: https://twitter.com/SlugocM

- pyMC3 documentation: https://docs.pymc.io/


Basic Installation [Linux/ Windows/ macOS]
------------------

Packages required (versions specified in requirements.txt): 
`pyMC3 <https://docs.pymc.io/>`_
`Numpy <http://www.numpy.org/>`_
`Matplotlib <https://matplotlib.org/>`_

To install required packages if the versions are out of date, or not installed in your working environment, first download the **requirements.txt** file in this repository.  Then navigate to the directory that contains the downloaded text file using the command-prompt.  Then type: 

::

   pip install -r requirements.txt

**RECOMMENDED:** BayesFit and required packages may be installed from the `Python Package Index
<https://pypi.python.org/pypi>`_ using ``pip``.

::

   pip install bayesfit

Alternatively, if required packages are already installed on your system, BayesFit can be installed via:

::

   git clone --recursive https://github.com/slugocm/bayesfit.git
   cd bayesfit
   python setup.py install


Upgrading BayesFit
------------------

Simply type: 

::

    pip install bayesfit -U


.. |pypi| image:: https://badge.fury.io/py/bayesfit.png
    :target: https://badge.fury.io/py/bayesfit
    :alt: pypi version
    
.. |travis| image:: https://travis-ci.org/SlugocM/bayesfit.svg?branch=master
    :target: https://travis-ci.org/SlugocM/bayesfit/
    :alt: travis-ci build status
    
.. |coverage| image:: https://coveralls.io/repos/github/SlugocM/bayesfit/badge.svg?branch=master
  :target: https://coveralls.io/github/SlugocM/bayesfit?branch=master




