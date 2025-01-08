"""
*******************************************************
*
*  BayesFit - SETUP FILE
*  
*  Version:      Version 2.4.1
*  License:      Apache 2.0
*  Written by:   Michael Slugocki
*  Created on:   September, 2017
*  Last updated: January 07, 2025
*
*******************************************************
"""

from setuptools import setup

setup(name='bayesfit',
      version='2.4.1',
      description='Bayesian Psychometric Curve Fitting Module',
      long_description=open('README.rst').read(),
      long_description_content_type='text/markdown',
      url='http://github.com/slugocm/BayesFit',
      author='Michael Slugocki',
      author_email='slugocm@gmail.com',
      license='Apache 2.0',
      packages=['bayesfit'],
      install_requires=['numpy', 
                        'scipy', 
                        'matplotlib'],
      zip_safe=False)