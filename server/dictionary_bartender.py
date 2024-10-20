import os
import requests
from dotenv import load_dotenv
load_dotenv()

key = os.environ['MERRIAM_WEBSTER_API_KEY']
url = f'https://www.dictionaryapi.com/api/v3/references/sd2/json/'


def get_word(word):
    response = requests.get(url + word, params={"key": key})
    return response.json()


def get_transcription(word):
    response = get_word(word)
    if type(response) == list:
        return response[0].get('hwi', {}).get('prs', [{}])[0].get('mw', '')
    return ''


if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument('word', type=str)
    # args = parser.parse_args()

    import json
    with open('../words.txt') as f:
        words = f.readlines()
        vocab = {}
        i = 0
        while i < len(words):
            word = words[i]
            word = word.strip().lower()
            vocab[word] = get_word(word)
            print(word)
            i += 1

        with open('../vocab.json', 'w') as f:
            f.write(json.dumps(vocab, indent=2))
