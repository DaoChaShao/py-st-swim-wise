#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/13 16:46
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preparation.py
# @Desc     :   

from pandas import DataFrame
from streamlit import session_state, stop, empty, data_editor, columns, metric

from app.subpages.preview import miss_values

NOTIFICATIONS = empty()

if "RAW" not in session_state or "REST_COLS" not in session_state:
    NOTIFICATIONS.warning("Please upload a file first or select the columns to rest.")
    stop()

if "DATA" not in session_state:
    data: DataFrame = session_state["RAW"].copy()

    # Sort the data by Athlete_ID and Day
    sorted_data = data.sort_values(by=["Athlete_ID", "Day"])

    # Fill missing values in "Training_Intensity" with the previous or next valid value
    sorted_data["Training_Intensity"] = (
        sorted_data.groupby("Athlete_ID")["Training_Intensity"]
        .ffill()  # Forward fill (use the previous day's value)
        .bfill()  # Backward fill (use the next day's value if the first day is missing)
    )

    # Fill missing values in s"Sleep_Duration_Hours" with the mean value
    sorted_data["Sleep_Duration_Hours"] = (
        sorted_data.groupby("Athlete_ID")["Sleep_Duration_Hours"]
        .transform(lambda x: x.fillna(x.mean()))
    )

    session_state["DATA"] = sorted_data[session_state["REST_COLS"]]

dup_rows: int = session_state["DATA"].duplicated().sum()
miss_values: int = session_state["DATA"].isnull().sum().sum()
left, mid, right = columns(3)
with left:
    metric("Duplicate Rows", dup_rows, help="Number of duplicate rows in the dataset")
with mid:
    metric("Missing Values", miss_values, help="Number of missing values in the dataset")
with right:
    metric("Total Rows", len(session_state["DATA"]), help="Total number of rows in the dataset")

data_editor(
    session_state["DATA"],
    height=600, width="stretch",
    hide_index=True, disabled=True, placeholder="Data Preparation"
)

NOTIFICATIONS.success("Data preparation curated and completed successfully!")
