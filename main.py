import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random

from gtts import gTTS
from time import ctime
r = sr.Recognizer()

def recordAudio(ask = False):    
    with sr.Microphone() as source:
        if ask:
            adeleSpeak(ask)
        audio = r.listen(source)
        try:
            voiceData = r.recognize_google(audio)
            return voiceData
        except sr.UnknownValueError:
            adeleSpeak('Sorry, I did not get that')
        except sr.RequestError:
            adeleSpeak('Sorry, my speech service is down')


def adeleSpeak(audioString):
    tts = gTTS(text=audioString, lang="en")
    r = random.randint(1, 1000000)
    audioFile = 'audio-' + str(r) + '.mp3'
    tts.save(audioFile)
    playsound.playsound(audioFile)
    print(audioString)
    os.remove(audioFile)

def respond(voiceData):
    if 'what is your name' in voiceData:
        adeleSpeak('My name is Adele')

    if 'time' in voiceData:
        adeleSpeak(ctime())
    
    if 'search' in voiceData:
        search = recordAudio('what do you want to search?')
        if search:
            url = 'https://google.com/search?q=' + search
            adeleSpeak('Here is what I found for ' + search)
            webbrowser.get().open(url)
    if 'exit' in voiceData:
        adeleSpeak('Sure thing, bye')
        exit()

time.sleep(1)
adeleSpeak('How can I help you?')
while 1:
    voiceData = recordAudio()
    if voiceData:
        print(voiceData)
        respond(voiceData)
        time.sleep(1)