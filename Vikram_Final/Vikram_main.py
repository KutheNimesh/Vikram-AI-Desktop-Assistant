import datetime
from email import message
import webbrowser
from numpy import tile
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
import pyglet
import timea
from NewsRead import latestnews
import wolframalpha 


# Your code here

# from Searchnow import searchGoogle
# from Searchnow import searchYoutube
# from Searchnow import searchWikipedia
#Paste this just below your import files
# for i in range(3):
#     a = input("Enter Password to open Vikram :- ")
#     pw_file = open("Vikram_Final/password.txt","r")
#     pw = pw_file.read()
#     pw_file.close()
#     if (a==pw):
#         print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
#         break
#     elif (i==2 and a!=pw):
#         exit()
#     elif (a!=pw):
#         print("Try Again")

from INTRO import play_gif
play_gif              
               


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
############################################## Alarm ###################################################
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("Vikram_Final\\alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                
                #################### Vikram: THe Trilogy 2.0 ##f###################

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
##################### schedule my day ############################
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("Vikram_Final/tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("Vikram_Final/notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\admin\\Desktop\\testingg\\Vikram_Final\\Vikram_Final\\FocusMode.py")
                    exit()    
                    

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("Vikram","")
                    query = query.replace("translate","")
                    translategl(query)

############ OPEN ANY APP AND WEBSITE ###############

                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("Vikram","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")            
                     
                     
                elif "internet speed" in query:
                    wifi  = wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                    

             
                
                elif "play a game" in query:
                    from game import game_play
                    game_play()
########################################### GUI ##################################################
                elif "screenshot" in query:
                     import pyautogui #pip install pip install requests
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

            
############################################################Conversation with AI###############
                elif "Hii" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
################################### Music ##########################
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:\
                        webbrowser.open("https://www.bing.com/videos/riverview/relatedvideo?&q=yodha+movie+songs&&mid=5D9B068E4CA53C90056E5D9B068E4CA53C90056E&&FORM=VRDGAR")
             ###########################play music########################
              #play music
                elif "play music" in query:
                    music_dir = r"C:\Users\Mayuri\Desktop\Vikram_Final-20240408T075108Z-001\Vikram_Final\Music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
                    while True:
                        query = takeCommand().lower()
#  # Stop music
#                 if "stop music" in query:
#                     pyautogui.press('enter')
#                     speak("Music stopped")
#                     break


#new functions
                elif "press enter" in query:
                    pyautogui.press("enter")
                elif "click on the search bar" in query:
                    pyautogui.moveTo (806, 125, 1)
                    pyautogui.click(x=806, y=125, clicks=1, interval=0, button='left')
                elif "open new tab" in query:
                    pyautogui.hotkey ("ctrl", "n")
                elif 'open incognito window' in query:
                    pyautogui.hotkey("ctrl", "shift", "n")
                elif 'open history' in query:
                    pyautogui.hotkey ("ctri", "h")
                elif "open downloads" in query:
                    pyautogui.hotkey("ctrl", "3")
                elif 'previous tab' in query:
                    pyautogui.hotkry("ctrl", "shift")
                elif "next tab" in query:
                    pyautogui.hotkey ("ctrl", "tab")
                elif 'close tab' in query:
                    pyautogui.hotkey ("ctrl", "w")
                elif 'clear browsing history' in query:
                    pyautogui.hotkey("ctrl","shift")






              ############################### #Youtube controls#############################mfKM#######
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")                                                    
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                elif "full screen" in query:
                    pyautogui.press("f")
                    speak("going full screen")
                elif "exit full screen" in query:
                    pyautogui.press("F")
                    speak("exiting full screen")
                elif "go forward" in query:
                    pyautogui.press("l")
                    speak("going forward 10 second")
                elif "go back" in query:
                    pyautogui.press("j")
                    speak("going back 10 seconds")
                elif "increase" in query:
                    pyautogui.hotkey('shift','.')
                    speak("playback speed incresing") 
                elif "decrease" in query:
                    pyautogui.hotkey('shift',',')
                    speak("playback speed decresing")  
                elif "next video" in query:
                    pyautogui.hotkey('shift','n')
                    speak("playing next video")
                    
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
####################################f###SEARCH ON GOOGLE, YOUTUBE ,  WEKIPEDIA###>#N##########################
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                #Open and Close apps/websites 
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "Vikram" in query:
                    print("yes sir")
                    print("yes sir")

                elif "type" in query: #0
                    query = query.replace("type","")
                    pyautogui.typewrite(f"{query}",0.1)
                
###############################################NEWS#####################################################

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                    
#########################################calculate#######################################################
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("Vikram","")
                    Calc(query)

                elif "whatsapp" in query:
                    webbrowser.open("https://web.whatsapp.com")
                    print("WhatsApp Web opened!")
                elif "type Mesaage" in query: #0
                    query = query.replace("type Mesaage","")
                    pyautogui.typewrite(f"{query}",0.1)

                
#########################################AUTO DETECT #############################################
                elif "temperature" in query:
                    search = "temperature in Maharashtra"
                    url =f"https://www.google.co.in/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text       
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in Maharashtra"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
#################################################set an alarm########################################################################
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
 ####################################################time###############################################################################                          
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
#################################### remember that ##########################################################
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Vikram","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
####################################### shutdown system ########################################
                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                




                


 