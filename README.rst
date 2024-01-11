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

[ updated on: 2024/01/10 ]

Hello BayesFitters!

Excited to announce that I will be revamping Bayesfit in the coming weeks / months ahead 🥳  Also, to celebrate this event, I purchased the domain **bayesfit.org** to provide a stable resource for managing documentation, as well as providing more in-depth updates for those folks who are interested.

Please stay tuned, and thank you for using BayesFit. Your feedback is always appreciated.
 
Kind Regards,  
🌳 M 🌳

--------------------------------------------------

**Citation:**

Slugocki, M., Sekuler, A.B. and Bennett, P., 2019. BayesFit: A tool for modeling psychophysical data using Bayesian inference. *Journal of Open Research Software*, 7(1), p.2. DOI: http://doi.org/10.5334/jors.202

--------------------------------------------------

🚧 under construction: currently moving API documentation to bayesfit.org 🚧

**API documentation**: http://www.slugocm.ca/bayesfit/

--------------------------------------------------

**Issues? Submit a question here**: https://github.com/SlugocM/bayesfit/issues

--------------------------------------------------

NEWS: 

An article on BayesFit has now been published in the Journal of Open Research Software!  See: http://doi.org/10.5334/jors.202 


Release Notes
------------------

Release 2.3 (noteable mentions):

- **Now uses numerical integration to avoid convergence errors**
- Removed PyMC3 dependency 
- Mulitple new functions have been written for fitting, plotting, and extracting metrics
- **Full API documentation now available** 

--------------------------------------------------

**BayesFit** provides a simple and easy to use interface to fit and plot psychometric functions using Bayesian inference via numerical integration.

Important links
---------------
- Use documentation: http://www.slugocm.ca/bayesfit/
- Source code repository: https://github.com/slugocm/bayesfit
- Issue tracker: https://github.com/slugocm/bayesfit/issues
- For latest update on new version releases, follow me on twitter: https://twitter.com/SlugocM


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
    
.. |travis| image:: https://travis-ci.org/SlugocM/bayesfit.svg?branch=master
    :target: https://travis-ci.org/SlugocM/bayesfit/
    :alt: travis-ci build status
    
.. |coverage| image:: https://coveralls.io/repos/github/SlugocM/bayesfit/badge.svg?branch=master
  :target: https://coveralls.io/github/SlugocM/bayesfit?branch=master




