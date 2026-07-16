#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/15 16:53
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   prescription.py
# @Desc     :
from openai import api_key
from pandas import DataFrame, Series
from streamlit import (empty, session_state, stop,
                       columns, selectbox, metric, line_chart,
                       sidebar, markdown)

from app.tools import get_injury_risk_status
from utils import BASE_CONFIG, verify_api_key, OpenAITextCompleter, DeepSeekCompleter

NOTIFICATIONS = empty()
DISPLAYER = empty()

if "CALC" not in session_state:
    NOTIFICATIONS.warning("Please upload a file first.")
    stop()

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
    # print(details)

# 1104-21 1183-26
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

line_chart(
    athlete_days,
    x="Day",
    y=["Daily_Load", "Acute_Load", "Chronic_Load"],
    width="stretch",
)

languages: list = ["Chinese", "English"]
language: str | None = sidebar.selectbox(
    "Language",
    languages,
    index=0, width="stretch",
    help="Select a language for the training prescription"
)
role: str = (
    "You are a world-class elite sports scientist and high-performance swim coach. "
    "You excel at analyzing physiological markers alongside training loads to prescribe "
    "precision training adjustments and minimize injury risks."
)

prompt: str = f"""
The data of Athlete {athlete} on Day {day} shows as follows:
- Daily Load: {details['Daily_Load']:.1f} (Duration × Intensity)
- Sleep Duration: {details['Sleep_Duration_Hours']:.1f} hours
- Resting Heart Rate: {details['Resting_Heart_Rate']:.0f} bpm
- HRV: {details['HRV_ms']:.1f} ms
- Recovery Score: {details['Recovery_Score']:.0f}/100
- Acute Load: {details['Acute_Load']:.1f}
- Chronic Load: {details['Chronic_Load']:.1f}
- ACWR: {details['ACWR']:.2f} (Current Status Zone: {get_injury_risk_status(details['ACWR'])})

Based on the sports science data above, please provide a highly professional, concise, and actionable training prescription for today. 
Structure your response strictly into the following 3 sections in {language} using Markdown:

### ⚖️ 1. Status Diagnosis | 状态诊断
Analyze if the athlete's current fatigue (ACWR) aligns with their physiological recovery (HRV, Sleep, Resting HR). State the core issue in one sharp sentence.

### 🏊‍♂️ 2. Training Load Adjustment | 训练负荷调整
Give explicit, quantifiable coaching advice for today's session (e.g., 'Maintain planned load', 'Reduce volume by 30%', 'Active recovery session only', or 'Complete rest').

### 🧘‍♂️ 3. Targeted Recovery Interventions | 目标恢复干预
Recommend 1-2 specific recovery protocols based on their fatigue levels (e.g., cold-water immersion, active stretching, sleep extension).
"""

provider: str = sidebar.selectbox(
    "LLM Service Provider",
    ["OpenAI", "Deepseek"], index=1,
    width="stretch",
    help="Select a LLM service provider"
)
match provider:
    case "OpenAI":
        sidebar.caption("OpenAI service is selected.")
        model: str = sidebar.selectbox(
            "Select an OpenAI model",
            ["gpt-4.1-mini", "gpt-5.4-mini"], index=0,
            disabled=True, width="stretch",
            help="Select a OpenAI LLM model"
        )
        sidebar.caption("The specific OpenAI model has been selected.")
        api_key: str = sidebar.text_input(
            "Enter your OpenAI API key",
            type="password",
            placeholder="sk-xxx",
            help="Enter your OpenAI API key"
        )
    case "Deepseek":
        sidebar.caption("Deepseek service is selected.")
        model: str = sidebar.selectbox(
            "Select a Deepseek model",
            ["deepseek-v4-flash", "deepseek-v4-pro"], index=0,
            disabled=True, width="stretch",
            help="Select a Deepseek LLM model"
        )
        sidebar.caption("The specific Deepseek model has been selected.")
        api_key: str = sidebar.text_input(
            "Enter your Deepseek API key",
            type="password",
            placeholder="sk-xxx",
            help="Enter your Deepseek API key"
        )
    case _:
        sidebar.warning("Please select a valid LLM service provider.")
        model: str | None = None
        api_key: str | None = None

if model and api_key:
    if verify_api_key(api_key, f"{provider.lower()}"):
        NOTIFICATIONS.success(f"{provider} API key is valid and ready to use.")

        if sidebar.button("Generate Training Prescription", type="primary", width="stretch"):
            match provider:
                case "OpenAI":
                    completer = OpenAITextCompleter(api_key)
                    response: str = completer.client(role=role, prompt=prompt, model=model)
                case "Deepseek":
                    completer = DeepSeekCompleter(api_key)
                    response: str = completer.client(role=role, prompt=prompt, model=model)
                case _:
                    NOTIFICATIONS.error("Please select a valid LLM service provider.")
                    response: str | None = None

            if response:
                markdown(response)
    else:
        NOTIFICATIONS.error(f"Invalid {provider} API key.")
