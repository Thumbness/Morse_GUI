from tkinter import *
import tkinter.font
import time

from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)


## hardware ##
redled = LED(17)


## GUI DEFINITIONS ##
win = Tk()
win.title("LED Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')
win.geometry('400x200')

## EVENT FUNCTIONS ##
print("starting")

def getInput():
    processinglbl["text"] = "processing output to LED"
    INPUT = usertext.get() ## get input from user
    print(INPUT)
    if(len(INPUT) >= 13):
        processinglbl["text"] = "Too many letters, must be less than 12."
        print("too many letters")
    else:
        word_list = list(INPUT) ## place each letter in input to own element in list
        processinglbl["text"] = "Morse Code Processed"
        for inputLetter in word_list: 
            for listLetter in alphabetLetters:
                if inputLetter == listLetter: ##comparing letter in user input word to letter in alphabet list
                    print(inputLetter)
                    x = alphabetLetters.index(inputLetter) ## getting index of alphabet list element
                    print(x)
                    morseCodeLetters[x]() ## passing index to list of morse code functions that align with letter
                    inter() ## between letter character delay gap

def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
## MORSE CODE LETTER FUNCTIONS ##
def intra():
    time.sleep(.2)
def inter():
    time.sleep(.6)
def dot():
    redled.on()
    intra()
    redled.off()
    intra() 
def dash():
    redled.on()
    inter()
    redled.off()
    intra()

def A():
    dot()
    dash()
    
def B():
    dash()
    dot()
    dot()
    dot()
    
def C():
    dash()
    dot()
    dash()
    dot()
    
def D():
    dash()
    dot()
    dot()

def E():
    dot()

def F():
    dot()
    dot()
    dash()
    dot()
    
def G():
    dash()
    dash()
    dot()
    
def H():
    dot()
    dot()
    dot()
    dot()
    
def I():
    dot()
    dot()
    
def J():
    dot()
    dash()
    dash()
    dash()
    
def K():
    dash()
    dot()
    dash()
    
def L():
    dot()
    dash()
    dot()
    dot()
    
def M():
    dash()
    dash()
    
def N():
    dash()
    dot()
    
def O():
    dash()
    dash()
    dash()
    
def P():
    dot()
    dash()
    dash()
    dot()
    
def Q():
    dash()
    dash()
    dot()
    dash()
    
def R():
    dot()
    dash()
    dot()
    
def S():
    dot()
    dot()
    dot()
    
def T():
    dash()
    
def U():
    dot()
    dot()
    dash()
    
def V():
    dot()
    dot()
    dot()
    dash()
    
def W():
    dot()
    dash()
    dash()
    
def X():
    dash()
    dot()
    dot()
    dash()
    
def Y():
    dash()
    dot()
    dash()
    dash()
    
def Z():
    dash()
    dash()
    dot()
    dot()


morseCodeLetters = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z] ## stores morse code letter functions in list
alphabetLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] ##stores individual string letters for indexing

### WIDGETS ###
    
##Header
info = tkinter.Label(win, text = "Enter maximum 12 letter word")
info.pack()
##Text Box

usertext = Entry(win)
usertext.pack()

executeButton = Button(win, text = "Execute", font = myFont, command = getInput, bg = "red", height = 2, width = 10)
executeButton.pack()

processinglbl = tkinter.Label(win, text = "Awaiting input.....")
processinglbl.pack()

exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = "white", height = 1, width = 10)
exitButton.pack()
                    
win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()