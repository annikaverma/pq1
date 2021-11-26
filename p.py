from tkinter import *
import speech_recognition as sr
root = Tk()
root.geometry(500x500")
def r_audio():
    speech_recognisor= sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recognisor
        voice_data=''
        try:
            voice_data= speech_recognisor.recognise_google(audio, language='en-in')
        except sr.UnknownValueError:
            print(voice_data)

r_audio()
root.mainloop()
