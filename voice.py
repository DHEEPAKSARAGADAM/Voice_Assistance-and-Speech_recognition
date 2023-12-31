import requests
import pyautogui
import wikipedia
import re
import os
import sys
import subprocess
import random
import speech_recognition as sr
import webbrowser
import time
import datetime
import playsound

class asis:
    name = 'Assistant'
    def setName(self, name):
        self.name = name
      
# for Speak of given text
def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() 
# FOR RECORDING AUDIO
def record_audio(ask=''):
    with sr.Microphone() as source:
        if(ask):
            engine_speak(ask)
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, 6, 4)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak("I didn't get that")
        except sr.RequestError:
            engine_speak('Sorry, my service is down')
        return voice_data.lower()
# fOR REPEATING SPEECH
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 50000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(asis.name + ":", audio_string)

def respond(voice_data):
    if there_exists(['hey', 'hi', 'hello']): # Greetings
        greetings = ["hey, how can I help you " + person_obj.name, "hey, what's up? " + person_obj.name, "I'm listening " + person_obj.name, "how can I help you? " + person_obj.name, "hello " + person_obj.name, "hi " + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            engine_speak(f"my name is {asis_obj.name}")
        else:                                                   
            engine_speak(f"my name is {asis_obj.name}. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)
    
    if there_exists(["what is my name"]):
        engine_speak("Your name must be " + person_obj.name)
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name)
   
    if there_exists(["how are you", "how are you doing", "what's up"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)
    
    if there_exists(["how old are you"]):
        engine_speak("I'm quite young, I'm still learning")

    if there_exists(["what's the time", "tell me the time", "what time is it", "what is the time", "time now"]): # Time
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)
    
    if there_exists(['open website']): # Website
        reg_ex = re.search('open website (.+)', voice_data)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
    
    if there_exists(['music', 'play music', 'songs']): # Musix Mix on Youtube
        url = "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj&list=RDMM&start_radio=1"
        webbrowser.get().open(url)
    
    if there_exists(['restaurant', 'restaurants', 'restaurants near me', 'nearby restaurants']): # Restaurants
        url = "https://www.google.com/search?q=restaurants+near+me"
        webbrowser.get().open(url)

    if there_exists(['supermarket', 'supermarkets', 'supermarket near me', 'nearby supermarket']): # Supermarkets
        url = "https://www.google.com/search?q=supermarket+near+me"
        webbrowser.get().open(url)

    if there_exists(['I need a haircut', 'hair salon', 'hair saloon', 'haircut', 'nearby hair salon']): # Hair Salon
        url = "https://www.google.com/search?q=hair+salon+near+me"
        webbrowser.get().open(url)

    if there_exists(['barber', 'barber shop', 'i need a barber', 'nearby barber shop']): # Barber
        url = "https://www.google.com/search?q=barber+shop+near+me"
        webbrowser.get().open(url)

    if there_exists(['pet shop', 'pet shops', 'pet shops near me']): # Pet Shop
        url = "https://www.google.com/search?q=pet+shops+near+me"
        webbrowser.get().open(url)

    if there_exists(['butcher', 'butcher shop']): # Butcher
        url = "https://www.google.com/search?q=butchers+near+me"
        webbrowser.get().open(url)

    if there_exists(['coffee', 'coffee shops']): # Coffee
        url = "https://google.com/search?q=coffee+shops+near+me"
        webbrowser.get().open(url)

    if there_exists(['bars', 'bars near me', 'drinks']): # Bar
        url = "https://www.google.com/search?q=bars+near+me"
        webbrowser.get().open(url)

    if there_exists(['clubs', 'clubs near me']): # Club
        url = "https://www.google.com/search?q=clubs+near+me"
        webbrowser.get().open(url)

    if there_exists(['news', 'latest news', 'news feed', 'top stories']): # News
        url = "https://news.google.com/"
        webbrowser.get().open(url)

    if there_exists(['gmail', 'g mail', 'geemail']): # Gmail
        url = "https://www.google.com/gmail/" 
        webbrowser.get().open(url)
    
    if there_exists(['facebook', 'open facebook']): # Facebook
        url = "https://facebook.com"
        webbrowser.get().open(url)

    if there_exists(['github']): # Github
        url = "https://github.com"
        webbrowser.get().open(url)

    if there_exists(["search"]) and 'youtube' not in voice_data: # Google Search
        search_term = voice_data.split("search")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term)

    if there_exists(["youtube"]): # Youtube Search
        search_term = voice_data.split("youtube")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + " on youtube")
    
    if there_exists(["game"]): # Rock-Paper-Scissor Game
        voice_data = record_audio("Choose among rock, paper or scissor")
        moves = ["rock", "paper", "scissor"]
        cmove = random.choice(moves)
        pmove = voice_data
        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            engine_speak("Player wins")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Computer wins")
        elif pmove == "paper" and cmove == "rock":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")
   
    if there_exists(["price of"]): # Stock Price
        search_term = voice_data.split("of")[-1]
        url = "https://google.com/search?q=" + search_term + "%20stock"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term)
    
    if there_exists(["covid", "coronavirus", "covid 19"]): # COVID-19 News
        url = "https://duckduckgo.com/?t=ffab&q=covid&ia=coronavirus"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for Coronavirus")

    if there_exists(["weather"]): # Weather
        search_term = voice_data.split("weather")[-1]
        url = "https://google.com/search?q=weather"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for weather")
    
    if there_exists(["my region"]): # Region
        Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
        loc = Ip_info['region']
        engine_speak(f"You must be somewhere in {loc}")    
        
    if 'find location' in voice_data: # Location
        location = record_audio('What is the location?')
        url = "https://google.com/maps/place/" + location
        webbrowser.get().open(url)
        engine_speak('Here is the location of ' + location)
    
    if there_exists(["what is my exact location", "what's my exact location", "my exact location", "my location", "where am i"]): # Current location from Google Maps
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")  

    def note(voice_data): # Note
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(voice_data)
        subprocess.Popen(["notepad.exe", file_name])

        NOTE_STRS = ["make a note", "write this down", "remember this", "type this"]
        for phrase in NOTE_STRS:
            if phrase in voice_data:
                engine_speak("What would you like me to write down? ")
                write_down = record_audio()
                note(write_down)
                engine_speak("I've made a note of that.")
    
    if there_exists(['open calculator']): # Calculator
        os.system('calc')

    if there_exists(['open calendar']): # Calendar
        url = "https://calendar.google.com/calendar"
        webbrowser.get().open(url)

    if there_exists(['open mail', 'open the mail', 'outlook']): # Outlook
        os.startfile('Outlook')

