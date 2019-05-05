# -*- coding: utf-8 -*-
"""Define a flake8 plugin to check for any given regex."""
#
# Distributed under the terms of the MIT license.
#
from __future__ import (
    absolute_import, division, print_function, unicode_literals)

__version__ = '1.0'

import importlib
import os
import sys

sys.path.append(os.getcwd())
CONFIG_MODULE = os.environ.get('FLAKE8_REGEX_CONFIG_MODULE')

PATTERNS_CONFIG = (getattr(importlib.import_module(CONFIG_MODULE), 'rules')
                   if CONFIG_MODULE else None)


def check_regex_patterns(physical_line):
    if PATTERNS_CONFIG:
        for pattern_cfg in PATTERNS_CONFIG:
            match = pattern_cfg['regex'].search(physical_line)
            if match:
                return (match.start(),
                        'R{} {}'.format(pattern_cfg['code'],
                                        pattern_cfg['message']))


check_regex_patterns.name = name = 'flake8-regex'
check_regex_patterns.version = __version__
