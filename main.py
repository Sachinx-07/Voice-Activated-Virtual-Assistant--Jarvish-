import speech_recognition as sr
import webbrowser 
import pyttsx3
import musicLibrary
import time     #xadd
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
# engine = pyttsx3.init()
newsapi="f8d32bd9687543ad8dea6ef90623ee67"

def speak_old(text):
    engine = pyttsx3.init()   #use this inside speak() work for me to run every speak funcion

    engine.say(text)
    engine.runAndWait()
    engine.stop()           #xadd

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        speak("opnening google")      #xadd
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("onening facebook")      #xadd

        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("opnening youtube")      #xadd

        webbrowser.open("https://youtube.com")
    elif "open linkdin" in c.lower():
          speak("opnening linkdin")      #xadd
          webbrowser.open("https://linkedin.com")
    # elif c.lower().startwith("play"):
    elif  "play" in c.lower():
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news"in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 
        
    #  pass

if __name__=="__main__":

        speak("Intializing Jaarvishh")
        
        speak("jarvish activated")   #xadd by me

        while True:

            # listen for the wake word jarvish
            # obtain audio from the microphone
            r = sr.Recognizer()
            
            

            # recognize speech using Sphinx  xx
            # recognize speech using google  

            # print("recognizing...")
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)      # xadd --> Ambient Noise Adjustment   (This improves accuracy a LOT.)

                    speak("listening...")   #xadd by me
                    print("listening...")
                    audio=r.listen(source,timeout=5, phrase_time_limit=5)
                    # audio = r.listen(source)

                print("recognizing...")

                # command=r.recognize_sphinx(audio) #(not using this as this is not recognizing properly)
                word=r.recognize_google(audio)
                print(word)
                # if (word.lower()=="jarvis"): #either this or
                # if (word.lower()==word):
                if "jarvis" in word.lower():  #xadd
                      time.sleep(0.5)          #xadd

                      speak("yes boss how can i help youu")

                      #  listen for command
                      with sr.Microphone() as source:
                        print("jarvis active...")
                        audio = r.listen(source)
                        command=r.recognize_google(audio)
                        

                        processCommand(command)
            except Exception as e:
                print("error; {0}".format(e))
