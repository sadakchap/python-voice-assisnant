import os
import speech_recognition as sr
import webbrowser
import random
from time import ctime, sleep
from gtts import gTTS
import playsound

r = sr.Recognizer()

def audio_to_words(ask=None):
    if ask:
        text_to_audio(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            text_to_audio('Sorry! I did not understand that!')
        except sr.RequestError:
            text_to_audio('Sorry, Looks like your internet is down :(')
        
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        text_to_audio( 'My name is Radha')

    if 'what time is it' in voice_data:
        text_to_audio(ctime())

    if 'search' in voice_data:
        search_for = audio_to_words('What do you want to search for?')
        url = 'https://www.google.com/search?q='+search_for
        text_to_audio(f'Here is what I found for "{search_for}"!')
        webbrowser.open_new(url)

    if 'find location' in voice_data:
        search_location = audio_to_words('Which location do you to search?')
        if search_location:
            url = 'https://google.nl/maps/place/' + search_location + '/&amp;'
            text_to_audio(f'Here is location of "{search_location}"!')
            webbrowser.get().open(url)
        else:
            text_to_audio('Sorry, say something!')

    if 'exit' in voice_data:
        exit()


def text_to_audio(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000000)
    audio_file = f'audio-{r}.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


text_to_audio('How Can I help you?')
sleep(1)
while 1:
    voice_data = audio_to_words()
    print(voice_data)
    respond(voice_data)

