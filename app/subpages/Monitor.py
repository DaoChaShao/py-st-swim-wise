#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/13 23:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   Monitor.py
# @Desc     :   

from pandas import DataFrame
from streamlit import empty, session_state, stop, data_editor

NOTIFICATIONS = empty()

if "DATA" not in session_state:
    NOTIFICATIONS.warning("Please upload a file first.")
    stop()

data: DataFrame = session_state["DATA"].copy()
