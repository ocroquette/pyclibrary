# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2015 by PyCLibrary Authors, see AUTHORS for more details.
#
# Distributed under the terms of the MIT/X11 license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Initialisation routines.

Those should be run before creating a CParser and can be run only once. They
are used to declare additional types and modifiers for the parser.

"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)
import sys
from .c_library import CLibrary
from .backends import init_libraries


def init(extra_types=None):
    """Init CLibrary classes.

    Parameters
    ----------
    extra_types : dict, optional
        typeName->c_type pairs to extend typespace.
    extra_modifiers : list, optional
        List of modifiers, such as '__stdcall'.

    """
    if CLibrary._init:
        raise RuntimeError('Can only initialise the parser once')

    init_libraries(extra_types or {})

    CLibrary._init = True


WIN_TYPES = {'__int64': None}


def auto_init(extra_types=None, extra_modifiers=None, os=None):
    """Init CLibrary classes based on the targeted OS.

    Parameters
    ----------
    extra_types : dict, optional
        Extra typeName->c_type pairs to extend typespace.
    extra_modifiers : list, optional
        List of extra modifiers, such as '__stdcall'.
    os : {'win32', 'linux2', 'darwin'}, optional
        OS for which to prepare the system. If not specified sys is used to
        identify the OS.

    """
    extra_types = extra_types if extra_types else {}
    extra_modifiers = extra_modifiers if extra_modifiers else []

    if os == 'win32' or sys.platform == 'win32':
        extra_types.update(WIN_TYPES)

    init(extra_types)
