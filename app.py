from flask import Flask, render_template, request,redirect
import speech_recognition as sr


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])    
def index():
    file = None
    transcript = ""
    if request.method == 'POST':
        print("recieved")
        
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
    if file:
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(file)
        with audio_file as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio,key=None)
        print(text)
        return render_template('index.html', transcript=text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
