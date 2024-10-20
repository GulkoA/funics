# import os
# import requests
# from dotenv import load_dotenv
# load_dotenv()

# key = os.environ['MERRIAM_WEBSTER_API_KEY']
# url = f'https://www.dictionaryapi.com/api/v3/references/sd2/json/'

import json

class Dictionary():
  def __init__(self):
    with open('../vocab.json') as f:
      self.dictionary = json.load(f)

  def get_words(self):
    return self.dictionary.keys()


  def get_word(self, word) -> dict:
    return self.dictionary[word]

  def get_transcription(self, word: dict):
    transcription = word[0]['hwi']['prs'][0]['mw']
    return transcription

  def get_stripped_transcription(self, word: dict):
    transcription = self.get_transcription(word)
    return transcription.replace('ˈ', '').replace('ˌ', '').replace('-', '')

  def get_all_sounds(self):
    sounds = set()
    for word, value in self.dictionary.items():
      transcription = self.get_transcription(value)
      for sound in transcription:
        sounds.add(sound)
    return sounds

  def get_audio_url(self, word: dict):
    name = word[0]['hwi']['prs'][0]['sound']['audio']
    return f'https://media.merriam-webster.com/audio/prons/en/us/mp3/{name[0]}/{name}.mp3'

  # if __name__ == '__main__':
  #   import argparse
  #   parser = argparse.ArgumentParser()
  #   parser.add_argument('word', type=str)
  #   args = parser.parse_args()
  #   print(get_stripped_transcription(args.word))

    # import json
    # with open('../words.txt') as f:
    #   words = f.readlines()
    #   vocab = {}
    #   i = 0
    #   while i < len(words):
    #     word = words[i]
    #     word = word.strip().lower()
    #     vocab[word] = get_word(word)
    #     print(word)
    #     i += 1

    #   with open('../vocab.json', 'w') as f:
    #     f.write(json.dumps(vocab, indent=2))