import io
from flask import Flask, request, url_for, send_from_directory
import uuid
import soundfile as sf
import wave

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

word = "green"


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

    return {
        "word": word.word,
        "audioURL": word.audio
    }

# post request


@app.route("/api/submit-audio", methods=["POST"], )
def submit_audio():
    if 'audio' not in request.files:
        return {"error": "No audio file provided"}, 400

    audio_file = request.files['audio']
    print(f"Received file: {audio_file.filename}, Content-Type: {audio_file.content_type}")

    try:
        # Read the audio data into a BytesIO buffer
        audio_data = io.BytesIO(audio_file.read())

        # Open the WAV file and extract relevant data
        with wave.open(audio_data, 'rb') as wav:
            sample_rate = wav.getframerate()
            num_channels = wav.getnchannels()
            num_frames = wav.getnframes()
            audio_frames = wav.readframes(num_frames)

            print(f"Sample Rate: {sample_rate}, Channels: {num_channels}, Frames: {num_frames}")

    except wave.Error as e:
        print(f"Wave Error: {e}")
        return {"error": str(e)}, 400

    audio = (audio_frames, sample_rate)
    # Perform your audio processing logic (assuming `judge` function is compatible)
    good = judge.judge(audio, word)


    good = judge.judge(audio_frames, word)

    return {
        "good": good
    }
