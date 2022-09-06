# Import Tkinter 
from tkinter import *

# Creat the tkinter window
window = Tk()

# Add title to the window
window.title("Task1: Control Sonoff Switches")

# Define the size of the window

window.geometry("500x300")

# Make the intial value for buttons turn on
switch_1_state = True
switch_2_state = True

SWITCH_ON  = PhotoImage(file = "on.png")
SWITCH_OFF = PhotoImage(file = "off.png")

BULB_ON  =  PhotoImage(file = "bulb_on.png")
BULB_OFF =  PhotoImage(file = "bulb_off.png")

def toggle_switch_1():
    global switch_1_state 

    if  switch_1_state:
        switch_1.config(image = SWITCH_OFF)
        switch_1_state = False

        if switch_2_state:
            bulb.config(image = BULB_OFF)
            bulb_state_text.config(text = "The Bulb is Off",
                                    fg = "grey")
        else:
            bulb.config(image = BULB_ON)
            bulb_state_text.config(text = "The Bulb is on",
                                    fg = "green")
    else:
        switch_1.config(image = SWITCH_ON)
        switch_1_state = True

        if not switch_2_state:
            bulb.config(image = BULB_OFF)
            bulb_state_text.config(text = "The Bulb is Off",
                                    fg = "grey")
        else:
            bulb.config(image = BULB_ON)
            bulb_state_text.config(text = "The Bulb is on",
                                    fg = "green")
               
def toggle_switch_2():
    global switch_2_state 

    if  switch_2_state:
        switch_2.config(image = SWITCH_OFF)
        switch_2_state = False

        if  switch_1_state:
            bulb.config(image = BULB_OFF)
            bulb_state_text.config(text = "The Bulb is Off",
                                    fg = "grey")
        else:
            bulb.config(image = BULB_ON)
            bulb_state_text.config(text = "The Bulb is on",
                                    fg = "green")
    else:
        switch_2.config(image = SWITCH_ON)
        switch_2_state = True

        if  not switch_1_state:
            bulb.config(image = BULB_OFF)
            bulb_state_text.config(text = "The Bulb is Off",
                                    fg = "grey")
        else:
            bulb.config(image = BULB_ON)
            bulb_state_text.config(text = "The Bulb is on",
                                    fg = "green")

switch_1 = Button(window,
    image = SWITCH_ON,
    bd = 0, # no border
    command = toggle_switch_1)
switch_1.pack(side = RIGHT)

switch_2 = Button(window, 
    image = SWITCH_ON,
    bd = 0,
    command = toggle_switch_2)
switch_2.pack(side = LEFT)

bulb = Label(window,
    image = BULB_ON)
bulb.pack(side = BOTTOM)

bulb_state_text = Label(window,
    text = "The Bulb Is On",
    fg  = "green",
    font = ("Helvetica", 30))
bulb_state_text.pack(side = TOP)

window.mainloop()