
import torch
from transformers import pipeline

class WhisperConfidenceScores():
    whisper = pipeline("automatic-speech-recognition", "openai/whisper-large-v3", torch_dtype=torch.float16, device="cuda:0")

    transcription = whisper("<audio_file.mp3>")

    print(transcription["text"])