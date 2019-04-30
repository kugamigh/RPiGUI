from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#led = LED(14)
blue = LED(14)
red = LED(15)
yellow = LED(18)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def blueToggle():
    if blue.is_lit:
        blue.off()
        blueButton["text"]="Turn blue on"
    else:
        blue.on()
        blueButton["text"]="Turn blue off"
        
def redToggle():
    if red.is_lit:
        red.off()
        redButton["text"]="Turn red on"
    else:
        red.on()
        redButton["text"]="Turn red off"
        
def yellowToggle():
    if yellow.is_lit:
        yellow.off()
        yellowButton["text"]="Turn yellow on"
    else:
        yellow.on()
        yellowButton["text"]="Turn yellow off"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
blueButton = Button(win, text='Turn blue on', font=myFont, command=blueToggle, bg='bisque2', height=1, width=24)
blueButton.grid(row=0, column=1)

redButton = Button(win, text='Turn red on', font=myFont, command=redToggle, bg='bisque2', height=1, width=24)
redButton.grid(row=1, column=1)

yellowButton = Button(win, text='Turn yellow on', font=myFont, command=yellowToggle, bg='bisque2', height=1, width=24)
yellowButton.grid(row=2, column=1)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=4, column=1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
