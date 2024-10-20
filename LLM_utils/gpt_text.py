# import torch
# from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
# from datasets import load_dataset, Dataset, Audio
from openai import OpenAI
import os

class OpenAI_text:
    def __init__(self):
        self.client = OpenAI()
        self.counter = 0

    def __call__(self, text):
        self.counter += 1
        messages = [
            {"role": "user", "content": str(self.counter) + " " + text}
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o",  # Ensure correct model name is used
            messages=messages,
            temperature=1.5,
            max_tokens=50,
        )
        response_text = response.choices[0].message.content

        # Extract the assistant's reply from the response
        return response_text
        
if __name__ == "__main__":
    # for i in range(20):
    text_engine = OpenAI_text()
    prompt = "Give three words a child might say, comma seperated. Only output the three words."
    output = text_engine(prompt)
    print(output)


