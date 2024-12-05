from tkinter import *
from tkinter import ttk
import tkSnack
import threading
import time

#tone = 0, tap = 1
tapOrTone = 0
currentDelay = 500

class soundThread(threading.Thread):
    def run(self):
        self.end = False
        self.play = True
        while not self.end:
                while self.play:
                    soundPlay()
                    time.sleep(0.5)

s = soundThread()    

def startB():
    global running
    running = True
    s.play = running
    playMetronome()

def stopB():
    global running
    running = False
    s.end = True

def playMetronome():
    if running:
        if not s.is_alive():
            s.start()
    else:
        print('STOP')
       

def chooseSound():
    global tapOrTone
    if tapOrTone == 0:
        tapOrTone = 1
    else:
        tapOrTone = 0

def initializeSound():
    global ta
    ta = tkSnack.Sound()
    ta.read('tap.wav')
    global to
    to = tkSnack.Sound()
    to.read('tone.wav')

def soundPlayTap():
    print('Tap played')
    ta.play()

def soundPlayTone():
    print('Tone played')
    to.play()

def soundPlay():
    if tapOrTone == 1:
        soundPlayTap()
    else:
        soundPlayTone()

root = Tk()
tkSnack.initializeSnack(root)
initializeSound()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Metronome").grid(column=0, row=0)
ttk.Button(frm, text="Start", command=startB).grid(column=0, row=1)
ttk.Button(frm, text="Stop", command=stopB).grid(column=0, row=2)
ttk.Button(root, text="Toggle sound type", command=chooseSound).grid(column=0,row=3)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)
root.mainloop()