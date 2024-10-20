from dictionary import Dictionary

class WordNet:
    def __init__(self, dictionary: Dictionary):
        self.words: list[WordNode] = []
        self.sounds: list[SoundNode] = []

        for sound in dictionary.get_all_sounds():
            sound_node = SoundNode(sound)
            self.sounds.append(sound_node)

        for word in dictionary.get_words():
            word_obj = dictionary.get_word(word)
            self.add_word(word, dictionary.get_stripped_transcription(word_obj), dictionary.get_audio_url(word_obj))

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

    def get_min_word(self):
        min_score = self.words[0].sound_score()
        min_word = self.words[0]
        for word_node in self.words:
            score = word_node.sound_score()
            if score < min_score:
                min_score = score
                min_word = word_node
        return min_word
            
class WordNode():
    def __init__(self, word, transcription, audio):
        self.word = word
        self.transcription = transcription
        self.audio = audio
        self.sounds = []

    def sound_score(self):
        return sum(sound.score for sound in self.sounds)
    
    def adjust_score_by(self, amount):
        for sound in self.sounds:
            sound.score += amount
            if sound.score < 0:
                sound.score = 0
            elif sound.score > 10:
                sound.score = 10

class SoundNode():
    def __init__(self, sound):
        self.sound = sound
        self.words = []
        self.score = 0