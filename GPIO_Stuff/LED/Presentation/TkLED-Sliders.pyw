import RPi.GPIO as GPIO
import tkinter as tk

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

def red_pwm():
    val = r_var.get()
    p = GPIO.PWM(r, 50)
    p.start(0.0)
    try:
        while 1:
            p.ChangeDutyCycle(val)
    except KeyboardInterrupt:
        pass
def green_pwm():
    val = g_var.get()
    p = GPIO.PWM(g, 50)
    p.start(0.0)
    try:
        while 1:
            p.ChangeDutyCycle(val)
    except KeyboardInterrupt:
        pass
def yellow_pwm():
    val = y_var.get()
    p = GPIO.PWM(y, 50)
    p.start(0.0)
    try:
        while 1:
            p.ChangeDutyCycle(val)
    except KeyboardInterrupt:
        pass
def blue_pwm():
    val = b_var.get()
    p = GPIO.PWM(b, 50)
    p.start(0.0)
    try:
        while 1:
            p.ChangeDutyCycle(val)
    except KeyboardInterrupt:
        pass
def orange_pwm():
    val = o_var.get()
    p = GPIO.PWM(o, 50)
    p.start(0.0)
    try:
        while 1:
            p.ChangeDutyCycle(val)
    except KeyboardInterrupt:
        pass
def white_pwm():
    val = w_var.get()
    p = GPIO.PWM(w, 50)
    p.start(0.0)
    try:
        while 1:
            p.ChangeDutyCycle(val)
    except KeyboardInterrupt:
        pass
    
        
r_var = tk.DoubleVar()
g_var = tk.DoubleVar()
y_var = tk.DoubleVar()
b_var = tk.DoubleVar()
o_var = tk.DoubleVar()
w_var = tk.DoubleVar()
r_scale = tk.Scale(root, variable=r_var, from_=0, to= 100, orient="vertical", background="#f00", activebackground="#000", command=red_pwm)
g_scale = tk.Scale(root, variable=g_var, from_=0, to= 100, orient="vertical", background="#0f0", activebackground="#000", command=green_pwm)
y_scale = tk.Scale(root, variable=y_var, from_=0, to= 100, orient="vertical", background="#ff0", activebackground="#000", command=yellow_pwm)
b_scale = tk.Scale(root, variable=b_var, from_=0, to= 100, orient="vertical", background="#00f", activebackground="#000", command=blue_pwm)
o_scale = tk.Scale(root, variable=o_var, from_=0, to= 100, orient="vertical", background="#FFA500", activebackground="#000", command=orange_pwm)
w_scale = tk.Scale(root, variable=w_var, from_=0, to= 100, orient="vertical", background="#fff", activebackground="#000", command=white_pwm)