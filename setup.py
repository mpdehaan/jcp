#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

setup(name='tcopy',
      version="0.0.11",
      description='Template aware copy tool.',
      author='Michael DeHaan',
      author_email='michael.dehaan@gmail.com',
      url='http://github.com/mpdehaan/tcopy/',
      license='Apache2',
      install_requires=['jinja2'],
      package_dir={ '': 'lib' },
      packages=find_packages('lib'),
      classifiers=[
      ],
      scripts=[
         'scripts/tcopy',
      ],
      data_files=[
      ],
)

