# import torch
# from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
# from datasets import load_dataset, Dataset, Audio
from openai import OpenAI
import os

class OpenAI_text:
    def __init__(self):
        self.client = OpenAI()

    def __call__(self, text):
        messages = [
            {"role": "user", "content": text}
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o",  # Ensure correct model name is used
            messages=messages,
            temperature=1.5,
            max_tokens=100,
        )
        response_text = response.choices[0].message.content

        # Extract the assistant's reply from the response
        return response_text
        
if __name__ == "__main__":
    text_engine = OpenAI_text()
    prompt = f"Create a math equation using only addition, subtraction and parentheses. Include the final result, ended with an equation symbol. This equation should not be too difficult for a child to solve. Do not ouput any other symbols beside the math equation. Use anywhere between 2-4 operands."
    output = text_engine(prompt)
    print(output)
    # proficency_levels = ["baby, beginner, intermediate, advanced"]
    # curr_prof = proficency_levels[0]
    # prompt = f"Suggest a sentence as an exercise for a child at a {curr_prof} reading level."
    # output = text_engine(prompt)
    # print(output)


