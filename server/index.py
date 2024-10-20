from flask import Flask, request, url_for, send_from_directory
import uuid

app = Flask(__name__)

dist_folder = '../website/dist'


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

    word = "hello"
    return {
        "word": word,
        "audioURL": "https://media.merriam-webster.com/audio/prons/en/us/mp3/o/orange02.mp3"
    }

# post request


@app.route("/api/submit-audio", methods=["POST"], )
def submit_audio():
    audio_file = request.files['audio']
    # analyze audio

    good = True
    return {
        "good": good
    }
