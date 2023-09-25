import RPi.GPIO as GPIO
from sys import argv
import tkinter as tk

r = 17
g = 18
y = 22
b = 23
o = 26
w = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(r, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(g, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(y, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(b, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(o, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(w, GPIO.OUT)

#Create window
root = tk.Tk()
root.attributes("-fullscreen", True)
root['bg'] = "black"
tk.Label(root, text="LED Fun!", fg='white', bg="black").grid(row=0)

#Checkbutton Tracking Vars
r_var = tk.IntVar()
g_var = tk.IntVar()
y_var = tk.IntVar()
b_var = tk.IntVar()
o_var = tk.IntVar()
w_var = tk.IntVar()

r_b = tk.Checkbutton(foreground="black", background="#f00", text="RED", activebackground="black", activeforeground="#f00", variable="r_var").grid(row=1, sticky='we')
g_b = tk.Checkbutton(foreground="black", background="#0f0", text="GREEN", activebackground="black", activeforeground="#0f0", variable="g_var").grid(row=2, sticky='we')
y_b = tk.Checkbutton(foreground="black", background="#ff0", text="YELLOW", activebackground="black", activeforeground="#ff0", variable="y_var").grid(row=3, sticky='we')
b_b = tk.Checkbutton(foreground="black", background="#0ff", text="BLUE", activebackground="black", activeforeground="#00f", variable="b_var").grid(row=4, sticky='we')
o_b = tk.Checkbutton(foreground="black", background="#ffa500", text="ORANGE", activebackground="black", activeforeground="#ffa500", variable="o_var").grid(row=5, sticky='we')
w_b = tk.Checkbutton(foreground="black", background="#fff", text="WHITE", activebackground="black", activeforeground="#fff", variable="w_var").grid(row=6, sticky='we')
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

tk.mainloop()