Bayesian Psychometric Curve Fitting tool 
====================================

.. image:: https://github.com/SlugocM/bayesfit/blob/master/logos/logo.png
    :alt: BayesFit Logo
    :scale: 50 %

|pypi| |coverage|

:Authors:
    Michael Slugocki


--------------------------------------------------

**Special Note from Author:**

[ updated on: 2025/01/07 ]

Given the ever changing landscape of software development, the recent jump from `Numpy 1.x` to `2.x` would require significant modifications to BayesFit to keep up-to-date with major changes that were implemented.

Unfortunately, provided this project is not funded, such ongoing development is simply not practical.  Therefore, modifications have been made to the requirements file to provide an upper limit to the Numpy version supported by BayesFit. 

What this means is to continue to utilize BayesFit without issue, simply create a virtual environment with module versions specified under `requirements.txt` via `pip install -r requirements.txt`, and install BayesFit within that environment.

This also means BayesFit will be frozen at this version number (v2.4.1). Thank you for your continued support, and I hope this software continues to help others in providing a simple Bayesian Curve Fitting Tool.

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

Release 2.4.1:

- **Updated requirements file with upper bound for Numpy (i.e., <= 1.24.4)**

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
