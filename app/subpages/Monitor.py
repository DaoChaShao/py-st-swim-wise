#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/13 23:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   Monitor.py
# @Desc     :   

from pandas import DataFrame, Series
from streamlit import (empty, session_state, stop,
                       data_editor,
                       selectbox,
                       columns, metric)

from app.tools import get_injury_risk_status
from utils import BASE_CONFIG

NOTIFICATIONS = empty()
DISPLAYER = empty()

if "DATA" not in session_state or "REST_COLS" not in session_state:
    NOTIFICATIONS.warning("Please upload a file first or select the columns to rest.")
    stop()

if "CALC" not in session_state:
    calc_data: DataFrame = session_state["DATA"][session_state["REST_COLS"]].copy()

    # Count the number of days each athlete has recorded because the total data cannot be divided by 28
    days: Series = calc_data.groupby("Athlete_ID")["Day"].count()
    # Find out which athletes have not recorded for 28 days
    incomplete_athletes: Series = days[days < 28]
    print(f"Incomplete athletes:\n{incomplete_athletes}")

    # Calculate Daily Load based on Training Duration and Training Intensity
    calc_data["Daily_Load"]: DataFrame = (calc_data["Training_Duration_Min"] * calc_data["Training_Intensity"])

    # Group daily load by athlete and Daily Training Load (DTL)
    grouped_load = calc_data.groupby("Athlete_ID")["Daily_Load"]
    # Calculate 7-day Acute Training Load (AL or ATL)
    calc_data["Acute_Load"]: DataFrame = grouped_load.transform(lambda x: x.rolling(window=7, min_periods=1).mean())
    # Calculate 28-day Chronic Training Load (CL or CTL)
    calc_data["Chronic_Load"]: DataFrame = grouped_load.transform(lambda x: x.rolling(window=28, min_periods=1).mean())

    # Calculate ACWR（Acute-to-Chronic Workload Ratio | 急慢性训练负荷比）
    calc_data["ACWR"]: DataFrame = calc_data["Acute_Load"] / (calc_data["Chronic_Load"] + 1e-5)

    session_state["CALC"]: DataFrame = calc_data

left, right = columns(2)
with left:
    # Select an athlete to view their data
    athletes: list = sorted(session_state["CALC"]["Athlete_ID"].unique())
    athlete: str = selectbox("1. Select an athlete", athletes, help="Select an athlete to view their data")
    athlete_days: DataFrame = session_state["CALC"][session_state["CALC"]["Athlete_ID"] == athlete].sort_values("Day")
with right:
    # Select a specific day to view ACWR data
    days: list = sorted(athlete_days["Day"].unique())
    day: str = selectbox("2. Select a specific day", days, help="Select a specific day to view ACWR data")
    details: Series = athlete_days[athlete_days["Day"] == day].iloc[0]
    print(details)

    DTL, ATL, CTL, ACWR = DISPLAYER.columns(4)
    with DTL:
        metric(
            "Daily Load",
            f"{details["Daily_Load"]:.2f}",
            help="Daily Training Load (Duration × Intensity)"
        )
    with ATL:
        metric(
            "Acute Load",
            f"{details["Acute_Load"]:.2f}",
            help="Acute Training Load (7-day rolling average)"
        )
    with CTL:
        metric(
            "Chronic Load",
            f"{details["Chronic_Load"]:.2f}",
            help="Chronic Training Load (28-day rolling average)"
        )
    with ACWR:
        metric(
            "ACWR",
            f"{details["ACWR"]:.2f}",
            delta=get_injury_risk_status(details["ACWR"]),
            delta_color="off" if details["ACWR"] <= BASE_CONFIG.ACWR.SWEET_SPOT else "inverse",
            help="Acute-to-Chronic Workload Ratio (Acute Load / Chronic Load)"
        )

data_editor(
    athlete_days,
    height=600, width="stretch",
    hide_index=True, disabled=True, placeholder="Data Preparation"
)

NOTIFICATIONS.success("Data has been calculated and displayed as follows:")
