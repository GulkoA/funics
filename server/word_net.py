from dictionary_bartender import get_stripped_transcription, get_audio_url

class WordNet:
    def __init__(self):
        self.words: list[WordNode] = []
        self.sounds: list[SoundNode] = []

    def add_word(self, word):
        word_node = WordNode(word)
        self.words.append(word_node)

        for sound_node in self.sounds:
            if word_node.sound in word_node.transcription:
                word_node.sounds.append(sound_node)
                sound_node.words.append(word_node)

class WordNode:
    def __init__(self, word):
      self.word = word
      self.transcription = get_stripped_transcription(word)
      self.audio = get_audio_url(word)
      self.sounds = []

class SoundNode:
    def __init__(self, sound):
        self.sound = sound
        self.words = []