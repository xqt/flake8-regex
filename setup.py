# -*- coding: utf-8 -*-
"""Arbitrary regex checker, extension for flake8."""
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, print_function, unicode_literals
from setuptools import setup
from flake8_regex import __version__ as version

def get_long_description():
    descr = []
    for fname in ('README.md',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)

setup(
    name='flake8-regex',
    license='MIT License',
    version=version,
    description='Arbitrary regex checker, extension for flake8',
    long_description=get_long_description(),
    keywords=('flake8', 'regex'),
    author='Aristide Niyungeko',
    author_email='aristide.niyungeko@gmail.com',
    url='https://github.com/aristiden7o/flake8-regex',
    python_requires='>=2.7.4, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    py_modules=['flake8_regex'],
    install_requires=['flake8 >= 3.6.0'],
    entry_points={
        'flake8.extension': [
            'R = flake8_regex:check_regex_patterns',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Utilities',
    ],
)