#    if there_exists(['open photos']): # Photos
#        os.system('Photos')

#    if there_exists(['open settings', 'settings']): # Setting 
#        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Settings')

    if there_exists(["user", "users"]): # User path
        path = "C:/Users"
        path = os.path.realpath(path)
        os.startfile(path)

    if there_exists(["capture", "my screen", "screenshot"]): # Screenshot
        z = random.randint(1, 50000000)
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/user/image' + str(z) + '.png') 
        
    if there_exists(["definition"]): # Definition
        try:
            definition = record_audio("What do you need the definition of?")
            wiki = wikipedia.page(str(definition), features="lxml")
            url = wiki.url
            webbrowser.get().open(url)
            print(wikipedia.summary(str(definition), sentences=2))
        except:
                engine_speak("I am sorry I could not find the definition for " + definition)
    
    if there_exists(["exit", "quit", "goodbye", "bye", "sleep", "I'm out"]): # Exit
        engine_speak("bye")
        sys.exit("Bye")

time.sleep(1)

person_obj = person()
person_obj.name = ''
asis_obj = asis()
asis_obj.name = 'Assistant'
engine = pyttsx3.init()
engine_speak('How can I help you?')

while 1:
    voice_data = record_audio("Recording")
    print("Q:", voice_data)
    respond(voice_data)


