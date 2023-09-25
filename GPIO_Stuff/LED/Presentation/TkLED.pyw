import RPi.GPIO as GPIO
import tkinter as tk
from pynput import keyboard

def for_canonical(c):
    return lambda k: c(l.canonical(k))
#Create window
root = tk.Tk()
root.attributes("-fullscreen", True)
root['bg'] = "black"
tk.Label(root, text="LED Fun!", fg='white', bg="black").grid(row=0)

#Setup GPIOs
r = 17
g = 18
y = 22
b = 23
o = 26
w = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(y, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(o, GPIO.OUT)
GPIO.setup(w, GPIO.OUT)

#LED Function
def led_on_off():
    var_list = []
    count = 1
    var_list.append(r_var.get())
    var_list.append(g_var.get())
    var_list.append(y_var.get())
    var_list.append(b_var.get())
    var_list.append(o_var.get())
    var_list.append(w_var.get())
    for t in var_list:
        if count == 1:
            if t == 1:
                GPIO.output(r, True)
            elif t == 0:
                GPIO.output(r, False)
        elif count == 2:
            if t == 1:
                GPIO.output(g, True)
            elif t == 0:
                GPIO.output(g, False)
        elif count == 3:
            if t == 1:
                GPIO.output(y, True)
            elif t == 0:
                GPIO.output(y, False)
        elif count == 4:
            if t == 1:
                GPIO.output(b, True)
            elif t == 0:
                GPIO.output(b, False)
        elif count == 5:
            if t == 1:
                GPIO.output(o, True)
            elif t == 0:
                GPIO.output(o, False)
        elif count == 6:
            if t == 1:
                GPIO.output(w, True)
            elif t == 0:
                GPIO.output(w, False)
        count += 1
        
#Hotkey functions
r_state = False
g_state = False
y_state = False
b_state = False
o_state = False
w_state = False

def r_hotkey():
    global r_state
    if r_state == False:
        r_state = True
        GPIO.output(r, r_state)
    elif r_state == True:
        r_state = False
        GPIO.output(r, r_state)
def g_hotkey():
    global g_state
    if g_state == False:
        g_state = True
        GPIO.output(g, g_state)
    elif g_state == True:
        g_state = False
        GPIO.output(g, g_state)
def y_hotkey():
    global y_state
    if y_state == False:
        y_state = True
        GPIO.output(y, y_state)
    elif y_state == True:
        y_state = False
        GPIO.output(y, y_state)
def b_hotkey():
    global b_state
    if b_state == False:
        b_state = True
        GPIO.output(b, b_state)
    elif b_state == True:
        b_state = False
        GPIO.output(b, b_state)
def o_hotkey():
    global o_state
    if o_state == False:
        o_state = True
        GPIO.output(o, o_state)
    elif o_state == True:
        o_state = False
        GPIO.output(o, o_state)
def w_hotkey():
    global w_state
    if w_state == False:
        w_state = True
        GPIO.output(w, w_state)
    elif w_state == True:
        w_state = False
        GPIO.output(w, w_state)
#add hotkeys
r_keystroke = keyboard.HotKey(keyboard.HotKey.parse('<shift>+r'), r_hotkey)

with keyboard.Listener(on_press=for_canonical(r_keystroke.press), on_release=for_canonical(r_keystroke.release)) as l:
    l.join()
#Checkbutton Tracking Vars
r_var = tk.IntVar()
g_var = tk.IntVar()
y_var = tk.IntVar()
b_var = tk.IntVar()
o_var = tk.IntVar()
w_var = tk.IntVar()
#Checkbuttons
r_b = tk.Checkbutton(foreground="black", background="#f00", text="RED", activebackground="black", activeforeground="#f00", variable=r_var).grid(row=1, sticky='we')
g_b = tk.Checkbutton(foreground="black", background="#0f0", text="GREEN", activebackground="black", activeforeground="#0f0", variable=g_var).grid(row=2, sticky='we')
y_b = tk.Checkbutton(foreground="black", background="#ff0", text="YELLOW", activebackground="black", activeforeground="#ff0", variable=y_var).grid(row=3, sticky='we')
b_b = tk.Checkbutton(foreground="black", background="#0ff", text="BLUE", activebackground="black", activeforeground="#00f", variable=b_var).grid(row=4, sticky='we')
o_b = tk.Checkbutton(foreground="black", background="#ffa500", text="ORANGE", activebackground="black", activeforeground="#ffa500", variable=o_var).grid(row=5, sticky='we')
w_b = tk.Checkbutton(foreground="black", background="#fff", text="WHITE", activebackground="black", activeforeground="#fff", variable=w_var).grid(row=6, sticky='we')
button = tk.Button(root, text="COMMIT", foreground="black", background="#fff", command=led_on_off).grid(row=7)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)

tk.mainloop()