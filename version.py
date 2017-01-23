#!/usr/bin/env python

import os
import sys
import types

from warnings import warn

PYTHON_VERSION = sys.version_info[:3]

versions_required_message = """
Pybib is not available on:
%s

Pybib only supported under 3.3+
"""


def python_is_supported():
    return (PYTHON_VERSION >= (3, 3, 0))

if not python_is_supported():
    print(versions_required_message % sys.version)
    sys.exit(1)
