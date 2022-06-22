import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import wolframalpha
import wikipedia
import datetime
import os
import sys
import pywhatkit
from dictionary import *
import tkinter as tk

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
        r.energy_threshold = 4000
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-id')
                print('User: ' + query + '\n')
                temp = True
            except sr.UnknownValueError:
                speak('Sorry sir! I didn\'t get that! Pardon please!')
            # query = str(input('Command: '))
    return query

def myCall():
    print("Listening...")
    r = sr.Recognizer()                                               
    r.energy_threshold = 4000
    with sr.Microphone() as source:
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
    myTextBox.delete(0, 'end')
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
        speak('Bye sir, have a good day')
        os.system("shutdown /s /t 1")
        sys.exit()

    elif 'open google' in query:
        speak('okay')
        webbrowser.open('www.google.co.in')

    elif 'open gmail' in query:
        speak('okay')
        webbrowser.open('www.gmail.com')
            
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
            speak('Bye sir, have a good day')
            os.system("shutdown /s /t 1")
            sys.exit()

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
            break
         
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            break

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
    window = tk.Tk()
    window.iconbitmap('images/assistant2.ico')
    window.title("A.L.P.H.A")

    window.geometry("862x519")
    window.configure(bg="#2B2B2B")
    canvas = tk.Canvas(
        window, bg="#2C96F1", height=519, width=862,
        bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC", outline="")
    canvas.create_rectangle(40, 125, 40 + 60, 125 + 5, fill="#FCFCFC", outline="")

    text_box_bg = tk.PhotoImage(file="images/Command Layer.png")
    text_entry_img = canvas.create_image(650.5, 307.5, image=text_box_bg)
    robot_box_bg = tk.PhotoImage(file="images/assistant.png")
    robot_entry_img = canvas.create_image(650.5, 123, image=robot_box_bg)

    myTextBox = tk.Entry(window, bd=0, bg="#C6CCD2", highlightthickness=0)
    myTextBox.place(x=490.0, y=277+25, width=270.0, height=35)
    myTextBox.focus()

    canvas.create_text(
        490.0, 296.0, text="Command", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")
    canvas.create_text(
        650.5, 243.0, text="Enter Your Command",
        fill="#000000", font=("Arial Bold", int(22.0)))

    title_1 = tk.Label(
        text="Alpha Assistant", bg="#2C96F1",
        fg="white", font=("Verdana bold", int(22.0)))
    title_1.place(x=87.0, y=30.0)

    title_2 = tk.Label(
        text="Commands", bg="#2C96F1",
        fg="white", font=("Verdana", int(17.0)))
    title_2.place(x=27.0, y=90.0)

    info_text = tk.Label(
        text="1. Open youtube\n2. Search something\n3. Find location\n4. Play music on youtube\n5. What time is it\n6. Shutdown my laptop\n7. Open google\n8. Open gmail\n9. Open facebook\n10. How are you\n11. Wait\n12. Nothing/abort/stop/bye\n13. Hello\n",
        bg="#2C96F1", fg="white", justify="left",
        font=("Verdana", int(14.0)))

    info_text.place(x=27.0, y=142.0)


    on_btn_img = tk.PhotoImage(file="images/ON Button.png")
    on_btn = tk.Button(
        image=on_btn_img, borderwidth=0, highlightthickness=0,
        command=hiAlpha, relief="flat")
    on_btn.place(x=517, y=381)

    off_btn_img = tk.PhotoImage(file="images/OFF Button.png")
    off_btn = tk.Button(
        image=off_btn_img, borderwidth=0, highlightthickness=0,
        command=byeAlpha, relief="flat")
    off_btn.place(x=677, y=381)

    submit_btn_img = tk.PhotoImage(file="images/Enter Button.png")
    submit_btn = tk.Button(
        image=submit_btn_img, borderwidth=0, highlightthickness=0,
        command=instructions, relief="flat")
    submit_btn.place(x=788, y=290)

    window.resizable(False, False)
    window.mainloop()
