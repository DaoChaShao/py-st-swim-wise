#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/12 23:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   display.py
# @Desc     :

from pandas import DataFrame
from streamlit import data_editor
from utils import BASE_CONFIG, load_csv


def main() -> None:
    """ Main Function """
    swimmer: DataFrame = load_csv(BASE_CONFIG.FILE_PATHS.DATA)
    data_editor(swimmer, height=700, width="stretch", hide_index=True, disabled=True, placeholder="Data Preview")


if __name__ == "__main__":
    main()
