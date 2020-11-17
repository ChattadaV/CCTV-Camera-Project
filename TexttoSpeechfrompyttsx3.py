#------From https://stackoverflow.com/questions/48438686/realistic-text-to-speech-with-python-that-doesnt-require-internet
#------ pyttsx3 Documentation: https://pypi.org/project/pyttsx3/2.5/
#------ pyttsx3 voice changing: https://stackoverflow.com/questions/28344200/changing-the-voice-with-pyttsx-module-in-python


#install
#import os
#output = os.system('sudo pip3 install pyttsx3') #use pip3 instead of pip for python3
#output = os.system('sudo apt-get update')
#output = os.system('sudo apt-get -y install espeak') #install eSpeak for text to speech (to create an audio)
#use eSpeak (espeak) for speech engine naturally, use SAPI5 (sapi5) if on Windows, and use NSSpeechSynthesizer (nsss) on Mac OS X

import pyttsx3

engine = pyttsx3.init()
#engine = pyttsx3.init(driverName='sapi5') #use this line to specify speech engine (espeak, sapi5 (for windows), nsss (for Mac OS X))
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

#engine.setProperty('voice', voice.id)
engine.setProperty('rate', rate-30)

#myText = 'Testing Text to Speech on Raspberry Pi' #for text_to_speech in the quote
fh = open('test.txt', 'r') #file handling (open text document for text_tp_speech)
myText = fh.read().replace('\n', ' ') #set myText to the the saved document and replace all the line endings with a space (to not confuse gTTS)

#engine.say("I will speak this text") #for text_to_speech in the quote
engine.say(text=myText)

engine.runAndWait()
