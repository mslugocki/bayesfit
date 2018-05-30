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

**VERSION 2.2 NOW RELEASED!**

Release Notes
------------------

Release 2.2 (noteable mentions):

- Added ability to define priors for each parameter of model
- Altered default priors to promote efficient sampling of posterior

Link to v2.2 in PyPI archive (https://pypi.org/project/bayesfit/)

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




