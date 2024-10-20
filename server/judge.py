from process_audio.whisper_read import Whisper
from word_net import WordNet

THRESHOLD = 0.7

class Judge():
    def __init__(self, wordnet):
      self.wordnet = wordnet

      print("Creating Whisper")
      self.whisper = Whisper()
      print("Whisper created")

    def get_score(self, audio, word):
      predicted_word = self.whisper(audio)
      confidence = self.whisper.getConfidenceScore()

      if predicted_word == word and confidence > THRESHOLD:
        return 1
      elif predicted_word == word:
        return -1 * (1 - confidence)
      else:
        return -1
      
    def judge(self, audio, word) -> bool:
      score = self.get_score(audio, word)
      print(f"Score for {word}: {score}")
      
      for word_node in self.wordnet.words:
        if word_node.word == word:
          word_node.adjust_score_by(score)
          break

      return score > 0
      