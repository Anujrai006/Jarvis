import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import time
import requests
recognizer=sr.Recognizer()
newsapi="pub_c6d486f10dc04c2fa7251fdad59fd23f"
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def process_command(c):
  if "open google" in c.lower():
     webbrowser.open("https://google.com")
     speak('opening gogole')
  elif "open youtube" in c.lower():
     webbrowser.open("https://youtube.com")
     speak("opening youtube")
  elif "open instagram" in c.lower():
     webbrowser.open("https://instagram.com")
     speak("opening instagram")
  elif c.lower().startswith("play"):
     song=c.lower().split(" ")[1]
     link=musiclibrary.music[song]
     webbrowser.open(link)
     speak(f"playing {song}")
     time.sleep(0.7)
  elif "news" in c.lower():
        try:
            r = requests.get(f'https://newsdata.io/api/1/latest?apikey={newsapi}&country=np&language=en')
            if r.status_code == 200:
                data = r.json()
                articles = data.get("results", [])
                if articles:
                    speak("Here are the top headlines:")
                    for article in articles[:9]:  # Only read 5 headlines
                        speak(article["title"])
                        print(article["title"])
                        time.sleep(0.3)
                else:
                    speak("Sorry, I could not find any news right now.")
            else:
                speak("Unable to fetch news right now.")
        except Exception as e:
            print("News error:", e)
            speak("There was a problem fetching the news.")
      
if __name__=="__main__":
   speak("Initializing jarvis....")


    
while True:
#  r=sr.Recognizer()
 print("recognizing.....")

 try:
    with sr.Microphone() as source:
         recognizer.adjust_for_ambient_noise(source)
         print("Listening....")
         audio=recognizer.listen(source,timeout=2,phrase_time_limit=1)
         word=recognizer.recognize_google(audio)
        #  print(word)
         if "jarvis" in word.lower():
          speak("yaa")
          time.sleep(0.8)
      
          print("Jarvis Activated.....")
         
         #  speak("jarvis activated")
          with sr.Microphone() as source:
           recognizer.adjust_for_ambient_noise(source)
           
           audio=recognizer.listen(source,timeout=2,phrase_time_limit=3)
        #    command=input("enter") By Semega workers
           command=recognizer.recognize_google(audio)
           print(command)
           process_command(command)
           time.sleep(1)
           speak("hunxa anuj aba voli vetum")

    
         

       
 except Exception as e:
    print("Error :{}".format(e))                          