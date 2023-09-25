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
tk.Label.grid(root, text="LED Fun!").grid(row=0)
#Checkbutton Tracking Vars
r_var = tk.IntVar()
g_var = tk.IntVar()
y_var = tk.IntVar()
b_var = tk.IntVar()
o_var = tk.IntVar()
w_var = tk.IntVar()

tk.Checkbutton(foreground="black", background="red", text="RED", activebackground="black", activeforeground="red", variable="r_var").grid(row=1)


tk.mainloop()