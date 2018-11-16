"""
*******************************************************
*
*  BayesFit - SETUP FILE
*  
*  Version:      Version 2.2
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September, 2017
*  Last updated: September 18, 2018
*
*******************************************************
"""

from setuptools import setup

setup(name='bayesfit',
      version='2.3',
      description='Bayesian Psychometric Curve Fitting Module',
      url='http://github.com/slugocm/BayesFit',
      author='Michael Slugocki',
      author_email='slugocm@mcmaster.ca',
      license='Apache 2.0',
      packages=['bayesfit'],
      install_requires=['numpy', 'scipy', 'matplotlib'],
      zip_safe=False)



