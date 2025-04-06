import pyttsx3
import speech_recognition as sr 
import webbrowser
import datetime
import pyjokes
import pyaudio
import time

#speech to text
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            #print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""

def speechtx(x):
    engine = pyttsx3.init()

    #voice propert, 0 is for male, 1 is for female
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)


    #to set the speed of the voice , if not defined program will take the default value
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)

    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__' :

    if "hey peter" in sptext().lower():
        while True:
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is peter"
                speechtx(name)
            elif "old are you" in data1:
                age = " i am one month old"
                speechtx(age)
            elif 'now time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)
            elif "exit" in data1:
                speechtx("Thankyou")
                break
            time.sleep(5)

    else:
        print("Thanks")
