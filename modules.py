import os
import playsound
import speech_recognition
from gtts import gTTS
from googletrans import Translator

def speak(text):
    ''' Converts text to speech '''
    try:
        tts = gTTS(text=text, lang='es')
    except:
        tts = gTTS(text='Sin palabras', lang='es')
    filename = 'temp.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def recognize():
    ''' Recognizes speech and converts it to text '''
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except:
            return ""

def translate(text):
    ''' Translates text from english to spanish '''
    translator = Translator()
    try:
        return translator.translate(text, src='en', dest='es').text
    except:
        return ""