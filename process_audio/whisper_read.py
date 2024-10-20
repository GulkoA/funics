# import torch
# from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
# from datasets import load_dataset, Dataset, Audio
from openai import OpenAI
import os

class Whisper_Inference:
    def __init__(self):
        self.client = OpenAI()

    def __call__(self, fileName):
        audio_file= open(fileName, "rb")
        transcription = self.client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
        )
        return transcription.text

if __name__ == "__main__":
    whisper_object = Whisper_Inference()
    fileName = "pronunciations/hello.mp3"
    transcription = whisper_object(fileName)
    print(transcription)
