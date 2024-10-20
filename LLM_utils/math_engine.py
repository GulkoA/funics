from gpt_text import OpenAI_text
import os
import re
from num2words import num2words

class MathEngine(OpenAI_text):
    def __init__(self):
        super().__init__()

    def generate(self, prompt):
        math_equation = self.__call__(prompt)
        print(math_equation)
        text_output = []
        # Convert math symbols to words for text to speech
        for i in range(len(math_equation)):
            if math_equation[i].isnumeric():
                text_output.append(num2words(math_equation[i]))
            elif math_equation[i] == "(":
                text_output.append("open")
            elif math_equation[i] == ")":
                text_output.append("closed")
            elif math_equation[i] == "+":
                text_output.append("plus")
            elif math_equation[i] == "-":
                text_output.append("minus")
            elif math_equation[i] == "=":
                text_output.append("=")
            else:
                continue

        equi2word = " ".join(text_output[:-2])
        res = text_output[-1]

        return {"res" : res, "equation" : equi2word}
            
if __name__ == "__main__":
    math_engine = MathEngine()
    prompt = f"Create a math equation using only addition, subtraction and parentheses. Include the final result, ended with an equation symbol. This equation should not be too difficult for a child to solve. Do not ouput any other symbols beside the math equation. Use either two or three operands."
    output = math_engine.generate(prompt)
    print(output)



