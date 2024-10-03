from flask import Flask, render_template, request
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

app = Flask(__name__)

def transcribe_video(video_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile("audio.wav")

    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile("audio.wav")

    with audio_file as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data) #To put API key in, do , and then api key

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
        file_path = os.path.join('uploaded_file.mp4') #Put a video file or something here idk
        file.save(file_path)
        text = transcribe_video(file)
        os.remove(file_path)
        return text

if __name__ == '__main__':
    app.run(debug=True)