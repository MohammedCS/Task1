# Import Tkinter 
from tkinter import *

# Creat the tkinter window
window = Tk()

# Add title to the window
window.title("Task1: Control Sonoff Switches")

# Define the size of the window
window.geometry("500x300")

# Make the intial value for switches turn on
switch_1_state = True
switch_2_state = True

### Define the images required for the program
# Switches images 
SWITCH_ON  = PhotoImage(file = "on.png")
SWITCH_OFF = PhotoImage(file = "off.png")
# Bulbs images
BULB_ON  =  PhotoImage(file = "bulb_on.png")
BULB_OFF =  PhotoImage(file = "bulb_off.png")

##### Functions
"""
    Main idea is XNor Gate for stairway switching.

    switch_1   | switch_2    =>  bulb
    ___________________________________
    On         | On          =>  On 
    On         | Off         =>  Off
    Off        | On          =>  Off
    Off        | Off         =>  On 
"""
# function to take action when the switch 1 toggle
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
            bulb_state_text.config(text = "The Bulb is On",
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
            bulb_state_text.config(text = "The Bulb is On",
                                    fg = "green")

# function to take action when the switch 2 toggle
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
            bulb_state_text.config(text = "The Bulb is On",
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
            bulb_state_text.config(text = "The Bulb is On",
                                    fg = "green")

# Define switch_1 and its properties
switch_1 = Button(window,       # Define the main window 
    image = SWITCH_ON,          # Define its image
    bd = 0,                     # No border
    command = toggle_switch_1)  # Define the action (function)
switch_1.pack(side = RIGHT)     # Define its place in the window

# Define switch_2 and its properties
switch_2 = Button(window,       # Define the main window
    image = SWITCH_ON,          # Define its image
    bd = 0,                     # No border
    command = toggle_switch_2)  # Define the action (function)
switch_2.pack(side = LEFT)      # Define its place in the window

# Define bulb and its properties
bulb = Label(window,            # Define the main window
    image = BULB_ON)            # Define its image
bulb.pack(side = BOTTOM)        # Define its palce in the window

# Define the text that appear in the program
bulb_state_text = Label(window,     # Define the main window
    text = "The Bulb Is On",        # The text 
    fg  = "green",                  # Foreground color
    font = ("Helvetica", 30))       # Font and font_size
bulb_state_text.pack(side = TOP)    # Define its place in the window  

# Start the program (Tkinter)
window.mainloop()