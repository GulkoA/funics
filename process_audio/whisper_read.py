import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration, pipeline
import os
import soundfile as sf

class Whisper:
    def __init__(self):
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-medium")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-medium")
        # self.model = pipeline("openai/whisper-small")

    def __call__(self, fileName):
        data, samplerate = sf.read(fileName) # Extracting the information and sample rate of the audio from the audio file
        input_features = self.processor(
            data, samplerate, return_tensors="pt"
        ).input_features
        output = self.model.generate(input_features)
      
        return self.processor.batch_decode(output, skip_special_tokens=True)[0]
        
    def getConfidenceScore(self, fileName):
        data, samplerate = sf.read(fileName) # Extracting the information and sample rate of the audio from the audio file
        input_features = self.processor(
            data, samplerate, return_tensors="pt"
        ).input_features

        outputs = self.model.generate(input_features, 
                                      output_hidden_states=True, 
                                      return_dict_in_generate=True,
                                      output_scores=True)
        logits_per_token = outputs.scores
        logits_normalized = [ torch.max( torch.softmax(logit, dim = -1) ) for logit in logits_per_token]
        # print(logits_normalized)
        logits_normalized = float(sum(logits_normalized) / 3)
        
        return logits_normalized

if __name__ == "__main__":
    whisper_object = Whisper()
    fileName = "pronunciations/cow.mp3"
    transcription = whisper_object.getConfidenceScore(fileName)
    print(transcription)
