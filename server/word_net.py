from dictionary import Dictionary

class WordNet:
    def __init__(self, dictionary: Dictionary):
        self.words: list[WordNode] = []
        self.sounds: list[SoundNode] = []

        for sound in dictionary.get_all_sounds():
            sound_node = SoundNode(sound)
            self.sounds.append(sound_node)

    def add_word(self, word, transcription, audio):
        word_node = WordNode(word, transcription, audio)
        self.words.append(word_node)

        for sound in word_node.transcription:
            if any(sound_node.sound == sound for sound_node in self.sounds):
                sound_node = next(sound_node for sound_node in self.sounds if sound_node.sound == sound)
            else:
                sound_node = SoundNode(sound)
                self.sounds.append(sound_node)
            word_node.sounds.append(sound_node)
            sound_node.words.append(word_node)

    def get_word(self, word):
        min_score
            

class WordNode:
    def __init__(self, word, transcription, audio):
        self.word = word
        self.transcription = transcription
        self.audio = audio
        self.sounds = []

    def sound_score(self):
        return sum(sound.score for sound in self.sounds)

class SoundNode:
    def __init__(self, sound):
        self.sound = sound
        self.words = []
        self.score = 0