Bayesian Psychometric Curve Fitting tool using PyStan and Stan
====================================

.. image:: https://github.com/SlugocM/bayesfit/blob/master/logos/logo.png
    :alt: BayesFit Logo
    :scale: 50 %

|pypi| |travis|

:Authors:
    Michael Slugocki
   

--------------------------------------------------

**BayesFit** provides a simple and easy to use interface to fit and plot psychometric functions by making use of pystan and Stan, which perform Bayesian inference using the No-U-Turn sampler.  

Important links
---------------
- Use documentation: https://github.com/SlugocM/bayesfit/blob/master/documentation/BayesFit%20Documentation.ipynb
- Source code repository: https://github.com/slugocm/bayesfit
- Issue tracker: https://github.com/slugocm/bayesfit/issues
- For latest update on new version releases, follow me on twitter: https://twitter.com/SlugocM

- pystan documentation: https://pystan.readthedocs.org
- Stan: http://mc-stan.org/
- Stan User's Guide and Reference Manual (pdf) available at http://mc-stan.org


Basic Installation [Linux/ Windows/ macOS]
------------------

**WINDOWS USERS:** 
**PLEASE READ ADDITIONAL INSTALLATION INSTRUCTIONS TO SAVE YOU HEADACHES!**

Packages required (versions specified in requirements.txt): 
`PyStan <http://mc-stan.org/users/interfaces/pystan>`_
`Scipy <https://www.scipy.org/>`_
`Pandas <http://pandas.pydata.org/>`_
`Seaborn <https://seaborn.pydata.org/>`_
`StatsModels <www.statsmodels.org/stable/index.html>`_

To install required packages if the versions are out of date, or not installed in your working environment, first download the **requirements.txt** file in this repository.  Then navigate to the directory that contains the downloaded text file using the command-prompt.  Then type: 

::

   pip install -r requirements.txt

**RECOMMENDED:** BayesFit and required packages may be installed from the `Python Package Index
<https://pypi.python.org/pypi>`_ using ``pip``.

::

   pip install bayesfit

*Not recommended but possible*: Alternatively, if required packages are already installed on your system, BayesFit can be installed via:

::

   git clone --recursive https://github.com/slugocm/bayesfit.git
   cd bayesfit
   python setup.py install


Additional installation instructions [Windows]
------------------
If you have not already, please complete the basic installation step first.

Next, to to the directory where pystan is installed.  For most using the Anaconda Python distribution environment, this will be located along the lines of **.../Anaconda3/Lib/site-packages/pystan/**.  There will be a file within this folder named **model.py**.  Open this file and comment out lines 286-287, from:
::
    if platform.platform().startswith('Win'):
        extra_compile_args = ['/EHsc', '-DBOOST_DATE_TIME_NO_LIB']
to:
::
    # if platform.platform().startswith('Win'):
    #     extra_compile_args = ['/EHsc', '-DBOOST_DATE_TIME_NO_LIB']



Unfortuntely, there are some compiler errors that may arise when running the BayesFit with Python on windows.  These errors mainly arise from pystan, and its requirement for compiling models in C++ code for use with Stan.  Please carefully follow the steps below, and ensure you are using Python version 3.5 or newer. The first steps also make use of Anaconda Python distribution environment. In your command-prompt, or Anaconda prompt type: 

::

    conda install libpython
    conda install -c mysys2 m2w64-toolchain=5.3.0
   
Now under your Anaconda directory go to **.../Anaconda3/Lib/distutils/** folder and see if a file labelled **distutils.cfg** exists.  If not, create such a file under this directory with the following code:

::

    [build]
    compiler=mingw32

Try running the basic demo script now.  If you receive an error along the lines of **"MS VS COMPILER ..."**, please follow this final step. Under the earlier directory **.../Anaconda3/Lib/distutils/** locate a file **cygwinccompiler.py**, and comment out lines: 157; 160; 325.  Save the file, and restart your Python session.  Everything should work now.    


Upgrading BayesFit
------------------

Simply type: 

::

    pip install bayesfit -U


Release Notes
------------------

Release 1.21 (Stable release):

- Fixed issue with the use of floats in vector of stimulus intensities.
- Default value for "chains" parameter now set to 1 to avoid parallel computing issues for Windows users.
- Removed gumbel distribution function until further notice.
- Corrected numerous issues with plotting functions, especially the density plot

.. |pypi| image:: https://badge.fury.io/py/bayesfit.png
    :target: https://badge.fury.io/py/bayesfit
    :alt: pypi version
    
.. |travis| image:: https://travis-ci.org/SlugocM/bayesfit.svg?branch=master
    :target: https://travis-ci.org/SlugocM/bayesfit/
    :alt: travis-ci build status
