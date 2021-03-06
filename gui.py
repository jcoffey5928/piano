#!/usr/bin/env python3
#Name: gui.py
#Purpose: View for the user to interact with which calls the controller.         
#Developer: Jonathan Coffey

from tkinter import *
from tkinter import ttk
from keyboard import Keyboard

class Gui:
    def __init__(self, master, controller):
        self.master = master
        self.master.title('Piano')
        self.master.resizable(False, False)
        self.master.configure(background="black")

        self.controller = controller
        self.controller.setGui(self)
        self.song = self.controller.getCurrentSong().getTitle()
        self.songText = StringVar()
        self.songText.set(self.song)
        self.key = self.controller.getCurrentKey()
        self.keyText = StringVar()
        self.keyText.set(f"Key: {self.key}")
        self.lightColor = Keyboard.KEY_COLORS.get(self.key) 

        self.style = ttk.Style()
        self.style.configure("TFrame", background="black")
        self.style.configure("Pl.TButton", background="green", padding=6)
        self.style.configure("Pr.TButton", background="grey", padding=6)
        self.style.configure("N.TButton", background="grey", padding=6)
        self.style.configure("KB.TButton", background="yellow", padding=6)
        self.style.configure("H.TButton", background="blue", padding=6)
        self.style.configure("S.TLabel", textvariable=self.songText, background="black", foreground="white", font=("Consolas", 14), anchor="center")
        self.style.configure("K.TLabel", textvariable=self.keyText, background="black", foreground=self.lightColor, font=("Consolas", 14, "bold"), anchor="center")

        self.createInfoFrame()
        self.createSongControlFrame()
        self.createModeControlFrame()

    def createInfoFrame(self):
        contentFrame = ttk.Frame(self.master, style="TFrame")
        contentFrame.pack()
        self.songLabel = ttk.Label(contentFrame, textvariable=self.songText, width=50, style="S.TLabel").grid(row=0, column=0)
        self.keyLabel = ttk.Label(contentFrame, textvariable=self.keyText, style="K.TLabel").grid(row=1,column=0)

    def createSongControlFrame(self):
        buttonFrame = ttk.Frame(self.master, style="TFrame")
        buttonFrame.pack()
        playButton = ttk.Button(buttonFrame, command=self.playSong, text="Play", style="Pl.TButton").grid(row=0, column=0)
        prevButton = ttk.Button(buttonFrame, command=self.prevSong, text="Previous", style="Pr.TButton").grid(row=0, column=1)
        nextButton = ttk.Button(buttonFrame, command=self.nextSong, text="Next", style="N.TButton").grid(row=0, column=2)

    def createModeControlFrame(self):
        modeFrame = ttk.Frame(self.master, style="TFrame")
        modeFrame.pack()
        keyboardButton = ttk.Button(modeFrame, command=self.startKeyboardMode, text="Keyboard Mode", style="KB.TButton").grid(row=1, column=0)
        learningButton = ttk.Button(modeFrame, command=self.startLearningMode, text="Learning Mode", style="KB.TButton").grid(row=1, column=1)
        self.helpButton = ttk.Button(modeFrame, command=self.playThreeNotes, text="Play 3 Notes", state=DISABLED, style="H.TButton")    
        self.helpButton.grid(row=1, column=2)

    def playSong(self):
        self.controller.playSong()

    def prevSong(self):
        self.controller.prevSong()
        self.reset()

    def nextSong(self):
        self.controller.nextSong()
        self.reset()

    def reset(self):
        self.song = self.controller.getCurrentSong()
        self.song = self.controller.getCurrentSong().getTitle()
        self.songText.set(self.song)
        self.updateKeyInfo()

    def updateKeyInfo(self):
        self.key = self.controller.getCurrentKey()
        self.keyText.set(f"Key: {self.key}")
        self.lightColor = Keyboard.KEY_COLORS.get(self.key) 
        self.style.configure("K.TLabel", foreground = self.lightColor)
        self.master.update_idletasks()
    
    def update(self):
        self.master.update_idletasks()

    def startKeyboardMode(self):
        print("\nStarting keyboard mode...")
        self.controller.playMode("keyboard")
        self.updateKeyInfo()

    def startLearningMode(self):
        #self.helpButton.state(["!disabled"])
        print("\nStarting learning mode...")
        self.controller.playMode("learning")
        self.updateKeyInfo()
        self.helpButton.state(["disabled"])
        self.update()
        print("End of learning mode")
    
    def playThreeNotes(self):
        self.controller.playThreeNotes()
