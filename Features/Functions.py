import datetime
from time import sleep
import keyboard
import requests
from bs4 import BeautifulSoup
import os
from pywikihow import search_wikihow
import pyautogui
import speech_recognition as sr
from googletrans import Translator
import datetime
from datetime import date
from PyDictionary import PyDictionary
import webbrowser
import geocoder
import wikipedia
import pywhatkit
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import wolframalpha
from PIL import Image
import speedtest
import pyjokes

#---- These are Some Functions That Will FullFill Your Requirment.

#---- Website opener Function - Done

def LaunchWebsite(name):
    url = str(name).replace("launch ","")
    url = str(url).replace("visit ","")
    Say(f"Opening The Website : {url}")
    import webbrowser

    if "facebook" in url:
        webbrowser.open("https://www.facebook.com")

    elif "instagram" in url:
        webbrowser.open("https://www.instagram.com")

    elif "YouTube" in url:
        webbrowser.open("https://www.youtube.com")

    elif "drive" in url:
        webbrowser.open("https://drive.google.com/")

    elif "gmail" in url:
        webbrowser.open("https://mail.google.com/mail/")

    elif "twitter" in url:
        webbrowser.open("https://twitter.com/")

    else:
        url2 = "https://www." + str(url).replace(" ","") + ".com"
        webbrowser.open(url2)

#---- Open Apps Function - Done

def ApplicationOpener(name):
    typo = str(name).replace("open ","")
    typo = str(typo).replace("start ","")
    import pyautogui

    if "chrome" in typo:
        pyautogui.hotkey("win")
        sleep(1)
        pyautogui.write(typo)
        sleep(1)
        pyautogui.press('enter')
        import keyboard
        keyboard.press_and_release("alt + space")
        pyautogui.press("x")

    else:
        pyautogui.hotkey("win")
        sleep(1)
        pyautogui.write(typo)
        sleep(1)
        pyautogui.press('enter')   

#---- Make notes Function - Done

def NotesMaker():
    Say("Tell Me, What To Note ?")
    note = Listen()
    ApplicationOpener('notepad')
    sleep(1)
    import pyautogui
    pyautogui.write(note)
    import keyboard
    keyboard.press_and_release("ctrl + s")
    sleep(2)
    date = datetime.datetime.now().strftime("%H-%M-%M")
    keyboard.write(f"{date}.txt")
    keyboard.press('enter')
    sleep(1)
    keyboard.press_and_release("alt + f4")

#---- Typing Function - Done

def TypeFunction():
    Say("What You Want Me To Type Sir ?")
    typeeee = Listen()
    import keyboard
    keyboard.write(typeeee)
    
#---- System Specification Function - Done

def SystemInfo():
    import platform
    info = {}
    platform_details = platform.platform()
    info["platform details"] = platform_details
    system_name = platform.system()
    info["system name"] = system_name
    processor_name = platform.processor()
    info["processor name"] = processor_name
    architecture_details = platform.architecture()
    info["architectural detail"] = architecture_details
    for i, j in info.items():
        Say(i)
        Say(j)

#---- IP ADDress Teller Function - Done

def IpAdd():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    Say("Your Computer Name is:" + hostname)
    Say("Your Computer IP Address is:" + IPAddr)

#---- Zoom In Function - Done

def ZoomIn():
    import keyboard
    keyboard.press_and_release("ctrl + plus")

#---- Zoom Out Function - Done

#def ZoomOut():
#    import keyboard
#    keyboard.press_and_release("ctrl + -")

#---- Weather Function - Done

def Temperature(Name):
    se = f"temperature in {Name}"
    url = f"https://www.google.com/search?q={se}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    Say(f"Temperature In {Name} Is {temp} .")

#---- Screen Shot Function - Done

def Screenshot():
    Say("What Should I Name That File ?")
    FileName = Listen()
    path1name = str(FileName) + ".png"
    kk = pyautogui.screenshot()
    kk.save(path1name)
    os.startfile(path1name)

#---- Time Function - Done

def TimeFunction():
    time = datetime.datetime.now().strftime("%H:%M")
    return time

#---- Date Function - Done

def DateFunction():
    date = datetime.date.today()
    return date

#---- Day Function - Done

def DayFunction():
    import datetime
    today = datetime.datetime.now().strftime("%A")

    Say(f"Today's Is : {today} .")

#---- Year Function - Done

def YearFunction():

    today = date.today()

    year = today.strftime("%Y")

    Say(f"This Is Year : {year} .")

#---- Dictionary Function - Done

def Dictionary(Word):

    Command = str(Word)

    Diction = PyDictionary()

    if 'synonym' in Command:
        Word = Command.replace("synonym of ","")
        synon = Diction.synonym(Word)
        Say(f"Synonym Of {Word} Is {synon} .")

    elif 'antonym' in Command:
        Word = Command.replace("antoynm of ","")
        anton = Diction.antonym(Word)
        Say(f"Antonym Of {Word} Is {anton} .")

    elif 'meaning' in Command:
        Word = Command.replace("meaning of ","")
        mean = Diction.meaning(Word)
        Say(f"The Meaning Of {Word} Is {mean} .")

