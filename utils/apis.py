#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/7/15 16:28
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   apis.py
# @Desc     :   

from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam


class DeepSeekCompleter(object):
    """ DeepSeek Completer API Wrapper """

    def __init__(self, api_key: str, temperature: float = 0.7) -> None:
        """
        Initialise the DeepSeek Completer API
        :param api_key: str: The API key for the DeepSeek API
        :param temperature: float: The temperature for the completion
        """
        self._api_key = api_key
        self._temperature = temperature

    def client(self, role: str, prompt: str, model: str = "deepseek-chat") -> str:
        """
        Initialise the DeepSeek Completion API
        :param role: str: The input text to be completed
        :param prompt: str: The prompt to complete the input text
        :param model: str: The model to use for the completion, default is "deepseek-chat-3.5"
        :return: str: The completed text
        """
        client = OpenAI(api_key=self._api_key, base_url="https://api.deepseek.com")

        messages = [
            ChatCompletionSystemMessageParam(
                role="system",
                content=role
            ),
            ChatCompletionUserMessageParam(
                role="user",
                content=prompt
            )
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=self._temperature,
            stream=False
        )

        return response.choices[0].message.content
