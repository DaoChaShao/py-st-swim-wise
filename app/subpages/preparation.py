#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/13 16:46
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preparation.py
# @Desc     :   

from streamlit import session_state, empty, data_editor

NOTIFICATIONS = empty()

if "RAW" not in session_state:
    NOTIFICATIONS.warning("Please upload a file first!")

if "DATA" not in session_state:
    session_state["DATA"] = session_state["RAW"].copy()

data_editor(
    session_state["DATA"],
    height=600, width="stretch",
    hide_index=True, disabled=True, placeholder="Data Preparation"
)

NOTIFICATIONS.success("Data preparation curated and completed successfully!")