#---- Map Automation Function - Done

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    webbrowser.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    Say(target)
    Say(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

#---- Scroll Down Function. - Done

def ScrollDown():

    keyboard.press('pagedown')
    sleep(0.5)
    keyboard.press('pagedown')
    sleep(0.5)
    keyboard.press('pagedown')

#---- Scroll UP Function. - Done

def ScrollUp():

    keyboard.press('up')
    sleep(0.5)
    keyboard.press('up')
    sleep(0.5)
    keyboard.press('up')
    sleep(0.5)
    keyboard.press('up')

#---- Woflram Aplha API Function - Done

def Wolfram(query):
    
    api = "LWGWYQ-WQVK6X2XJL"

    requester = wolframalpha.Client(api)

    request = requester.query(query)

    try:
        
        answer = next(request.results).text

        Say(answer)

    except:

        Say("I am Really Sorry Sir. I Can Not Access The Answer!")

#---- Calulator  - Done

def Calculator(Problem):

    r = str(Problem)

    kk = Wolfram(r)

    Say(kk)

#---- Google Search Function - Done

def GoogleSearch(Topic):

    if 'how to' in Topic:
        Say("Getting Data From The Internet !")
        op = Topic.replace("maverick","")
        max_result = 1
        how_to_func = search_wikihow(op,max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Say(how_to_func[0].summary)

    else:
        import wikipedia as googleScrap
        query = Topic.replace("maverick","")
        query = Topic.replace("google search","")
        query = Topic.replace("google","")
        query = Topic.replace("what is ","")
        query = Topic.replace("who is ","")
        Say("This Is What I Found On The Web!")
        pywhatkit.search(query)

        try:
            result = googleScrap.summary(query,2)
            Say(result)

        except:
            Say("No Speakable Data Available!")

#---- Wikipedia Function - Done

def Wikipedia(Topic):

    Topic = str(Topic).replace("what is ","")

    resd = wikipedia.summary(Topic,2)

    Say(f"According To My Research : {resd}")

#---- YouTube Search Function - Done

def YouTubeSearch(Topic):
        Say("Ok Sir , Searching..")
        query = Topic.replace("youtube search","")
        url = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open_new_tab(url)
        pywhatkit.playonyt(Topic)

#---- Repeatme Function - Done

def RepeatMe():
    Say("What You Want Me To Repeat ?")
    rep = Listen()
    Say(f"You Said : {rep} .")
    Say("Thanks .")

#---- Jokes Function - Done

def Jokes():
    Joke = pyjokes.get_jokes(language='en')
    Say(Joke)

#--------------------------------------------------------------------------------------------------------------------------------------

#---- Maverick Will Listen Through This Function :-

def Listen():

    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,3)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")
        print(" ")

    except:
        return ""

    return query.lower()

#---- Maverick Will Speak Through This Function :-

def Say(audio):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',190)
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("")

#---- This Function Will Help You To Verify a Function and Tell You A Query About Your Query

def FTasker(Tasks,Command):

    Tasks = str(Tasks)
    
    Command = str(Command)

    if "time" in Tasks:
        time = datetime.datetime.now().strftime("%H:%M")
        Say(time)

    elif "date" in Tasks:
        date = datetime.date.today()
        Say(date)

    elif "launch" in Tasks:
        LaunchWebsite(Command)

    elif "open" in Tasks:
        ApplicationOpener(Command)

    elif "note" in Tasks:
        NotesMaker()
    
    elif "type" in Tasks:
        TypeFunction()

    elif "day" in Tasks:
        DayFunction()

    elif "year" in Tasks:
        YearFunction()

    elif "temp" in Tasks:
        name = str(Command).replace("temperature in ","")
        name = str(name).replace("weather in ","")
        Temperature(name)

    elif "ss" in Tasks:
        Screenshot()

    elif "sys" in Tasks:
        SystemInfo()

    elif "in" in Tasks:
        ZoomIn()

    #elif "out" in Tasks:
    #    ZoomOut()

    elif "scup" in Tasks:
        ScrollUp()

    elif "scdown" in Tasks:
        ScrollDown()

    elif "ipadd" in Tasks:
        IpAdd()

    elif "dict" in Tasks:
        Dictionary(Command)

    elif "locate" in Tasks:
        place = str(Command).replace("where is ","")
        place = str(place).replace("locate ","")
        GoogleMaps(place)

    elif "calculate" in Tasks:
        cmd_12371283 = str(Command).replace("calculate ","")
        cmd_12371283 = str(cmd_12371283).replace("calculator ","")
        Calculator(cmd_12371283)

    elif "search" in Tasks:
        cmd_2342348 = str(Command).replace("google search ","")
        cmd_2342348 = str(cmd_2342348).replace("google ","")
        cmd_2342348 = str(cmd_2342348).replace("search ","")
        GoogleSearch(cmd_2342348)

    elif "wiki" in Tasks:
        realcmd = str(Command).replace("wikipedia ","")
        Wikipedia(realcmd)

    elif "alarm" in Tasks:
        os.startfile("My System\\Features\\Alarm.py")

    elif "joke" in Tasks:
        Jokes()

    elif "youtube" in Tasks:
        comnd = str(Command).replace("youtube search ","")
        YouTubeSearch(comnd)
