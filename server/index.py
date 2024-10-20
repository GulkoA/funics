import io
import os
import subprocess
from flask import Flask, request, url_for, send_from_directory
import uuid
import soundfile as sf
# from pydub import AudioSegment
# import moviepy.editor as moviepy


from dictionary import Dictionary
from word_net import WordNet
from process_audio.whisper_read import Whisper
from judge import Judge

app = Flask(__name__)

dist_folder = '../website/dist'

dictionary = Dictionary('./vocab.json')
wordnet = WordNet(dictionary)
print(f"Loaded {len(wordnet.words)} words and {len(wordnet.sounds)} sounds")
judge = Judge(wordnet)

global_word = "up"


@app.route("/")
@app.route("/parent")
def serve_html():
    return send_from_directory(dist_folder, 'index.html')


@app.route("/assets/<path>")
def serve_assets(path):
    print('path requested', path)
    return send_from_directory(dist_folder + '/assets', path)


@app.route("/cache/<path>")
def cache(path):
    return send_from_directory('../cache', path)


@app.route("/api/get-word")
def get_word():
    # get word from database
    word = wordnet.get_min_word()
    global_word = word.word
    return {
        "word": word.word,
        "audioURL": word.audio
    }

# post request


@app.route("/api/submit-audio", methods=["POST"], )
def submit_audio():
    # blob
    file = request.files['audio']

    # Write the data to a file.
    file.save("./cache/audio.webm")

    convert("./cache/audio.webm", "./cache/audio.mp3")
    # audio = AudioSegment.from_file("./cache/audio.webm", "webm")
    # audio.export("audio.wav", format="wav")


    # audio_file = request.files['audio']
    # file_id = uuid.uuid4()
    # audio_file.save(f"../cache/{file_id}.wav")

    good = judge.judge(f"./cache/audio.mp3", global_word)

    return {
        "good": good
    }

def convert(input_path, output_path):
    command = ['ffmpeg', '-i', input_path, output_path, '-y']
    os.system(' '.join(command))

