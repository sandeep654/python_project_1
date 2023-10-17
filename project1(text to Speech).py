# Start by importing the win32com package
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
print("")
#just write what you want me to speak : 
while(True):
    text=input("Enter what you want me to speak: ")
    if text == "Quit":
        speak.Speak("You Quit, Bye friend see you later take care")
        break
    speak.Speak(text)