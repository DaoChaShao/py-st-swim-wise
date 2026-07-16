#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/12 22:27
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :   

from streamlit import title, expander, caption, empty

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

title("Swim Wise")
with expander("**INTRODUCTION (CN)**", expanded=False):
    caption("+ 📋 **定位**：专为竞技游泳打造的数字化运动负荷监控与伤病预警系统。")
    caption("+ 📊 **预览**：支持多维原始训练日志动态检索，一键审计重复值与缺失项。")
    caption("+ 🧹 **清洗**：智能隔离运动员历史周期，采用前后向填补算法修复破损数据。")
    caption("+ 📈 **监控**：科学构建7/28天急慢性负荷比（ACWR）引擎，动态捕捉伤病红线。")
    caption("+ 🧠 **AI 处方**：融合负荷评级与 HRV 等多维体征，由大模型一键生成智能课表调整建议。")

with expander("**INTRODUCTION (EN)**", expanded=True):
    caption("+ 📋 **Core Value**: An elite sports tech platform designed for swim workload monitoring and injury prevention.")
    caption("+ 📊 **Data Preview**: Dynamic exploration of raw training logs with instant data anomaly auditing.")
    caption("+ 🧹 **Preparation**: Localized athlete grouping with advanced imputation to cure missing tracking metrics.")
    caption("+ 📈 **Load Monitor**: Scientific ACWR framework evaluating rolling acute fatigue against chronic fitness limits.")
    caption("+ 🧠 **AI Prescription**: Fusing workload zones with HRV biomarkers to synthesize precision training adjustments.")
