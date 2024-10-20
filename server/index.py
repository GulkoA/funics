from flask import Flask, request, url_for, send_from_directory
import uuid

app = Flask(__name__)

@app.route("/")
@app.route("/parent")
def serve_html():
  return send_from_directory('static', 'index.html')

@app.route("/<path>")
def serve_static(path):
  print(path)
  return send_from_directory('static', path)

@app.route("/cache/<path>")
def cache(path):
  return send_from_directory('../cache', path)

@app.route("/api/get-word")
def get_word():
  # get word from database

  word = "hello"
  audio_path = "cache/hello.mp3"
  return {
    "word": word,
    "audioPath": audio_path
  }

# post request
@app.route("/api/submit-audio", methods=["POST"], )
def submit_audio():
  submission_id = uuid.uuid4()
  audio_file = request.files['audio']
  audio_file.save(f"../cache/{submission_id}.wav")
  # analyze audio


  good = True
  return {
    "good": good
  }