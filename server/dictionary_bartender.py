# import os
# import requests
# from dotenv import load_dotenv
# load_dotenv()

# key = os.environ['MERRIAM_WEBSTER_API_KEY']
# url = f'https://www.dictionaryapi.com/api/v3/references/sd2/json/'

import json

dictionary = {}
with open('../vocab.json') as f:
  dictionary = json.load(f)

def get_words():
  return dictionary.keys()


def get_word(word):
  return dictionary[word]

def get_transcription(word):
  response = get_word(word)
  if type(response) == list:
    return response[0].get('hwi', {}).get('prs', [{}])[0].get('mw', '')
  else:
    Exception('No transcription found')

def get_stripped_transcription(word):
  transcription = get_transcription(word)
  if transcription:
    return transcription.replace('ˈ', '').replace('ˌ', '').replace('-', '')
  return ''

def get_audio_url(word):
  response = get_word(word)
  if type(response) == list:
    name = response[0].get('hwi', {}).get('prs', [{}])[0].get('sound', {}).get('audio', '')
    if name:
      return f'https://media.merriam-webster.com/audio/prons/en/us/mp3/{name[0]}/{name}.mp3'
  return ''


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('word', type=str)
  args = parser.parse_args()
  print(get_stripped_transcription(args.word))

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