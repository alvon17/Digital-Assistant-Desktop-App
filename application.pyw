# from threading import local
import pyttsx3
import webbrowser
# import smtplib
import random
import speech_recognition as sr
import wolframalpha
import wikipedia
import datetime
import os
import sys
import pywhatkit
# import time
from dictionary import *
from tkinter import *

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('ULH945-4E9RWQ85KG')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-3].id)

audio = str

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')
    
    speak('Hello Sir, I am your digital assistant, My name is Alpha!')
    speak('How may I help you?')

query = str

def myCommand():
    temp = False
    while temp == False:
        r = sr.Recognizer()                                                                    
        with sr.Microphone() as source:                                                  
            r.pause_threshold =  1
            r.energy_threshold = 4000
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-id')
            print('User: ' + query + '\n')
            temp = True

        except sr.UnknownValueError:
            speak('Sorry sir! I didn\'t get that! Pardon please!')
            # query = str(input('Command: '))
            temp = False

    return query

def myCall():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.energy_threshold = 4000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-id')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        query = '\0'

    return query

def instructions():
    query = myTextBox.get()
    query = query.lower()
    print(query)
    myTextBox.delete(0, END)
    query = tokenize(query)
    query = check_words(query)
    print(query)
    if 'open youtube' in query:
        speak('okay')
        webbrowser.open('www.youtube.com')

    elif 'search something' in query:
        speak('what do you want to search for?')
        search = myCommand()
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what i found for ' + search)

    elif 'find location' in query:
        speak('what is the location?')
        location = myCommand()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)

    elif 'play music on youtube' in query:
        speak('what song do you want to play?')
        song = myCommand()
        pywhatkit.playonyt(song)
        speak('playing ' + song)
            
    elif 'what time is it' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak('It is ' + strTime)
        
    elif 'shutdown my laptop' in query:
        os.system("shutdown /s /t 1")

    elif 'open google' in query:
        speak('okay')
        webbrowser.open('www.google.co.in')

    elif 'open gmail' in query:
        speak('okay')
        webbrowser.open('www.gmail.com')
            
    # elif 'open my gmail' in query:
    #     speak('okay')
    #     webbrowser.open('https://mail.google.com/mail/u/4/#inbox')
            
    elif 'open facebook' in query:
        speak('okay')
        webbrowser.open('www.facebook.com')

    elif 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))

    elif 'wait' in query:
        speak('okay, please call my name if you need me again')
        call = myCall()
        call = call.lower()
        while('alpha' not in call):
            call = myCall()
            call = call.lower()

    elif 'nothing' in query or 'abort' in query or 'stop' in query:
        speak('okay')
        speak('Bye Sir, have a good day.')
        sys.exit()
         
    elif 'hello' in query:
        speak('Hello Sir')

    elif 'bye' in query:
        speak('Bye Sir, have a good day.')
        sys.exit()

    else:
        query = query
        speak('Searching...')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                speak(results)
                    
            except:
                results = wikipedia.summary(query, sentences=2)
                speak(results)
        
        except:
            webbrowser.open('www.google.com')
        
    speak('Next Command! Sir!')

def hiAlpha():
    greetMe()

    while True:
        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'search something' in query:
            speak('what do you want to search for?')
            search = myCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Here is what i found for ' + search)

        elif 'find location' in query:
            speak('what is the location?')
            location = myCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            speak('Here is the location of ' + location)

        elif 'play music on youtube' in query:
            speak('what song do you want to play?')
            song = myCommand()
            pywhatkit.playonyt(song)
            speak('playing ' + song)
            
        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak('It is ' + strTime)
        
        elif 'shutdown my laptop' in query:
            os.system("shutdown /s /t 1")

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
            
        elif 'open facebook' in query:
            speak('okay')
            webbrowser.open('www.facebook.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'wait' in query:
            speak('okay, please call my name if you need me again')
            call = myCall()
            call = call.lower()
            while('alpha' not in call):
                call = myCall()
                call = call.lower()

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
         
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')

def byeAlpha():
    speak('Bye sir, have a good day')
    sys.exit()

if __name__ == "__main__":
    root = Tk()
    root.title('Alpha Assistant')
    root.geometry('250x450')

    myLabel = Label(root, text='Press the Button')
    myLabel.pack()

    onButton = Button(root, text='Turn On', command=hiAlpha)
    onButton.pack(pady=5)

    offButton = Button(root, text='Turn Off', command=byeAlpha)
    offButton.pack(pady=5)

    commandLabel = Label(root, text='\nCommand:\n1. open youtube\n2. search something\n3. find location\n4. play music on youtube\n5. what time is it\n6. shutdown my laptop\n7. open google\n8. open gmail\n9. open facebook\n10. how are you\n11. wait\n12. nothing/abort/stop/bye\n hello\n')
    commandLabel.pack()

    myLabel2 = Label(root, text='Instruct by Command')
    myLabel2.pack(pady=5)

    myTextBox = Entry(root, width=30)
    myTextBox.pack(pady=5)

    submitButton = Button(root, text='Run', command=instructions)
    submitButton.pack(pady=5)

    root.mainloop()
