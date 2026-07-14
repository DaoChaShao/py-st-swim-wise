#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/14 23:29
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   lever.py
# @Desc     :   

from utils import BASE_CONFIG


def get_injury_risk_status(acw_ratio: float) -> str:
    """
    Get injury risk status based on ACWR (Average Cardiovascular Work Ratio)
    :param acw_ratio: Average Cardiovascular Work Ratio
    :return: Injury risk status
    """
    if acw_ratio < BASE_CONFIG.ACWR.UNDER:
        return "Deconditioning Zone"  # Under Training Zone
    elif BASE_CONFIG.ACWR.UNDER <= acw_ratio <= BASE_CONFIG.ACWR.SWEET_SPOT:
        return "Optimal Training Zone"  # Sweet Spot
    elif BASE_CONFIG.ACWR.SWEET_SPOT < acw_ratio < BASE_CONFIG.ACWR.DANGER:
        return "Injury Danger Zone"  # Over-training Zone
    else:
        return "Caution Zone"  # Extreme Danger Training Zone
