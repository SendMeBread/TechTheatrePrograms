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
    p = GPIO.PWM(r, val)
    p.start(0.0)
def green_pwm():
    val = g_var.get()
    p = GPIO.PWM(g, val)
    p.start(0.0)
def yellow_pwm():
    val = y_var.get()
    p = GPIO.PWM(y, val)
    p.start(0.0)
def blue_pwm():
    val = b_var.get()
    p = GPIO.PWM(b, val)
    p.start(0.0)
def orange_pwm():
    val = o_var.get()
    p = GPIO.PWM(o, val)
    p.start(0.0)
def white_pwm():
    val = w_var.get()
    p = GPIO.PWM(w, val)
    p.start(0.0)
    
        
r_var = tk.DoubleVar()
g_var = tk.DoubleVar()
y_var = tk.DoubleVar()
b_var = tk.DoubleVar()
o_var = tk.DoubleVar()
w_var = tk.DoubleVar()
r_scale = tk.Scale(root, variable=r_var, from_=0, to= 255, orient="vertical", background="#f00", activebackground="#000", command=red_pwm)
g_scale = tk.Scale(root, variable=g_var, from_=0, to= 255, orient="vertical", background="#0f0", activebackground="#000")
y_scale = tk.Scale(root, variable=y_var, from_=0, to= 255, orient="vertical", background="#ff0", activebackground="#000")
b_scale = tk.Scale(root, variable=b_var, from_=0, to= 255, orient="vertical", background="#00f", activebackground="#000")
o_scale = tk.Scale(root, variable=o_var, from_=0, to= 255, orient="vertical", background="#FFA500", activebackground="#000")
w_scale = tk.Scale(root, variable=w_var, from_=0, to= 255, orient="vertical", background="#fff", activebackground="#000")