import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your_api"



def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiProcess(command):
  client = OpenAI(
    api_key="your_api_keys"

  )
  completion = client.chat.completions.create(
     model ="gpt-3.5-turbo",
         messages=[
            {"role": "system", "content": "You are a virtual assistant."},
            {"role": "user", "content": command}
        ],
)
  return completion.choices[0].message.content

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://www.linkedin.com/in/vashu-sharma01/")
   elif "open portfolio" in c.lower():
      webbrowser.open("https://vashu-sharma.netlify.app/")
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = musicLibrary.music[song]
      webbrowser.open(link)

   elif "news" in c.lower():
      r = requests.get("https://newsapi.io/v2/top-headlines?/country=india?apikey={newsapi}") 
      data = r.json()

      #extract the articles
      articles = data.get('articles',[])  
      #print the articles
      for article in articles:
         speak(article)['title']
   else:
      #let openAi handle the req
      output = aiProcess(c)
      speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
      #listen to the wake word "Jarvis"
        #obtain audio from the microphone
      r = sr.Recognizer()
      print("Recognizing...")

    #recognize speech google 
      try:
        with sr.Microphone() as source:
           print("Listning...")
           audio = r.listen(source,timeout=2,phrase_time_limit=1)

        word = r.recognize_google(audio)
        if(word.lower()=="jarvis"):
           speak("Ya")

           #listen for command
           with sr.Microphone() as source:
            print("jarvis Active...")
            audio = r.listen(source)
            command= r.recognize_google(audio)

           processCommand(command)
            
     
      except Exception as e:
        print("Voice error ; {0}".format(e))
