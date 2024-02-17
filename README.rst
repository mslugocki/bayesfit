Bayesian Psychometric Curve Fitting tool 
====================================

.. image:: https://github.com/SlugocM/bayesfit/blob/master/logos/logo.png
    :alt: BayesFit Logo
    :scale: 50 %

|pypi| |travis| |coverage|

:Authors:
    Michael Slugocki


--------------------------------------------------

**Special Note from Author:**

[ updated on: 2024/02/17 ]

BayesFit now has a brand new website (http://www.bayesfit.org).

Some outstanding issues have been addressed, and a new PYPI version of BayesFit (version 2.4) has been released.  Please update to the latest version to get all the benefits.
 
Kind Regards,  
🌳 M 🌳

--------------------------------------------------

**Citation:**

Slugocki, M., Sekuler, A.B. and Bennett, P., 2019. BayesFit: A tool for modeling psychophysical data using Bayesian inference. *Journal of Open Research Software*, 7(1), p.2. DOI: http://doi.org/10.5334/jors.202

--------------------------------------------------

**API documentation**: http://www.bayesfit.org

--------------------------------------------------

**Issues? Submit a question here**: https://github.com/SlugocM/bayesfit/issues

--------------------------------------------------

Release Notes
------------------

Release 2.4:

- **New dedicated website for API documentation at: www.bayesfit.org**
- Fixed issue with casting to float using numpy

--------------------------------------------------

**BayesFit** provides a simple and easy to use interface to fit and plot psychometric functions using Bayesian inference via numerical integration.

Important links
---------------
- Use documentation: http://www.bayesfit.org
- Source code repository: https://github.com/slugocm/bayesfit
- Issue tracker: https://github.com/slugocm/bayesfit/issues


Basic Installation [Linux/ Windows/ macOS]
------------------

Packages required (versions specified in requirements.txt): 
`Numpy <http://www.numpy.org/>`_
`Matplotlib <https://matplotlib.org/>`_
`Scipy <https://docs.scipy.org/doc/>`_

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
    
.. |coverage| image:: https://coveralls.io/repos/github/SlugocM/bayesfit/badge.svg?branch=master
  :target: https://coveralls.io/github/SlugocM/bayesfit?branch=master
