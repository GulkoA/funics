import torch
from transformers import pipeline
import re

class Llama_Inference:
    def __init__(self):
        model_id = "unsloth/Llama-3.2-3B-Instruct"
        self.model = pipeline(
            "text-generation", 
            model=model_id, 
            torch_dtype=torch.bfloat16, 
            device_map="auto",
            max_length = 50
        )
    
    def __call__(self, text):
        output = self.model(text)
        return output

if __name__ == "__main__":
    inf_object = Llama_Inference()
    for i in range(10):
        prompt = "Give three words, comma seperated:"
        # prompt = "What is the h\u0259-\u02c8l\u014d"
        output = inf_object(prompt)
        print(output)
        key_output = output[0]['generated_text'].split(":")[1]
        print(key_output)
        words = re.split("[0-9]. ", key_output)
        print(output)
        print(words)

