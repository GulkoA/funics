import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration, pipeline
import os
import soundfile as sf
# from datasets import load_dataset
import numpy as np

class Whisper:
    def __init__(self):
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-medium")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-medium")

    def __call__(self, audio):
        data, samplerate = audio
        # data, samplerate = sf.read(fileName) # Extracting the information and sample rate of the audio from the audio file
        
        if len(data.shape) >= 2:
            data = np.sum(data, axis = -1)

        input_features = self.processor(
            data, samplerate, return_tensors="pt"
        ).input_features
        output = self.model.generate(input_features)
      
        return self.processor.batch_decode(output, skip_special_tokens=True)[0]
        
    def getConfidenceScore(self, audio):
        data, samplerate = audio
        # data, samplerate = sf.read(fileName) # Extracting the information and sample rate of the audio from the audio file
       
        if len(data.shape) >= 2:
            data = np.sum(data, axis = -1)
 
        input_features = self.processor(
            data, 
            samplerate, 
            return_tensors="pt", 
        ).input_features

        outputs = self.model.generate(input_features, 
                                      output_hidden_states=True, 
                                      return_dict_in_generate=True,
                                      output_scores=True)
        logits_per_token = outputs.scores
        logits_normalized = [ torch.max( torch.softmax(logit, dim = -1) ) for logit in logits_per_token]
        print(logits_normalized)
        logits_normalized = float(sum(logits_normalized) / len(logits_normalized))
        
        return logits_normalized

if __name__ == "__main__":
    whisper_object = Whisper()
    # fileName = "cache/correct_hello.mp3"
    fileName = "cache/bad_hello.mp3"
    transcription = whisper_object(fileName)
    score = whisper_object.getConfidenceScore(fileName)
    print(transcription)
    print(score)
