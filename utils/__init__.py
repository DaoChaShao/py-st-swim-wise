#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/12 22:28
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :   

"""
****************************************************************
Utility Module - Comprehensive Toolkit
----------------------------------------------------------------
This module provides a comprehensive suite of utility functions
and classes designed for general data processing tasks.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .decorator import beautifier, timer
from .helper import (Beautifier, Timer,
                     RandomSeedForGeneral,
                     read_file, read_files)
from .highlighter import (black, red, green, yellow, blue, purple, cyan, white,
                          bold, underline, invert, strikethrough,
                          starts, lines, sharps)
from .stats import (RandomSeedForNumpy,
                    load_csv, summary_dataframe)

__all__ = [
    "beautifier",
    "timer",

    "Beautifier",
    "Timer",
    "RandomSeedForGeneral",
    "read_file",
    "read_files",

    "black", "red", "green", "yellow", "blue", "purple", "cyan", "white",
    "bold", "underline", "invert", "strikethrough",
    "starts", "lines", "sharps",

    "RandomSeedForNumpy",
    "load_csv",
    "summary_dataframe"
]
