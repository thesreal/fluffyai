from gtts import gTTS
import speech_recognition as sr
import os
import random
from datetime import datetime
import urllib.request, json
import http.client
import tkinter as tk
from PIL import ImageTk, Image
from eventregistry import *
import subprocess
subprocess.Popen("python3 house.py",shell=True)
r = sr.Recognizer()
tts = gTTS(text="Welcome back!", lang='en')
tts.save("tr.mp3")
os.system("mpg321 tr.mp3")
while True:
    with sr.Microphone() as source:
        print("Give me a command!");
        audio = r.listen(source)
    if 'what is' in r.recognize_google(audio):
        try:
            with urllib.request.urlopen("https://api.dictionaryapi.dev/api/v2/entries/en/"+r.recognize_google(audio).replace("what is ", "")) as url:
                data = json.load(url)
                try:
                    tts = gTTS(text=str(data[0]["meanings"][0]["definitions"][0]["definition"]), lang='en')
                    tts.save("tr.mp3")
                    os.system("mpg321 tr.mp3")
                except:
                    tts = gTTS(text="Oops, an error occured.", lang='en')
                    tts.save("tr.mp3")
                    os.system("mpg321 tr.mp3")
        except:
                tts = gTTS(text="Oops, an error occured.", lang='en')
                tts.save("tr.mp3")
                os.system("mpg321 tr.mp3")
    elif 'tell me the time' in r.recognize_google(audio):
        now = datetime.now()
        current_time = now.strftime("%H %M")
        tts = gTTS(text="The time is "+current_time, lang='en')
        tts.save("tr.mp3")
        os.system("mpg321 tr.mp3")
    elif 'end' in r.recognize_google(audio):
        tts = gTTS(text="Bye bye, Fluffy fan. See ya soon!", lang='en')
        tts.save("tr.mp3")
        os.system("mpg321 tr.mp3")
        os._exit(os.EX_OK)
    elif 'tell me the weather' in r.recognize_google(audio):
        conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "bd32181f0amshdc1a69d774bdbc8p17cacdjsn13706569590f",
            'X-RapidAPI-Host': "weatherbit-v1-mashape.p.rapidapi.com"
        }
        conn.request("GET", "/forecast/minutely?lat=51.2470588684082&lon=-0.5760717988014221&units=metric", headers=headers)
        res = conn.getresponse()
        data = res.read()
        parsed_data = json.loads(data)
        tts = gTTS(text=str(parsed_data["data"][0]["snow"])+" percent chance of snow, It is "+str(parsed_data["data"][0]["temp"])+" celcius now, and "+str(parsed_data["data"][0]["precip"])+" percent chance of precipitation.", lang='en')
        tts.save("tr.mp3")
        os.system("mpg321 tr.mp3")
    elif 'tell me the news' in r.recognize_google(audio):
        try:
            er = EventRegistry(apiKey = "89eefbe9-ab8d-4d85-9286-f40fd3249e76", allowUseOfArchive = True)
            q = QueryArticlesIter(keywords = QueryItems.AND["bunny","bunnies","rabbit","rabbits"], dataType = ["news", "pr"])
            for article in q.execQuery(er, sortBy="date", sortByAsc=False, maxItems=1):
                tts = gTTS(text=article, lang='en')
                tts.save("tr.mp3")
                os.system("mpg321 tr.mp3")
        except:
            tts = gTTS(text="There is no news about bunnies.", lang='en')
            tts.save("tr.mp3")
            os.system("mpg321 tr.mp3")
    else:
        tts = gTTS(text="I didn't get that, say that again?", lang='en')
        tts.save("tr.mp3")
        os.system("mpg321 tr.mp3")

#tts = gTTS(text=r.recognize_google(audio), lang='en')
#tts.save("tr.mp3")
#os.system("mpg321 tr.mp3")
