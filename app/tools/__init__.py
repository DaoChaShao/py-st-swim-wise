#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/12 22:15
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :   

"""
****************************************************************
Tools for Streamlit Application
----------------------------------------------------------------
A collection of utility tools designed for Streamlit page initialisation and core function execution.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .layout import config_page, set_pages
from .lever import get_injury_risk_status

__all__ = [
    "config_page",
    "set_pages",

    "get_injury_risk_status"
]
