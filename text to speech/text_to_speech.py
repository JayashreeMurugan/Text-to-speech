import pyttsx3
import os
myFile=open("python.txt","r")
myText=myFile.read()

voice = pyttsx3.init()
myText="Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI. Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python. The name Tkinter comes from Tk interface."
voice.say(myText)
voice.save_to_file(myText,"python.mp3")
voice.runAndWait()
os.system("start python.mp3")