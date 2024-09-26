"""Run this model in Python

> pip install openai
"""
import os
from openai import OpenAI


class openai_api_response:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "GITHUB_TOKEN": ("STRING", {"multiline": False}),
            "message": ("STRING", {"multiline": False}),
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "response_and_message"
    CATEGORY = "API_using"
    def response_and_message(self, GITHUB_TOKEN, message):
        client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=GITHUB_TOKEN,
        )

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "",
                },
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )

        return (response.choices[0].message.content,)
