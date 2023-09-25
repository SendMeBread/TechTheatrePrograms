import RPi.GPIO as GPIO
import tkinter as tk
import keyboard


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
def r_on():
    GPIO.output(r, True)
def r_off():
    GPIO.output(r, False)

def g_on():
    GPIO.output(g, True)
def g_off():
    GPIO.output(g, False)

def y_on():
    GPIO.output(y, True)
def y_off():
    GPIO.output(y, False)

def b_on():
    GPIO.output(b, True)
def b_off():
    GPIO.output(b, False)

def o_on():
    GPIO.output(o, True)
def o_off():
    GPIO.output(o, False)

def w_on():
    GPIO.output(w, True)
def w_off():
    GPIO.output(w, False)
    
#add hotkeys
keyboard.add_hotkey('r', r_on)
keyboard.add_hotkey('R', r_off)
keyboard.add_hotkey('g', g_on)
keyboard.add_hotkey('G', g_off)
keyboard.add_hotkey('y', y_on)
keyboard.add_hotkey('Y', y_off)
keyboard.add_hotkey('b', b_on)
keyboard.add_hotkey('B', b_on)
keyboard.add_hotkey('o', o_on)
keyboard.add_hotkey('O', o_off)
keyboard.add_hotkey('w', w_on)
keyboard.add_hotkey('W' w_off)

#Checkbutton Tracking Vars
r_var = tk.IntVar()
g_var = tk.IntVar()
y_var = tk.IntVar()
b_var = tk.IntVar()
o_var = tk.IntVar()
w_var = tk.IntVar()
#Checkbuttons
tk.Text(foreground="#fff", background="#000", text="Keybinds ON/OFF: r/R, g/G, y/Y, b/B, o/O, w/W")
r_b = tk.Checkbutton(foreground="black", background="#f00", text="RED", activebackground="black", activeforeground="#f00", variable=r_var).grid(row=2, sticky='we')
g_b = tk.Checkbutton(foreground="black", background="#0f0", text="GREEN", activebackground="black", activeforeground="#0f0", variable=g_var).grid(row=3, sticky='we')
y_b = tk.Checkbutton(foreground="black", background="#ff0", text="YELLOW", activebackground="black", activeforeground="#ff0", variable=y_var).grid(row=4, sticky='we')
b_b = tk.Checkbutton(foreground="black", background="#0ff", text="BLUE", activebackground="black", activeforeground="#00f", variable=b_var).grid(row=5, sticky='we')
o_b = tk.Checkbutton(foreground="black", background="#ffa500", text="ORANGE", activebackground="black", activeforeground="#ffa500", variable=o_var).grid(row=6, sticky='we')
w_b = tk.Checkbutton(foreground="black", background="#fff", text="WHITE", activebackground="black", activeforeground="#fff", variable=w_var).grid(row=7, sticky='we')
button = tk.Button(root, text="COMMIT", foreground="black", background="#fff", command=led_on_off).grid(row=8)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)

tk.mainloop()