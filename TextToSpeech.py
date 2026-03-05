from tkinter import *
import os
from gtts import gTTS
window = Tk()
window.geometry("600x600")
window.title("Text To speech")
window.config(bg = "red")

def TextToSpeech():
    language = "en"
    myObject = gTTS(text = TextEntry.get(), lang = language, slow = False)
    myObject.save("MySpeech.wav")
    os.system("MySpeech.wav")

frame1 = Frame(window, bg = "dark blue", height = "200")
frame2 = Frame(window, bg = "blue", height = "400")
Heading = Label(frame1, text = "text to speech", bg = "dark blue", fg = "light blue", font = ("Ariel", 30))
EnterLabel = Label(frame1, text = "enter text here: ", bg = "dark blue", fg = "light blue", font = ("Ariel", 15))
TextEntry = Entry(frame1, width = 30, bg = "light blue", fg = "blue")
SubmitButton = Button(frame2, text = "submit", bg = "dark blue", fg = "light blue", command = TextToSpeech)

frame1.pack(fill = X)
frame2.pack(fill = X)
Heading.place(x = 180, y = 75)
EnterLabel.place(x = 150, y = 120)
TextEntry.place(x = 300, y = 128)
SubmitButton.place(x = 300, y = 200)


window.mainloop()