import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model_and_tokenizer():
    model_name = "unsloth/Llama-3.2-1B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_sentence(model, tokenizer, max_length=30):
    prompt = "Generate a single, simple sentence for a child to read:"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Extract the generated sentence, removing the prompt
    sentence = generated_text.split(prompt)[-1].strip()
    return sentence

def main():
    print("Loading model and tokenizer...")
    model, tokenizer = load_model_and_tokenizer()
    
    print("Generating sentence...")
    sentence = generate_sentence(model, tokenizer)
    
    print("Generated sentence:")
    print(sentence)

if __name__ == "__main__":
    main()