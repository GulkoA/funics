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
        )
    
    def __call__(self, text):
        output = self.model(text)
        return output

if __name__ == "__main__":
    inf_object = Llama_Inference()
    prompt = "Generate a numbered list of three words that a child can pronounce : "
    output = inf_object(prompt)
    key_output = output[0]['generated_text'].split(":")[1]
    print(key_output)
    words = re.search("[0-9]. ", key_output)
    print(output)
    print(words)
