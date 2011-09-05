#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='south_demos',
      version='0.1',
      packages=find_packages(),
      package_data={'examples': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'south_demos': ['bin/*.pyc']},
      scripts=['examples/bin/manage.py'])
