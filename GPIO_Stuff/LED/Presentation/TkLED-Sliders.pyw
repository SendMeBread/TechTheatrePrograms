import RPi.GPIO as GPIO
import tkinter as tk

#Create window
root = tk.Tk()
root.attributes("-fullscreen", True)
root['bg'] = "black"
tk.Label(root, text="LED Fun!", fg='white', bg="black").grid(row=0, column=3)

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

r_var = tk.IntVar()
g_var = tk.IntVar()
y_var = tk.IntVar()
b_var = tk.IntVar()
o_var = tk.IntVar()
w_var = tk.IntVar()

#RED Functions
def r_add_1():
    global r_var
    r_var.set(r_var.get() + 1)
def r_sub_1():
    global r_var
    r_var.set(r_var.get() - 1)
def r_add_10():
    global r_var
    r_var.set(r_var.get() + 10)
def r_sub_10():
    global r_var
    r_var.set(r_var.get() - 10)
def r_max():
    global r_var
    r_var.set(100)
def r_off():
    global r_var
    r_var.set(0)
def r_trace(var, index, mode):
    print(str(r_var.get()))
    print(str(g_var.get()))
    p = GPIO.PWM(r, 50)
    p.start(0)
    try:
        while 1:
            p.ChangeDutyCycle(g_var)
    except KeyboardInterrupt:
        pass
#GREEN Functions
def g_add_1():
    global g_var
    g_var.set(g_var.get() + 1)
def g_sub_1():
    global g_var
    g_var.set(g_var.get() - 1)
def g_max():
    global g_var
    g_var.set(100)
def g_off():
    global g_var
    g_var.set(0)
def g_trace(var, index, mode):
    print(str(g_var.get()))
    p = GPIO.PWM(r, 50)
    p.start(0)
    try:
        while 1:
            p.ChangeDutyCycle(g_var)
    except KeyboardInterrupt:
        pass

#Sliders
r_scale = tk.Scale(root, fg="black", variable=r_var, from_= 0, to= 100, orient="horizontal", background="#f00", activebackground="#000").grid(row=1, column=4)
g_scale = tk.Scale(root, fg="black", variable=g_var, from_= 0, to= 100, orient="horizontal", background="#0f0", activebackground="#000").grid(row=2, column=2)
y_scale = tk.Scale(root, fg="black", variable=y_var, from_= 0, to= 100, orient="horizontal", background="#ff0", activebackground="#000").grid(row=3, column=2)
b_scale = tk.Scale(root, fg="black", variable=b_var, from_= 0, to= 100, orient="horizontal", background="#00f", activebackground="#000").grid(row=4, column=2)
o_scale = tk.Scale(root, fg="black", variable=o_var, from_= 0, to= 100, orient="horizontal", background="#ffa500", activebackground="#000").grid(row=5, column=2)
w_scale = tk.Scale(root, fg="black", variable=w_var, from_= 0, to= 100, orient="horizontal", background="#fff", activebackground="#000").grid(row=6, column=2)

#RED Buttons
tk.Button(root, width=5, text="OFF", command=r_off, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=1)
tk.Button(root, width=5, text="+10", command=r_add_10, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=6)
tk.Button(root, width=5, text="-1", command=r_sub_1, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=3)
tk.Button(root, width=5, text="-10", command=r_sub_10, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=2)
tk.Button(root, width=5, text="+1", command=r_add_1, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=5)
tk.Button(root, width=5, text="MAX", command=r_max, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=7)
#GREEN Buttons
tk.Button(root, width=5, text="OFF", fg="#000", bg="#0f0", borderwidth=0, activebackground="#000", activeforeground="#0f0").grid(row=2, column=7)

root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=0)
root.columnconfigure(4, weight=0)
root.columnconfigure(5, weight=0)
root.columnconfigure(6, weight=0)
root.columnconfigure(7, weight=0)

#Var Tracers
r_var.trace_add("write", r_trace)
g_var.trace_add("write", g_trace)

tk.mainloop()