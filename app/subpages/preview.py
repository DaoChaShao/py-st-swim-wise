#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/12 23:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preview.py
# @Desc     :

from pandas import DataFrame
from streamlit import data_editor, multiselect, markdown, columns, metric, empty, session_state
from utils import BASE_CONFIG, load_csv

NOTIFICATIONS = empty()

if "RAW" not in session_state:
    raw: DataFrame = load_csv(BASE_CONFIG.FILE_PATHS.DATA, dis_summary=True)
    session_state["RAW"] = raw

dup_rows: int = session_state["RAW"].duplicated().sum()
miss_values: int = session_state["RAW"].isnull().sum().sum()

# Display Columns: 19
COLS: list = session_state["RAW"].columns.tolist()
# Display selected columns: 12
REST_COLS: list = [
    "Athlete_ID",
    "Day",
    "Day_of_Week",
    "Week",
    "Age",
    "Gender",
    "Training_Duration_Min",
    "Training_Intensity",
    "Sleep_Duration_Hours",
    "Resting_Heart_Rate",
    "HRV_ms",
    "Recovery_Score",
]

left, mid, right = columns(3)
with left:
    metric("Duplicate Rows", dup_rows, help="Number of duplicate rows in the dataset")
with mid:
    metric("Missing Values", miss_values, help="Number of missing values in the dataset")
with right:
    metric("Total Rows", len(session_state["RAW"]), help="Total number of rows in the dataset")

cols: list = multiselect(
    "Select Columns",
    options=COLS, default=REST_COLS,
    width="stretch", placeholder="Select Columns", help="Select the columns to display"
)
markdown("Details", width="stretch")
data_editor(
    session_state["RAW"][cols],
    height=450, width="stretch",
    hide_index=True, disabled=True, placeholder="Data Preview"
)

NOTIFICATIONS.success("Data preview loaded successfully!")
