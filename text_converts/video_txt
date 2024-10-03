from flask import Flask, render_template, request
from moviepy.editor import VideoFileClip
import speech_recognition as sr

app = Flask(__name__)

def transcribe_video(video_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile("audio.wav")

    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile("audio.wav")

    with audio_file as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    return text

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/transcribe_video', methods=['POST'])
def transcribe_video_endpoint():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        text = transcribe_video(file)
        return text

if __name__ == '__main__':
    app.run(debug=True)