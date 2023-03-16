import os
import re
import sys
from pathlib import Path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Reddit REST Wrapper',
    author='Jie Jenn',
    author_email='jiejenn@learndataanalysis.org',
    version='1.0.1',
    keywords=['reddit', 'reddit api'],
    python_requires='>=3.6',
    install_requires=['requests'],
    packages=['red'],
    license='MIT'
)    